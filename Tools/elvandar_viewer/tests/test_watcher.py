from __future__ import annotations

import time
from pathlib import Path

from PySide6.QtCore import QCoreApplication

from elvandar_viewer.repository import Repository
from elvandar_viewer.watcher import RepositoryWatcher


def _wait_until(application: QCoreApplication, predicate: object, timeout: float = 3.0) -> bool:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        application.processEvents()
        if predicate():
            return True
        time.sleep(0.02)
    return False


def test_watcher_recovers_after_atomic_save_notification(tmp_path: Path) -> None:
    application = QCoreApplication.instance() or QCoreApplication([])
    document = tmp_path / "chapter.md"
    document.write_text("First version", encoding="utf-8")
    watcher = RepositoryWatcher(Repository.open(tmp_path))
    changes: list[Path] = []
    watcher.document_changed.connect(changes.append)
    watcher.set_document(document)
    application.processEvents()
    time.sleep(0.05)
    application.processEvents()

    replacement = tmp_path / "replacement.tmp"
    replacement.write_text("Second version", encoding="utf-8")
    replacement.replace(document)
    watcher._directory_changed(str(tmp_path))

    assert _wait_until(application, lambda: len(changes) == 1)

    document.write_text("Third version", encoding="utf-8")
    watcher._file_changed(str(document))

    assert _wait_until(application, lambda: len(changes) == 2)


def test_watcher_waits_for_temporarily_missing_document(tmp_path: Path) -> None:
    application = QCoreApplication.instance() or QCoreApplication([])
    document = tmp_path / "chapter.md"
    document.write_text("Before", encoding="utf-8")
    watcher = RepositoryWatcher(Repository.open(tmp_path))
    availability: list[bool] = []
    changes: list[Path] = []
    watcher.document_availability_changed.connect(availability.append)
    watcher.document_changed.connect(changes.append)
    watcher.set_document(document)

    document.unlink()
    watcher._directory_changed(str(tmp_path))
    assert _wait_until(application, lambda: availability == [False])

    document.write_text("After", encoding="utf-8")
    watcher._directory_changed(str(tmp_path))
    assert _wait_until(application, lambda: changes == [document])
    assert availability[-1] is True
