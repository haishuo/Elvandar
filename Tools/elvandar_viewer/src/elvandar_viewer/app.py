from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

from PySide6.QtCore import QEventLoop, QSettings, QStandardPaths, QTimer
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QFileDialog, QMessageBox

from .git import GitClient, GitError
from .navigation import normalized_scroll
from .outline import document_outline
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


def runtime_icon_path(platform: str) -> Path | None:
    # macOS owns the Dock icon through CFBundleIconFile. Replacing it through Qt
    # after launch bypasses the bundle's native sizing and makes the icon jump.
    if platform == "darwin":
        return None
    icon = resource_path("ElvandarViewer-transparent.png")
    return icon if icon.is_file() else None


def main(argv: list[str] | None = None) -> int:
    supplied = argv if argv is not None else sys.argv[1:]
    supplied = [argument for argument in supplied if not argument.startswith("-psn_")]
    arguments = build_parser().parse_args(supplied)
    if arguments.smoke_test:
        QStandardPaths.setTestModeEnabled(True)
    application = QApplication(sys.argv[:1])
    application.setApplicationName("Elvandar Viewer")
    application.setOrganizationName("Elvandar")
    settings = QSettings("Elvandar", "Elvandar Viewer")
    appearance_mode = stored_appearance_mode(settings)
    night_mode = night_mode_for(appearance_mode, system_uses_dark_mode(application))
    application.setStyleSheet(app_stylesheet(night_mode))
    icon = runtime_icon_path(sys.platform)
    if icon is not None:
        application.setWindowIcon(QIcon(str(icon)))

    try:
        root = locate_repository(arguments.repository)
        if root is None:
            return 0
        working_tree = Repository.open(root)
        repository = RepositoryView(working_tree, GitClient(working_tree.root))
    except (OSError, ValueError, GitError) as error:
        if arguments.smoke_test:
            print(f"Repository unavailable: {error}", file=sys.stderr)
        else:
            QMessageBox.critical(None, "Repository unavailable", str(error))
        return 2

    if not arguments.smoke_test:
        QSettings("Elvandar", "Elvandar Viewer").setValue(
            "repository/path", str(working_tree.root)
        )

    window = MainWindow(repository)
    window.show()
    if arguments.smoke_test:
        def settle_ui() -> None:
            loop = QEventLoop()
            QTimer.singleShot(220, loop.quit)
            loop.exec()

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
        outline_document = next(
            (
                document
                for document in documents
                if document_outline(repository.read_text(document))
            ),
            None,
        )
        if outline_document is not None:
            window._open_document(outline_document)
            window._show_mode("Rendered")
            settle_ui()
            window._set_contents_mode("outline")
            assert window.outline_list.count() == len(window.current_outline)
            target = min(2, len(window.current_outline) - 1)
            window._jump_to_outline(target)
            settle_ui()
            assert window.outline_list.currentRow() == target
            window._show_mode("Raw")
            settle_ui()
            window._jump_to_outline(target)
            settle_ui()
            assert (
                window.reader.textCursor().blockNumber()
                == window.current_outline[target].line
            )
            window._set_contents_mode("folder")
        if documents:
            position_document = max(
                documents,
                key=lambda document: len(repository.read_text(document)),
            )
            window._open_document(position_document)
            window._show_mode("Rendered")
            rendered_blocks = window.reader.document().blockCount()
            if rendered_blocks > 1:
                change_blocks = [0, rendered_blocks - 1]
                window._set_live_change_navigation(change_blocks)
                window._go_to_next_change()
                first_change = window.reader.textCursor().blockNumber()
                assert first_change in change_blocks
                window._go_to_next_change()
                assert window.reader.textCursor().blockNumber() in change_blocks
                window._show_mode("Raw")
                assert window.change_navigator.isHidden()
                window._show_mode("Rendered")
                assert not window.change_navigator.isHidden()
                window._clear_live_change_navigation()
            window._show_mode("Diff")
            assert window.diff_selector.count() >= 1
            window._show_mode("Rendered")
            settle_ui()
            window._finish_pending_scroll_restore()
            rendered_scroll = window.reader.verticalScrollBar()
            if rendered_scroll.maximum() > 0:
                rendered_scroll.setValue(round(rendered_scroll.maximum() * 0.72))
                rendered_value = rendered_scroll.value()
                rendered_ratio = normalized_scroll(
                    rendered_scroll.value(), rendered_scroll.maximum()
                )
                window._show_mode("Raw")
                settle_ui()
                raw_scroll = window.reader.verticalScrollBar()
                raw_ratio = normalized_scroll(raw_scroll.value(), raw_scroll.maximum())
                assert abs(rendered_ratio - raw_ratio) < 0.08
                for _iteration in range(6):
                    window._show_mode("Rendered")
                    settle_ui()
                    returned_scroll = window.reader.verticalScrollBar()
                    returned_ratio = normalized_scroll(
                        returned_scroll.value(), returned_scroll.maximum()
                    )
                    assert returned_scroll.value() == rendered_value
                    assert abs(raw_ratio - returned_ratio) < 0.08
                    window._show_mode("Raw")
                    settle_ui()
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
