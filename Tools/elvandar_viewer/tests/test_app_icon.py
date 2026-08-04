from __future__ import annotations

from pathlib import Path

from PySide6.QtGui import QImage

from elvandar_viewer.app import runtime_icon_path


ICON_PATH = Path(__file__).resolve().parents[1] / "assets" / "ElvandarViewer-transparent.png"


def test_app_icon_has_transparent_outer_corners() -> None:
    icon = QImage(str(ICON_PATH))

    assert not icon.isNull()
    assert icon.width() >= 1024
    assert icon.height() >= 1024
    assert icon.hasAlphaChannel()

    corners = (
        (0, 0),
        (icon.width() - 1, 0),
        (0, icon.height() - 1),
        (icon.width() - 1, icon.height() - 1),
    )
    assert all(icon.pixelColor(x, y).alpha() == 0 for x, y in corners)
    assert icon.pixelColor(icon.width() // 2, icon.height() // 2).alpha() == 255


def test_macos_keeps_the_bundle_icon_after_launch() -> None:
    assert runtime_icon_path("darwin") is None


def test_other_platforms_receive_the_runtime_icon() -> None:
    assert runtime_icon_path("linux") == ICON_PATH
