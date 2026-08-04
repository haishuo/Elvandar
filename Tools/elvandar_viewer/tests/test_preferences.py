from PySide6.QtWidgets import QApplication

from elvandar_viewer.preferences import (
    SettingsDialog,
    SettingsValues,
    clamp_font_size,
    night_mode_for,
    reading_page_width,
)


def test_appearance_mode_can_follow_or_override_the_system() -> None:
    assert night_mode_for("system", system_is_dark=True)
    assert not night_mode_for("system", system_is_dark=False)
    assert night_mode_for("night", system_is_dark=False)
    assert not night_mode_for("day", system_is_dark=True)


def test_settings_dialog_preserves_all_preferences() -> None:
    _application = QApplication.instance() or QApplication([])
    expected = SettingsValues(
        appearance_mode="night",
        reading_width=1680,
        font_size=24,
        remember_reading_mode=False,
        highlight_live_changes=False,
    )

    dialog = SettingsDialog(expected)

    assert dialog.values() == expected


def test_reading_page_width_is_wide_but_responsive() -> None:
    assert reading_page_width(1400, 2048) == 1400
    assert reading_page_width(1400, 1200) == 1104
    assert reading_page_width(1680, 700) == 680


def test_font_size_is_limited_to_a_readable_range() -> None:
    assert clamp_font_size(12) == 14
    assert clamp_font_size(22) == 22
    assert clamp_font_size(40) == 30
