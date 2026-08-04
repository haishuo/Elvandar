from __future__ import annotations

import os
import subprocess
from pathlib import Path

from elvandar_viewer.git import GitClient
from elvandar_viewer.repository import Repository
from elvandar_viewer.repository_view import RepositoryView


def _git(root: Path, *arguments: str) -> str:
    environment = os.environ.copy()
    environment.update(
        {
            "GIT_AUTHOR_NAME": "Elvandar Test",
            "GIT_AUTHOR_EMAIL": "test@elvandar.invalid",
            "GIT_COMMITTER_NAME": "Elvandar Test",
            "GIT_COMMITTER_EMAIL": "test@elvandar.invalid",
        }
    )
    result = subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env=environment,
    )
    return result.stdout.strip()


def _repository(tmp_path: Path) -> tuple[GitClient, Path]:
    _git(tmp_path, "init", "-b", "main")
    chapter = tmp_path / "Book 1" / "Chapter 1.md"
    chapter.parent.mkdir()
    chapter.write_text("Committed chapter", encoding="utf-8")
    _git(tmp_path, "add", "Book 1/Chapter 1.md")
    _git(tmp_path, "commit", "-m", "Add opening chapter")
    _git(tmp_path, "branch", "alternate")
    return GitClient(tmp_path), chapter


def test_git_client_reads_status_history_branches_and_worktrees(tmp_path: Path) -> None:
    git, chapter = _repository(tmp_path)
    chapter.write_text("Working draft", encoding="utf-8")

    assert git.current_branch() == "main"
    assert git.current_branch_name() == "main"
    assert git.preferred_base_branch() == "main"
    assert git.merge_base("main", "alternate")
    assert [branch.name for branch in git.branches()] == ["main", "alternate"]
    assert git.recent_commits()[0].subject == "Add opening chapter"
    assert git.worktrees()[0].branch == "main"
    assert git.changes()[0].path.as_posix() == "Book 1/Chapter 1.md"
    assert git.paths_changed_since("HEAD") == {git.changes()[0].path}
    assert git.list_files("alternate")[0].as_posix() == "Book 1/Chapter 1.md"
    assert git.show_file("alternate", git.list_files("alternate")[0]) == "Committed chapter"
    assert list(git.show_files("alternate", git.list_files("alternate")).values()) == ["Committed chapter"]
    assert git.metadata_watch_paths()


def test_branch_snapshot_does_not_switch_or_overwrite_working_tree(tmp_path: Path) -> None:
    git, chapter = _repository(tmp_path)
    chapter.write_text("Claude is editing this version", encoding="utf-8")
    view = RepositoryView(Repository.open(tmp_path), git)

    working_diff = view.diff_versions(chapter)
    assert working_diff.before == "Committed chapter"
    assert working_diff.after == "Claude is editing this version"
    assert working_diff.after_label == "Working tree"

    view.show_revision("alternate")
    snapshot_text = view.read_text(chapter)
    snapshot_diff = view.diff_versions(chapter)

    assert [path.name for path in view.directories()] == ["Book 1"]
    assert [path.name for path in view.contents(tmp_path / "Book 1")] == ["Chapter 1.md"]
    assert snapshot_text == "Committed chapter"
    assert snapshot_diff.before == ""
    assert snapshot_diff.after == "Committed chapter"
    assert chapter.read_text(encoding="utf-8") == "Claude is editing this version"
    assert git.current_branch() == "main"


def test_linked_worktree_can_be_opened_as_an_independent_read_only_view(tmp_path: Path) -> None:
    git, chapter = _repository(tmp_path)
    linked = tmp_path.parent / f"{tmp_path.name}-alternate"
    _git(tmp_path, "worktree", "add", str(linked), "alternate")
    linked_chapter = linked / "Book 1" / "Chapter 1.md"
    linked_chapter.write_text("Alternate worktree draft", encoding="utf-8")
    chapter.write_text("Main worktree draft", encoding="utf-8")

    linked_view = RepositoryView(Repository.open(linked), GitClient(linked))

    assert linked_view.read_text(linked_chapter) == "Alternate worktree draft"
    assert chapter.read_text(encoding="utf-8") == "Main worktree draft"
    assert GitClient(tmp_path).current_branch() == "main"
    assert GitClient(linked).current_branch() == "alternate"


def test_feature_worktree_diff_defaults_to_committed_branch_changes(tmp_path: Path) -> None:
    _git_client, _chapter = _repository(tmp_path)
    linked = tmp_path.parent / f"{tmp_path.name}-feature"
    _git(tmp_path, "worktree", "add", str(linked), "alternate")
    linked_chapter = linked / "Book 1" / "Chapter 1.md"
    linked_chapter.write_text("**Committed chapter**", encoding="utf-8")
    _git(linked, "add", "Book 1/Chapter 1.md")
    _git(linked, "commit", "-m", "Use bold emphasis")
    view = RepositoryView(Repository.open(linked), GitClient(linked))

    comparisons = view.diff_comparisons()
    branch_diff = view.diff_versions(linked_chapter)
    uncommitted_diff = view.diff_versions(linked_chapter, "working")

    assert [(item.key, item.label) for item in comparisons] == [
        ("branch", "Branch vs main"),
        ("working", "Uncommitted"),
    ]
    assert branch_diff.before == "Committed chapter"
    assert branch_diff.after == "**Committed chapter**"
    assert branch_diff.before_label == "Base · main"
    assert branch_diff.after_label == "Worktree · alternate"
    assert uncommitted_diff.before == uncommitted_diff.after == "**Committed chapter**"
    assert {path.as_posix() for path in view.changed_paths()} == {"Book 1/Chapter 1.md"}


def test_main_view_surfaces_files_from_the_latest_commit(tmp_path: Path) -> None:
    git, chapter = _repository(tmp_path)
    chapter.write_text("A newly committed chapter", encoding="utf-8")
    _git(tmp_path, "add", "Book 1/Chapter 1.md")
    _git(tmp_path, "commit", "-m", "Revise the opening chapter")
    view = RepositoryView(Repository.open(tmp_path), git)

    assert {path.as_posix() for path in view.changed_paths()} == {
        "Book 1/Chapter 1.md"
    }


def test_converged_feature_worktree_falls_back_to_its_latest_commit(tmp_path: Path) -> None:
    _git_client, _chapter = _repository(tmp_path)
    linked = tmp_path.parent / f"{tmp_path.name}-converged"
    _git(tmp_path, "worktree", "add", str(linked), "alternate")
    linked_chapter = linked / "Book 1" / "Chapter 1.md"
    linked_chapter.write_text("The latest finished chapter", encoding="utf-8")
    _git(linked, "add", "Book 1/Chapter 1.md")
    _git(linked, "commit", "-m", "Finish the chapter")
    _git(tmp_path, "merge", "--ff-only", "alternate")
    view = RepositoryView(Repository.open(linked), GitClient(linked))

    assert {path.as_posix() for path in view.changed_paths()} == {
        "Book 1/Chapter 1.md"
    }
