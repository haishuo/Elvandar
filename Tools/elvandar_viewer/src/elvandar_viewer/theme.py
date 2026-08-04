from __future__ import annotations


LIGHT_PALETTE = {
    "app": "#E9EBEF",
    "text": "#252932",
    "pane": "#F4F5F7",
    "reader": "#FCFCFD",
    "border": "#D5D8DE",
    "eyebrow": "#737B89",
    "title": "#1D222C",
    "repository": "#171B24",
    "muted": "#69717F",
    "metadata": "#8A919D",
    "input": "#FFFFFF",
    "input_border": "#D4D8DF",
    "input_focus": "#7698C4",
    "selection": "#DFE7F2",
    "selection_text": "#1D2B3D",
    "navigation_text": "#414A58",
    "compact": "#ECEEF2",
    "compact_text": "#4E5664",
    "button": "#626A78",
    "button_checked": "#1E2D41",
    "button_background": "#E3E9F2",
    "button_disabled": "#ADB2BB",
    "scrollbar": "#C5CAD2",
    "badge_blue_text": "#315D9B",
    "badge_blue_background": "#E4EBF5",
    "badge_blue_border": "#CBD8E9",
    "badge_green_text": "#477056",
    "badge_green_background": "#E5EFE8",
    "badge_green_border": "#CEE0D3",
    "badge_amber_text": "#8A6629",
    "badge_amber_background": "#F4EAD4",
    "badge_amber_border": "#E6D4AA",
    "badge_waiting_text": "#8B5A36",
    "badge_waiting_background": "#F3E4DA",
    "badge_waiting_border": "#E4CBBB",
}

DARK_PALETTE = {
    "app": "#191C21",
    "text": "#D7DBE4",
    "pane": "#22262D",
    "reader": "#191C21",
    "border": "#343A44",
    "eyebrow": "#8F98A7",
    "title": "#EEF0F4",
    "repository": "#F4F5F7",
    "muted": "#A1A8B4",
    "metadata": "#858F9F",
    "input": "#2A2F37",
    "input_border": "#414854",
    "input_focus": "#7197C8",
    "selection": "#35445A",
    "selection_text": "#F2F5F9",
    "navigation_text": "#C9CED8",
    "compact": "#292E36",
    "compact_text": "#B5BCC8",
    "button": "#A4ACB9",
    "button_checked": "#F1F4F8",
    "button_background": "#344157",
    "button_disabled": "#626A76",
    "scrollbar": "#4A525E",
    "badge_blue_text": "#8CAFD9",
    "badge_blue_background": "#29384B",
    "badge_blue_border": "#3B5069",
    "badge_green_text": "#7EB08D",
    "badge_green_background": "#263A2D",
    "badge_green_border": "#36533F",
    "badge_amber_text": "#CEAA67",
    "badge_amber_background": "#403521",
    "badge_amber_border": "#5B4A2C",
    "badge_waiting_text": "#CA9470",
    "badge_waiting_background": "#402F27",
    "badge_waiting_border": "#5B4033",
}


def app_stylesheet(night_mode: bool = False) -> str:
    palette = DARK_PALETTE if night_mode else LIGHT_PALETTE
    return """
QMainWindow, QWidget#appRoot { background: %(app)s; color: %(text)s; }
QFrame#navigationPane, QFrame#contentsPane, QFrame#statusPane {
    background: %(pane)s;
    border: 0;
}
QFrame#contentsPane { border-left: 1px solid %(border)s; }
QFrame#statusPane { border-left: 1px solid %(border)s; }
QFrame#readerPane { background: %(reader)s; border-left: 1px solid %(border)s; }
QLabel#eyebrow {
    color: %(eyebrow)s; font-size: 10px; font-weight: 650; letter-spacing: 1.4px;
    padding: 0;
}
QLabel#paneTitle { color: %(title)s; font-size: 15px; font-weight: 650; }
QLabel#changeLegend {
    color: %(muted)s; font-size: 9px; font-weight: 650; letter-spacing: .5px;
    padding: 7px 3px 1px; border-top: 1px solid %(border)s;
}
QLabel#repositoryName { color: %(repository)s; font-size: 19px; font-weight: 700; }
QLabel#muted, QLabel#metadataValue { color: %(muted)s; font-size: 12px; }
QLabel#metadataLabel { color: %(metadata)s; font-size: 10px; font-weight: 650; letter-spacing: 1px; }
QLabel#readOnlyBadge {
    color: %(badge_blue_text)s; background: %(badge_blue_background)s; border: 1px solid %(badge_blue_border)s;
    border-radius: 8px; padding: 3px 8px; font-size: 10px; font-weight: 650;
}
QLabel#liveBadge {
    border-radius: 8px; padding: 3px 8px; font-size: 10px; font-weight: 650;
}
QLabel#liveBadge[state="watching"] {
    color: %(badge_green_text)s; background: %(badge_green_background)s; border: 1px solid %(badge_green_border)s;
}
QLabel#liveBadge[state="updated"] {
    color: %(badge_amber_text)s; background: %(badge_amber_background)s; border: 1px solid %(badge_amber_border)s;
}
QLabel#liveBadge[state="waiting"] {
    color: %(badge_waiting_text)s; background: %(badge_waiting_background)s; border: 1px solid %(badge_waiting_border)s;
}
QLabel#liveBadge[state="snapshot"] {
    color: %(badge_blue_text)s; background: %(badge_blue_background)s; border: 1px solid %(badge_blue_border)s;
}
QComboBox#branchSelector, QComboBox#diffSelector, QComboBox#settingsCombo, QSpinBox#settingsSpin {
    color: %(text)s; background: %(input)s; border: 1px solid %(input_border)s;
    border-radius: 6px; padding: 6px 9px; font-size: 12px;
}
QComboBox#branchSelector:focus, QComboBox#diffSelector:focus, QComboBox#settingsCombo:focus,
QSpinBox#settingsSpin:focus {
    border-color: %(input_focus)s;
}
QComboBox#branchSelector::drop-down, QComboBox#diffSelector::drop-down,
QComboBox#settingsCombo::drop-down { border: 0; width: 22px; }
QComboBox QAbstractItemView {
    color: %(text)s; background: %(input)s; border: 1px solid %(input_border)s;
    selection-background-color: %(selection)s; selection-color: %(selection_text)s;
}
QLineEdit#searchField {
    color: %(text)s; background: %(input)s; border: 1px solid %(input_border)s;
    border-radius: 7px; padding: 7px 9px; font-size: 12px;
    selection-background-color: %(selection)s; selection-color: %(selection_text)s;
}
QLineEdit#searchField:focus { border-color: %(input_focus)s; }
QListWidget#compactList, QListWidget#commitList {
    background: %(compact)s; border: 0; border-radius: 6px; padding: 3px;
    color: %(compact_text)s; font-size: 11px;
}
QListWidget#compactList::item, QListWidget#commitList::item {
    min-height: 24px; padding: 4px 6px; border-radius: 4px;
}
QListWidget#commitList::item { min-height: 40px; }
QTreeWidget, QListWidget {
    background: transparent; border: 0; outline: 0; color: %(navigation_text)s; font-size: 13px;
    selection-background-color: %(selection)s; selection-color: %(selection_text)s;
}
QTreeWidget::item, QListWidget::item { min-height: 28px; border-radius: 5px; padding: 2px 5px; }
QTreeWidget::item:selected, QListWidget::item:selected { border-left: 2px solid %(input_focus)s; }
QListWidget::item { margin: 1px 0; }
QWidget#contentsSwitcher {
    background: %(compact)s; border: 1px solid %(border)s; border-radius: 6px;
}
QPushButton#contentsModeButton {
    color: %(muted)s; background: transparent; border: 0; border-radius: 4px;
    padding: 5px 8px; font-size: 11px; font-weight: 600;
}
QPushButton#contentsModeButton:checked {
    color: %(button_checked)s; background: %(button_background)s;
}
QPushButton#contentsModeButton:disabled { color: %(button_disabled)s; }
QListWidget#outlineList::item { padding-left: 7px; padding-right: 7px; }
QMenu#outlineMenu {
    color: %(text)s; background: %(input)s; border: 1px solid %(input_border)s;
    padding: 5px; font-size: 12px;
}
QMenu#outlineMenu::item { padding: 6px 22px 6px 10px; border-radius: 4px; }
QMenu#outlineMenu::item:selected {
    color: %(selection_text)s; background: %(selection)s;
}
QPushButton#modeButton, QPushButton#utilityButton {
    color: %(button)s; background: transparent; border: 0; border-radius: 5px;
    padding: 5px 10px; font-size: 12px; font-weight: 550;
}
QPushButton#modeButton:checked, QPushButton#utilityButton:checked {
    color: %(button_checked)s; background: %(button_background)s;
}
QPushButton#modeButton:disabled, QPushButton#utilityButton:disabled { color: %(button_disabled)s; }
QPushButton#navigationButton {
    color: %(button)s; background: transparent; border: 0; border-radius: 5px;
    padding: 0; font-size: 22px; font-weight: 500;
}
QPushButton#navigationButton:hover { background: %(button_background)s; color: %(button_checked)s; }
QPushButton#navigationButton:disabled { color: %(button_disabled)s; }
QFrame#changeNavigator {
    background: %(badge_amber_background)s; border: 1px solid %(badge_amber_border)s;
    border-radius: 6px;
}
QLabel#changePosition {
    color: %(badge_amber_text)s; font-size: 9px; font-weight: 700; letter-spacing: .5px;
    padding: 0 3px;
}
QPushButton#changeNavigationButton {
    color: %(badge_amber_text)s; background: transparent; border: 0; border-radius: 4px;
    padding: 0; font-size: 14px; font-weight: 650;
}
QPushButton#changeNavigationButton:hover {
    color: %(button_checked)s; background: %(button_background)s;
}
QPushButton#changeNavigationButton:disabled { color: %(button_disabled)s; }
QTextBrowser { color: %(text)s; background: %(reader)s; border: 0; }
QSplitter::handle { background: transparent; width: 1px; }
QScrollBar:vertical { background: transparent; width: 10px; margin: 2px; }
QScrollBar::handle:vertical { background: %(scrollbar)s; border-radius: 4px; min-height: 32px; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }
QToolTip { color: %(text)s; background: %(input)s; border: 1px solid %(input_border)s; }
QDialog#settingsDialog { color: %(text)s; background: %(app)s; }
QDialog#helpDialog { color: %(text)s; background: %(reader)s; }
QFrame#helpHeader {
    color: %(text)s; background: %(pane)s; border-bottom: 1px solid %(border)s;
}
QFrame#helpBody { background: %(reader)s; }
QLabel#helpEyebrow {
    color: %(eyebrow)s; font-size: 9px; font-weight: 700; letter-spacing: 1.4px;
}
QLabel#helpTitle { color: %(title)s; font-size: 23px; font-weight: 650; }
QLabel#helpSubtitle { color: %(muted)s; font-size: 12px; }
QListWidget#helpTopicList {
    color: %(navigation_text)s; background: %(pane)s; border-right: 1px solid %(border)s;
    border-radius: 0; padding: 15px 10px; font-size: 12px;
}
QListWidget#helpTopicList::item { min-height: 30px; padding: 5px 9px; margin: 1px 0; }
QListWidget#helpTopicList::item:selected {
    color: %(selection_text)s; background: %(selection)s; border-left: 2px solid %(input_focus)s;
}
QTextBrowser#helpContent { color: %(text)s; background: %(reader)s; border: 0; }
QLabel#settingsTitle { color: %(title)s; font-size: 20px; font-weight: 650; }
QFrame#settingsSection {
    color: %(text)s; background: %(pane)s; border: 1px solid %(border)s; border-radius: 8px;
}
QLabel#settingsSectionTitle {
    color: %(eyebrow)s; font-size: 10px; font-weight: 650; letter-spacing: 1px;
}
QLabel#settingsDescription { color: %(muted)s; font-size: 11px; padding: 0 0 3px 24px; }
QLabel#settingsLabel, QRadioButton#settingsRadio, QCheckBox#settingsCheck {
    color: %(text)s; font-size: 13px;
}
QPushButton#settingsDialogButton {
    color: %(text)s; background: %(input)s; border: 1px solid %(input_border)s;
    border-radius: 6px; padding: 6px 16px; min-width: 72px;
}
QPushButton#settingsDialogButton:default {
    color: %(selection_text)s; background: %(selection)s; border-color: %(input_focus)s;
}
""" % palette


APP_STYLESHEET = app_stylesheet()
