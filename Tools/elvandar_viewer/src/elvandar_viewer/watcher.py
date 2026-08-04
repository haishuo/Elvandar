from __future__ import annotations

from pathlib import Path

from PySide6.QtCore import QFileSystemWatcher, QObject, QTimer, Signal

from .repository import Repository


FileSignature = tuple[int, int]


class RepositoryWatcher(QObject):
    """Observe a repository without opening or locking any file for writing."""

    document_changed = Signal(object)
    document_availability_changed = Signal(bool)
    structure_changed = Signal()
    repository_touched = Signal()
    files_changed = Signal(object)

    def __init__(self, repository: Repository, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.repository = repository
        self._watcher = QFileSystemWatcher(self)
        self._watcher.fileChanged.connect(self._file_changed)
        self._watcher.directoryChanged.connect(self._directory_changed)

        self._document: Path | None = None
        self._last_emitted_signature: FileSignature | None = None
        self._candidate_signature: FileSignature | None = None
        self._document_pending = False
        self._structure_pending = False
        self._structure_snapshot = repository.structure_snapshot()
        self._touched_files: set[Path] = set()

        self._settle_timer = QTimer(self)
        self._settle_timer.setSingleShot(True)
        self._settle_timer.setInterval(140)
        self._settle_timer.timeout.connect(self._flush)
        self._sync_directory_watches()

    def set_document(self, path: Path | None) -> None:
        self._document = self.repository.resolve(path) if path is not None else None
        self._candidate_signature = None
        self._last_emitted_signature = self._signature(self._document)
        self._document_pending = False
        self._ensure_document_watch()

    def _file_changed(self, changed_path: str) -> None:
        self._touched_files.add(Path(changed_path))
        if self._document is not None and Path(changed_path) == self._document:
            self._document_pending = True
        self._structure_pending = True
        self._settle_timer.start()

    def _directory_changed(self, changed_path: str) -> None:
        self._structure_pending = True
        if self._document is not None and Path(changed_path) == self._document.parent:
            self._document_pending = True
        self._settle_timer.start()

    def _flush(self) -> None:
        self._sync_directory_watches()
        self.repository_touched.emit()

        if self._structure_pending:
            self._structure_pending = False
            snapshot = self.repository.structure_snapshot()
            if snapshot != self._structure_snapshot:
                self._structure_snapshot = snapshot
                self.structure_changed.emit()

        if not self._document_pending or self._document is None:
            self._emit_file_changes()
            return

        signature = self._signature(self._document)
        if signature is None:
            self._document_pending = False
            self._candidate_signature = None
            self.document_availability_changed.emit(False)
            self._emit_file_changes()
            return

        # Require the size and modification time to remain unchanged for one
        # quiet interval. This avoids displaying a half-written save.
        if signature != self._candidate_signature:
            self._candidate_signature = signature
            self._settle_timer.start()
            return

        self._document_pending = False
        self._candidate_signature = None
        self._ensure_document_watch()
        self.document_availability_changed.emit(True)
        if signature != self._last_emitted_signature:
            self._last_emitted_signature = signature
            self.document_changed.emit(self._document)
        self._emit_file_changes()

    def _emit_file_changes(self) -> None:
        if not self._touched_files:
            return
        changed = sorted(self._touched_files, key=str)
        self._touched_files.clear()
        self.files_changed.emit(changed)

    def _sync_directory_watches(self) -> None:
        desired_directories = {str(path) for path in self.repository.walk_directories()}
        desired_files = {str(path) for path in self.repository.walk_visible_files()}
        current_directories = set(self._watcher.directories())
        current_files = set(self._watcher.files())
        desired = desired_directories | desired_files
        current = current_directories | current_files
        stale = current - desired
        missing = desired - current
        if stale:
            self._watcher.removePaths(sorted(stale))
        if missing:
            self._watcher.addPaths(sorted(missing))
        self._ensure_document_watch()

    def _ensure_document_watch(self) -> None:
        if self._document is None or not self._document.is_file():
            return
        document = str(self._document)
        if document not in self._watcher.files():
            self._watcher.addPath(document)

    @staticmethod
    def _signature(path: Path | None) -> FileSignature | None:
        if path is None:
            return None
        try:
            stat = path.stat()
        except OSError:
            return None
        return stat.st_mtime_ns, stat.st_size
