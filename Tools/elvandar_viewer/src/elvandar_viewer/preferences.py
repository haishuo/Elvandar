from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import QSettings, Qt
from PySide6.QtWidgets import (
    QButtonGroup,
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


APPEARANCE_MODES = {"system", "day", "night"}
READING_WIDTHS = (1120, 1400, 1680)
DEFAULT_FONT_SIZE = 18
MIN_FONT_SIZE = 14
MAX_FONT_SIZE = 30


def stored_appearance_mode(settings: QSettings) -> str:
    mode = settings.value("appearance/mode", "", type=str)
    if mode in APPEARANCE_MODES:
        return mode
    if settings.contains("appearance/night_mode"):
        return "night" if settings.value("appearance/night_mode", False, type=bool) else "day"
    return "system"


def night_mode_for(appearance_mode: str, system_is_dark: bool) -> bool:
    if appearance_mode == "night":
        return True
    if appearance_mode == "day":
        return False
    return system_is_dark


def reading_page_width(configured_width: int, window_width: int) -> int:
    return min(configured_width, max(680, window_width - 96))


def clamp_font_size(font_size: int) -> int:
    return min(MAX_FONT_SIZE, max(MIN_FONT_SIZE, font_size))


def system_uses_dark_mode(application: QApplication) -> bool:
    return application.styleHints().colorScheme() == Qt.ColorScheme.Dark


@dataclass(frozen=True, slots=True)
class SettingsValues:
    appearance_mode: str = "system"
    reading_width: int = 1400
    font_size: int = DEFAULT_FONT_SIZE
    remember_reading_mode: bool = True
    highlight_live_changes: bool = True


class SettingsDialog(QDialog):
    def __init__(self, values: SettingsValues, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setObjectName("settingsDialog")
        self.setWindowTitle("Settings")
        self.setWindowModality(Qt.WindowModality.WindowModal)
        self.setMinimumWidth(500)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(28, 24, 28, 22)
        layout.setSpacing(18)
        layout.addWidget(QLabel("Elvandar Viewer Settings", objectName="settingsTitle"))

        appearance = self._section("APPEARANCE")
        self.appearance_group = QButtonGroup(self)
        self.appearance_buttons: dict[str, QRadioButton] = {}
        for mode, label, description in (
            ("system", "Match macOS", "Follow the current macOS appearance automatically."),
            ("day", "Day mode", "Always use the light reading palette."),
            ("night", "Night mode", "Always use the low-light reading palette."),
        ):
            radio = QRadioButton(label, objectName="settingsRadio")
            radio.setProperty("appearanceMode", mode)
            radio.setChecked(mode == values.appearance_mode)
            self.appearance_group.addButton(radio)
            self.appearance_buttons[mode] = radio
            appearance.layout().addWidget(radio)
            appearance.layout().addWidget(QLabel(description, objectName="settingsDescription"))
        layout.addWidget(appearance)

        reading = self._section("READING")
        width_row = QHBoxLayout()
        width_row.addWidget(QLabel("Page width", objectName="settingsLabel"))
        width_row.addStretch(1)
        self.reading_width = QComboBox(objectName="settingsCombo")
        for label, width in (("Narrow", 1120), ("Comfortable", 1400), ("Wide", 1680)):
            self.reading_width.addItem(label, width)
        selected_width = values.reading_width if values.reading_width in READING_WIDTHS else 1400
        self.reading_width.setCurrentIndex(self.reading_width.findData(selected_width))
        width_row.addWidget(self.reading_width)
        reading.layout().addLayout(width_row)

        text_size_row = QHBoxLayout()
        text_size_row.addWidget(QLabel("Text size", objectName="settingsLabel"))
        text_size_row.addStretch(1)
        self.font_size = QSpinBox(objectName="settingsSpin")
        self.font_size.setRange(MIN_FONT_SIZE, MAX_FONT_SIZE)
        self.font_size.setSuffix(" px")
        self.font_size.setValue(clamp_font_size(values.font_size))
        text_size_row.addWidget(self.font_size)
        reading.layout().addLayout(text_size_row)

        self.remember_reading = QCheckBox(
            "Remember Reading Mode between launches", objectName="settingsCheck"
        )
        self.remember_reading.setChecked(values.remember_reading_mode)
        reading.layout().addWidget(self.remember_reading)
        layout.addWidget(reading)

        live_updates = self._section("LIVE UPDATES")
        self.highlight_changes = QCheckBox(
            "Briefly highlight paragraphs changed by Claude", objectName="settingsCheck"
        )
        self.highlight_changes.setChecked(values.highlight_live_changes)
        live_updates.layout().addWidget(self.highlight_changes)
        layout.addWidget(live_updates)

        buttons = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok
        )
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        for button in buttons.buttons():
            button.setObjectName("settingsDialogButton")
        layout.addWidget(buttons)

    @staticmethod
    def _section(title: str) -> QFrame:
        section = QFrame(objectName="settingsSection")
        layout = QVBoxLayout(section)
        layout.setContentsMargins(16, 14, 16, 15)
        layout.setSpacing(7)
        layout.addWidget(QLabel(title, objectName="settingsSectionTitle"))
        return section

    def values(self) -> SettingsValues:
        appearance_mode = next(
            mode for mode, button in self.appearance_buttons.items() if button.isChecked()
        )
        return SettingsValues(
            appearance_mode=appearance_mode,
            reading_width=int(self.reading_width.currentData()),
            font_size=self.font_size.value(),
            remember_reading_mode=self.remember_reading.isChecked(),
            highlight_live_changes=self.highlight_changes.isChecked(),
        )
