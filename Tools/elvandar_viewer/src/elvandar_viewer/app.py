from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from PySide6.QtCore import QSettings, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox

from .git import GitClient, GitError
from .preferences import night_mode_for, stored_appearance_mode, system_uses_dark_mode
from .repository import Repository, discover_repository
from .repository_view import RepositoryView
from .theme import app_stylesheet
from .window import MainWindow


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read a Markdown repository without modifying it")
    parser.add_argument("repository", nargs="?", help="Repository to open (defaults to the current repository)")
    parser.add_argument("--smoke-test", action="store_true", help=argparse.SUPPRESS)
    return parser


def locate_repository(explicit: str | None) -> Path | None:
    if explicit:
        return Path(explicit).expanduser()

    settings = QSettings("Elvandar", "Elvandar Viewer")
    saved = settings.value("repository/path", "", type=str)
    candidates = [
        os.environ.get("ELVANDAR_REPOSITORY", ""),
        saved,
        "/Volumes/Archive/Documents/Dropbox/Elvandar",
        str(Path.home() / "Dropbox" / "Elvandar"),
        str(Path.home() / "Documents" / "Elvandar"),
    ]
    try:
        candidates.append(str(discover_repository(os.getcwd())))
    except OSError:
        pass

    for candidate_text in candidates:
        if not candidate_text:
            continue
        candidate = Path(candidate_text).expanduser()
        if candidate.is_dir() and (candidate / ".git").exists():
            return candidate

    chosen = QFileDialog.getExistingDirectory(
        None,
        "Choose the Elvandar repository",
        str(Path.home()),
        QFileDialog.Option.ShowDirsOnly,
    )
    return Path(chosen) if chosen else None


def resource_path(name: str) -> Path:
    bundle_root = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parents[2]))
    return bundle_root / "assets" / name


def main(argv: list[str] | None = None) -> int:
    supplied = argv if argv is not None else sys.argv[1:]
    supplied = [argument for argument in supplied if not argument.startswith("-psn_")]
    arguments = build_parser().parse_args(supplied)
    application = QApplication(sys.argv[:1])
    application.setApplicationName("Elvandar Viewer")
    application.setOrganizationName("Elvandar")
    settings = QSettings("Elvandar", "Elvandar Viewer")
    appearance_mode = stored_appearance_mode(settings)
    night_mode = night_mode_for(appearance_mode, system_uses_dark_mode(application))
    application.setStyleSheet(app_stylesheet(night_mode))
    icon = resource_path("ElvandarViewer-source.png")
    if icon.is_file():
        application.setWindowIcon(QIcon(str(icon)))

    try:
        root = locate_repository(arguments.repository)
        if root is None:
            return 0
        working_tree = Repository.open(root)
        repository = RepositoryView(working_tree, GitClient(working_tree.root))
    except (OSError, ValueError, GitError) as error:
        QMessageBox.critical(None, "Repository unavailable", str(error))
        return 2

    QSettings("Elvandar", "Elvandar Viewer").setValue("repository/path", str(working_tree.root))

    window = MainWindow(repository)
    window.show()
    if arguments.smoke_test:
        documents = repository.all_documents()
        if documents:
            window._open_document(documents[0])
        if len(documents) > 1:
            first_document = documents[0]
            second_document = documents[1]
            window._open_document(second_document)
            window._go_back()
            assert window.current_document == first_document
            window._go_forward()
            assert window.current_document == second_document
        original_night_mode = window.night_mode
        original_reading_mode = window.reading_mode
        original_font_size = window.reading_font_size
        window._apply_night_mode(not original_night_mode)
        window._set_reading_font_size(original_font_size + 1, persist=False)
        window._set_reading_mode(not original_reading_mode, persist=False)
        window._set_reading_mode(original_reading_mode, persist=False)
        window._set_reading_font_size(original_font_size, persist=False)
        window._apply_night_mode(original_night_mode)
        QTimer.singleShot(750, application.quit)
    return application.exec()


if __name__ == "__main__":
    raise SystemExit(main())
