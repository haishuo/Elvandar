from pathlib import Path

import pytest

from elvandar_viewer.repository import Repository, RepositoryBoundaryError


def test_repository_lists_supported_documents_and_folders(tmp_path: Path) -> None:
    (tmp_path / "Book 1").mkdir()
    (tmp_path / "Chapter.md").write_text("# Chapter", encoding="utf-8")
    (tmp_path / "cover.png").write_bytes(b"not an image")
    (tmp_path / ".git").mkdir()

    repository = Repository.open(tmp_path)

    assert [item.name for item in repository.contents(tmp_path)] == ["Book 1", "Chapter.md", "cover.png"]
    assert repository.read_binary(tmp_path / "cover.png") == b"not an image"


def test_repository_refuses_paths_outside_root(tmp_path: Path) -> None:
    root = tmp_path / "repository"
    root.mkdir()
    repository = Repository.open(root)

    with pytest.raises(RepositoryBoundaryError):
        repository.resolve(tmp_path / "elsewhere.md")


def test_read_text_replaces_incomplete_utf8(tmp_path: Path) -> None:
    document = tmp_path / "draft.md"
    document.write_bytes(b"A draft in progress: \xe2\x80")
    repository = Repository.open(tmp_path)

    assert repository.read_text(document).startswith("A draft in progress:")
