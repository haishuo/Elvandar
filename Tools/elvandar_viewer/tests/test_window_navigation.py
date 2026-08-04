from __future__ import annotations

import os
import subprocess
from pathlib import Path

from PySide6.QtCore import QSettings, QStandardPaths
from PySide6.QtWidgets import QApplication

from elvandar_viewer.git import GitClient
from elvandar_viewer.repository import Repository
from elvandar_viewer.repository_view import RepositoryView
from elvandar_viewer.window import PATH_ROLE, MainWindow


def _git(root: Path, *arguments: str) -> None:
    environment = os.environ.copy()
    environment.update(
        {
            "GIT_AUTHOR_NAME": "Elvandar Test",
            "GIT_AUTHOR_EMAIL": "test@elvandar.invalid",
            "GIT_COMMITTER_NAME": "Elvandar Test",
            "GIT_COMMITTER_EMAIL": "test@elvandar.invalid",
        }
    )
    subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
    )


def _repository(tmp_path: Path) -> tuple[RepositoryView, Path]:
    _git(tmp_path, "init", "-b", "main")
    chapter = tmp_path / "Book 1" / "Chapters" / "Chapter 2 - Arrival.md"
    chapter.parent.mkdir(parents=True)
    chapter.write_text(
        "First paragraph.\n\nSecond paragraph.\n\nThird paragraph.",
        encoding="utf-8",
    )
    _git(tmp_path, "add", chapter.relative_to(tmp_path).as_posix())
    _git(tmp_path, "commit", "-m", "Add chapter")
    return RepositoryView(Repository.open(tmp_path), GitClient(tmp_path)), chapter


def _application() -> QApplication:
    QStandardPaths.setTestModeEnabled(True)
    return QApplication.instance() or QApplication([])


def test_restored_document_is_revealed_in_both_navigation_panels(
    tmp_path: Path,
) -> None:
    _app = _application()
    repository, chapter = _repository(tmp_path)
    window = MainWindow(repository)
    window.settings.remove(window.settings_prefix)
    window._open_document(chapter)
    window._save_repository_state()
    window.settings.sync()

    restored = MainWindow(
        RepositoryView(Repository.open(tmp_path), GitClient(tmp_path))
    )

    assert restored.current_document == chapter
    selected_folder = restored.folder_tree.currentItem()
    assert selected_folder is not None
    assert Path(selected_folder.data(0, PATH_ROLE)) == chapter.parent
    selected_document = restored.document_list.currentItem()
    assert selected_document is not None
    assert Path(selected_document.data(PATH_ROLE)) == chapter
    assert selected_folder.isExpanded()

    restored.close()
    window.close()
    QSettings("Elvandar", "Elvandar Viewer").remove(restored.settings_prefix)


def test_live_change_controls_jump_and_wrap_between_changed_paragraphs(
    tmp_path: Path,
) -> None:
    _app = _application()
    repository, chapter = _repository(tmp_path)
    window = MainWindow(repository)
    settings_prefix = window.settings_prefix
    window.settings.remove(settings_prefix)
    window._open_document(chapter)
    changed_blocks = [0, window.reader.document().blockCount() - 1]
    assert len(set(changed_blocks)) == 2

    window._set_live_change_navigation(changed_blocks)
    window._go_to_next_change()

    assert not window.change_navigator.isHidden()
    first_target = window.reader.textCursor().blockNumber()
    assert first_target in changed_blocks
    assert window.change_position.text() in {"1 OF 2", "2 OF 2"}

    window._go_to_next_change()
    second_target = window.reader.textCursor().blockNumber()
    assert second_target in changed_blocks
    assert second_target != first_target
    window._go_to_next_change()
    assert window.reader.textCursor().blockNumber() == first_target
    window._go_to_previous_change()
    assert window.reader.textCursor().blockNumber() == second_target

    window._show_mode("Raw")
    assert window.change_navigator.isHidden()
    assert not window.next_change_action.isEnabled()
    window._show_mode("Rendered")
    assert not window.change_navigator.isHidden()

    window.close()
    QSettings("Elvandar", "Elvandar Viewer").remove(settings_prefix)
