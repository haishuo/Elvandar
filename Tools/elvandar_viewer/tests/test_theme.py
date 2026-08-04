from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication, QListWidget, QTreeWidget

from elvandar_viewer.theme import APP_STYLESHEET, app_stylesheet


def test_navigation_lists_keep_dark_text_in_dark_macos_appearance() -> None:
    application = QApplication.instance() or QApplication([])
    previous_stylesheet = application.styleSheet()
    application.setStyleSheet(APP_STYLESHEET)
    try:
        for widget in (QTreeWidget(), QListWidget()):
            widget.ensurePolished()
            assert widget.palette().color(QPalette.ColorRole.Text).name() == "#414a58"
            assert widget.palette().color(QPalette.ColorRole.HighlightedText).name() == "#1d2b3d"
    finally:
        application.setStyleSheet(previous_stylesheet)


def test_night_mode_sets_readable_navigation_colors() -> None:
    application = QApplication.instance() or QApplication([])
    previous_stylesheet = application.styleSheet()
    application.setStyleSheet(app_stylesheet(True))
    try:
        for widget in (QTreeWidget(), QListWidget()):
            widget.ensurePolished()
            assert widget.palette().color(QPalette.ColorRole.Text).name() == "#c9ced8"
            assert widget.palette().color(QPalette.ColorRole.HighlightedText).name() == "#f2f5f9"
    finally:
        application.setStyleSheet(previous_stylesheet)
