from __future__ import annotations

import html
import base64
import mimetypes
import hashlib
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Callable
from urllib.parse import unquote

from PySide6.QtCore import QPoint, QSettings, QSize, Qt, QTimer, QUrl
from PySide6.QtGui import (
    QAction,
    QColor,
    QCloseEvent,
    QDesktopServices,
    QImage,
    QKeySequence,
    QResizeEvent,
    QShortcut,
    QTextCursor,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QButtonGroup,
    QComboBox,
    QFrame,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMenu,
    QMessageBox,
    QPushButton,
    QScrollBar,
    QSizePolicy,
    QSplitter,
    QStackedWidget,
    QTextBrowser,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from .diff import DiffRenderer
from .change_awareness import ChangeState, ChangeTracker
from .git import GitClient, GitError, GitMetadataWatcher
from .help_window import HelpDialog
from .image_viewer import ImageViewerDialog
from .live_updates import adjacent_change_index, changed_block_indices
from .markdown import MarkdownRenderer
from .navigation import (
    NavigationEntry,
    NavigationHistory,
    ReadingModeHandoff,
    normalized_scroll,
    restored_scroll,
    scroll_storage_mode,
)
from .outline import OutlineEntry, document_outline
from .preferences import (
    DEFAULT_FONT_SIZE,
    READING_WIDTHS,
    SettingsDialog,
    SettingsValues,
    clamp_font_size,
    night_mode_for,
    reading_page_width,
    stored_appearance_mode,
    system_uses_dark_mode,
)
from .repository import VISIBLE_SUFFIXES, Repository
from .repository_view import RepositoryView
from .search import SearchIndex
from .theme import DARK_PALETTE, LIGHT_PALETTE, app_stylesheet
from .watcher import RepositoryWatcher
from . import __version__


PATH_ROLE = Qt.ItemDataRole.UserRole
OUTLINE_ROLE = Qt.ItemDataRole.UserRole + 1
BASE_TEXT_ROLE = Qt.ItemDataRole.UserRole + 2
BASE_TOOLTIP_ROLE = Qt.ItemDataRole.UserRole + 3


class MainWindow(QMainWindow):
    def __init__(self, repository: RepositoryView) -> None:
        super().__init__()
        self.repository = repository
        self.settings = QSettings("Elvandar", "Elvandar Viewer")
        application = QApplication.instance()
        self.appearance_mode = stored_appearance_mode(self.settings)
        self.night_mode = night_mode_for(
            self.appearance_mode,
            system_uses_dark_mode(application) if application is not None else False,
        )
        self.remember_reading_mode = self.settings.value(
            "reading/remember_mode", True, type=bool
        )
        stored_reading_mode = self.settings.value("appearance/reading_mode", False, type=bool)
        self.reading_mode = stored_reading_mode if self.remember_reading_mode else False
        stored_reading_width = self.settings.value("reading/page_width", 980, type=int)
        reading_width_version = self.settings.value("reading/page_width_version", 1, type=int)
        if reading_width_version < 2:
            self.reading_width = {840: 1120, 980: 1400, 1120: 1680}.get(
                stored_reading_width, 1400
            )
            self.settings.setValue("reading/page_width", self.reading_width)
            self.settings.setValue("reading/page_width_version", 2)
        else:
            self.reading_width = stored_reading_width
        if self.reading_width not in READING_WIDTHS:
            self.reading_width = 1400
        self.highlight_live_changes = self.settings.value(
            "live_updates/highlight_changes", True, type=bool
        )
        self.reading_font_size = clamp_font_size(
            self.settings.value("reading/font_size", DEFAULT_FONT_SIZE, type=int)
        )
        if application is not None:
            application.setStyleSheet(app_stylesheet(self.night_mode))
            application.styleHints().colorSchemeChanged.connect(self._system_color_scheme_changed)
        self.renderer = MarkdownRenderer(self.night_mode, self.reading_font_size)
        self.diff_renderer = DiffRenderer(self.renderer)
        self.search_index = SearchIndex()
        self.current_document: Path | None = None
        self.current_image_path: Path | None = None
        self.current_image_data = b""
        self.image_windows: list[ImageViewerDialog] = []
        self.help_dialog: HelpDialog | None = None
        self.current_source = ""
        self.current_outline: list[OutlineEntry] = []
        self._outline_document_positions: list[int] = []
        self._outline_sync_pending = False
        self.contents_mode = "folder"
        self._folder_contents_title = "Repository"
        self.current_mode = "Rendered"
        self._reading_mode_handoff: tuple[Path, str | None, ReadingModeHandoff] | None = None
        self._pending_scroll_restore: tuple[
            QScrollBar,
            Callable[[int, int], None],
            Callable[[int], None],
            Callable[[], None],
            Callable[[], None],
        ] | None = None
        self.active_query = ""
        self._highlighted_blocks: list[int] = []
        self._highlight_frame = 0
        self._search_selections: list[QTextEdit.ExtraSelection] = []
        self._change_selections: list[QTextEdit.ExtraSelection] = []
        self._change_focus_selections: list[QTextEdit.ExtraSelection] = []
        self._live_change_blocks: list[int] = []
        self._live_change_index: int | None = None
        self._live_change_document: Path | None = None
        self._splitter_state_before_reading = None
        self.navigation_history = NavigationHistory()
        self._navigating_history = False
        self._diff_comparison_context: tuple[Path, str | None] | None = None
        self.settings_prefix = self._settings_prefix_for(repository.root)
        self.change_tracker = self._load_change_tracker()

        self.setWindowTitle(f"Elvandar Viewer — {repository.root.name}")
        self.setMinimumSize(1050, 680)
        self.resize(1480, 900)
        self.setUnifiedTitleAndToolBarOnMac(True)
        self._build_ui()
        self._populate_tree()
        self._highlight_timer = QTimer(self)
        self._highlight_timer.setInterval(90)
        self._highlight_timer.timeout.connect(self._fade_change_highlight)
        self._attach_watchers()
        self._refresh_git_sidebar()
        self._rebuild_search_index()
        self.branch_selector.currentIndexChanged.connect(self._view_revision_changed)
        self._setup_shortcuts()
        self._build_menus()
        self._restore_window_state()
        self._set_reading_mode(self.reading_mode, persist=False)
        self._update_navigation_controls()

    @staticmethod
    def _settings_prefix_for(root: Path) -> str:
        repository_key = hashlib.sha1(str(root.resolve(strict=False)).encode()).hexdigest()[:12]
        return f"repositories/{repository_key}"

    def _change_tracking_key(self) -> str:
        return f"{self.settings_prefix}/changes/seen_versions"

    def _load_change_tracker(self) -> ChangeTracker:
        stored = self.settings.value(self._change_tracking_key(), "", type=str)
        return ChangeTracker.from_json(stored)

    def _persist_change_tracker(self) -> None:
        self.settings.setValue(self._change_tracking_key(), self.change_tracker.to_json())

    def _working_file_signature(self, relative: PurePosixPath) -> str | None:
        path = self.repository.root / Path(relative.as_posix())
        try:
            stat = path.stat()
        except OSError:
            return None
        if not path.is_file():
            return None
        return f"{stat.st_mtime_ns}:{stat.st_size}"

    def _refresh_change_awareness(self) -> None:
        if not self.repository.is_working_tree:
            self.change_tracker.states = {}
            self._refresh_change_decorations()
            return
        try:
            changed_paths = self.repository.changed_paths()
        except GitError:
            changed_paths = set()
        visible_paths = {
            path
            for path in changed_paths
            if path.suffix.casefold() in VISIBLE_SUFFIXES
        }
        before = self.change_tracker.to_json()
        self.change_tracker.refresh(visible_paths, self._working_file_signature)
        if self.change_tracker.to_json() != before:
            self._persist_change_tracker()
        self._refresh_change_decorations()

    def _mark_version_viewed(self, path: Path) -> None:
        if not self.repository.is_working_tree:
            return
        relative = PurePosixPath(self.repository.relative(path).as_posix())
        if self.change_tracker.mark_viewed(
            relative, self._working_file_signature(relative)
        ):
            self._persist_change_tracker()
        self._refresh_change_decorations()

    def _attach_watchers(self) -> None:
        self.watcher = RepositoryWatcher(self.repository.working_tree, self)
        self.watcher.document_changed.connect(self._asset_changed)
        self.watcher.document_availability_changed.connect(
            self._document_availability_changed
        )
        self.watcher.structure_changed.connect(self._repository_structure_changed)
        self.watcher.repository_touched.connect(self._refresh_git_sidebar)
        self.watcher.files_changed.connect(self._search_files_changed)
        self.git_watcher = GitMetadataWatcher(self.repository.git, self)
        self.git_watcher.changed.connect(self._git_metadata_changed)

    def _detach_watchers(self) -> None:
        self.watcher.set_document(None)
        self.watcher.blockSignals(True)
        self.git_watcher.blockSignals(True)
        self.watcher.deleteLater()
        self.git_watcher.deleteLater()

    def _build_ui(self) -> None:
        root = QWidget(objectName="appRoot")
        layout = QVBoxLayout(root)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.folder_tree = self._navigation_pane(self.splitter)
        self.document_list = self._contents_pane(self.splitter)
        self.reader = self._reader_pane(self.splitter)
        self._status_pane(self.splitter)
        self.splitter.setSizes([205, 245, 760, 245])
        self.splitter.setStretchFactor(2, 1)
        layout.addWidget(self.splitter)
        self.setCentralWidget(root)

    @staticmethod
    def _header(eyebrow: str, title: str) -> tuple[QVBoxLayout, QLabel]:
        layout = QVBoxLayout()
        layout.setSpacing(4)
        eyebrow_label = QLabel(eyebrow.upper(), objectName="eyebrow")
        title_label = QLabel(title, objectName="paneTitle")
        layout.addWidget(eyebrow_label)
        layout.addWidget(title_label)
        return layout, title_label

    def _navigation_pane(self, parent: QWidget) -> QTreeWidget:
        pane = QFrame(parent, objectName="navigationPane")
        layout = QVBoxLayout(pane)
        layout.setContentsMargins(16, 20, 12, 14)
        layout.setSpacing(14)

        eyebrow = QLabel("LIBRARY", objectName="eyebrow")
        self.repository_name = QLabel(self.repository.root.name, objectName="repositoryName")
        self.repository_name.setWordWrap(True)
        layout.addWidget(eyebrow)
        layout.addWidget(self.repository_name)

        self.search_field = QLineEdit(objectName="searchField")
        self.search_field.setPlaceholderText("Search Elvandar")
        self.search_field.setClearButtonEnabled(True)
        self.search_field.setAccessibleName("Search all documents")
        self.search_field.textChanged.connect(self._search_changed)
        self.search_field.returnPressed.connect(self._open_first_search_result)
        layout.addWidget(self.search_field)

        tree = QTreeWidget()
        tree.setHeaderHidden(True)
        tree.setIndentation(14)
        tree.setAnimated(True)
        tree.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        tree.itemSelectionChanged.connect(self._folder_selected)
        layout.addWidget(tree, 1)
        return tree

    def _contents_pane(self, parent: QWidget) -> QListWidget:
        pane = QFrame(parent, objectName="contentsPane")
        layout = QVBoxLayout(pane)
        layout.setContentsMargins(14, 20, 12, 14)
        layout.setSpacing(10)
        header, self.contents_title = self._header("CONTENTS", "Repository")
        layout.addLayout(header)

        switcher = QWidget(objectName="contentsSwitcher")
        switcher_layout = QHBoxLayout(switcher)
        switcher_layout.setContentsMargins(0, 2, 0, 2)
        switcher_layout.setSpacing(2)
        self.contents_button_group = QButtonGroup(self)
        self.contents_button_group.setExclusive(True)
        self.folder_contents_button = QPushButton("Folder", objectName="contentsModeButton")
        self.folder_contents_button.setCheckable(True)
        self.folder_contents_button.setChecked(True)
        self.folder_contents_button.clicked.connect(
            lambda _checked=False: self._set_contents_mode("folder")
        )
        self.contents_button_group.addButton(self.folder_contents_button)
        switcher_layout.addWidget(self.folder_contents_button)
        self.outline_contents_button = QPushButton("Page", objectName="contentsModeButton")
        self.outline_contents_button.setCheckable(True)
        self.outline_contents_button.setEnabled(False)
        self.outline_contents_button.clicked.connect(
            lambda _checked=False: self._set_contents_mode("outline")
        )
        self.contents_button_group.addButton(self.outline_contents_button)
        switcher_layout.addWidget(self.outline_contents_button)
        layout.addWidget(switcher)

        listing = QListWidget()
        listing.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        listing.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        listing.itemActivated.connect(self._content_activated)
        listing.itemSelectionChanged.connect(self._content_selected)

        self.outline_list = QListWidget(objectName="outlineList")
        self.outline_list.setAccessibleName("Document outline")
        self.outline_list.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.outline_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.outline_list.setTextElideMode(Qt.TextElideMode.ElideRight)
        self.outline_list.itemActivated.connect(self._outline_item_activated)
        self.outline_list.itemClicked.connect(self._outline_item_activated)

        self.contents_stack = QStackedWidget()
        self.contents_stack.addWidget(listing)
        self.contents_stack.addWidget(self.outline_list)
        layout.addWidget(self.contents_stack, 1)
        self.change_legend = QLabel(objectName="changeLegend")
        self.change_legend.setTextFormat(Qt.TextFormat.RichText)
        self.change_legend.setToolTip(
            "Solid coral: changed and not yet opened. Hollow blue: this changed version was viewed."
        )
        self.change_legend.setVisible(False)
        layout.addWidget(self.change_legend)
        return listing

    def _reader_pane(self, parent: QWidget) -> QTextBrowser:
        pane = QFrame(parent, objectName="readerPane")
        layout = QVBoxLayout(pane)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        toolbar = QWidget()
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(20, 10, 20, 10)
        toolbar_layout.setSpacing(3)

        self.back_button = QPushButton("‹", objectName="navigationButton")
        self.back_button.setAccessibleName("Back")
        self.back_button.setToolTip("Back (⌘[)")
        self.back_button.setFixedSize(28, 26)
        self.back_button.clicked.connect(self._go_back)
        toolbar_layout.addWidget(self.back_button)

        self.forward_button = QPushButton("›", objectName="navigationButton")
        self.forward_button.setAccessibleName("Forward")
        self.forward_button.setToolTip("Forward (⌘])")
        self.forward_button.setFixedSize(28, 26)
        self.forward_button.clicked.connect(self._go_forward)
        toolbar_layout.addWidget(self.forward_button)
        toolbar_layout.addSpacing(5)

        self.reader_title = QLabel("Choose a document", objectName="muted")
        self.reader_title.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        toolbar_layout.addWidget(self.reader_title)

        self.change_navigator = QFrame(objectName="changeNavigator")
        change_layout = QHBoxLayout(self.change_navigator)
        change_layout.setContentsMargins(7, 1, 2, 1)
        change_layout.setSpacing(1)
        self.change_position = QLabel("CHANGES", objectName="changePosition")
        change_layout.addWidget(self.change_position)
        self.previous_change_button = QPushButton("↑", objectName="changeNavigationButton")
        self.previous_change_button.setAccessibleName("Previous Change")
        self.previous_change_button.setToolTip("Previous changed paragraph (⌘⌥↑)")
        self.previous_change_button.setFixedSize(23, 23)
        self.previous_change_button.clicked.connect(self._go_to_previous_change)
        change_layout.addWidget(self.previous_change_button)
        self.next_change_button = QPushButton("↓", objectName="changeNavigationButton")
        self.next_change_button.setAccessibleName("Next Change")
        self.next_change_button.setToolTip("Next changed paragraph (⌘⌥↓)")
        self.next_change_button.setFixedSize(23, 23)
        self.next_change_button.clicked.connect(self._go_to_next_change)
        change_layout.addWidget(self.next_change_button)
        self.change_navigator.setVisible(False)
        toolbar_layout.addWidget(self.change_navigator)

        self.mode_buttons: dict[str, QPushButton] = {}
        modes = QButtonGroup(self)
        modes.setExclusive(True)
        for text, checked, enabled in (
            ("Rendered", True, True),
            ("Raw", False, True),
            ("Diff", False, False),
        ):
            button = QPushButton(text, objectName="modeButton")
            button.setCheckable(True)
            button.setChecked(checked)
            button.setEnabled(enabled)
            button.clicked.connect(lambda _checked, mode=text: self._show_mode(mode))
            modes.addButton(button)
            self.mode_buttons[text] = button
            toolbar_layout.addWidget(button)

        self.diff_selector = QComboBox(objectName="diffSelector")
        self.diff_selector.setAccessibleName("Diff comparison")
        self.diff_selector.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToContents)
        self.diff_selector.setMaximumWidth(180)
        self.diff_selector.setVisible(False)
        self.diff_selector.currentIndexChanged.connect(self._diff_comparison_changed)
        toolbar_layout.addWidget(self.diff_selector)

        self.outline_button = QPushButton("Outline", objectName="utilityButton")
        self.outline_button.setEnabled(False)
        self.outline_button.setToolTip("Jump to a heading or scene (⌘⇧O)")
        self.outline_button.clicked.connect(self._show_outline_menu)
        toolbar_layout.addWidget(self.outline_button)

        self.reading_button = QPushButton("Reading", objectName="utilityButton")
        self.reading_button.setCheckable(True)
        self.reading_button.setChecked(self.reading_mode)
        self.reading_button.setToolTip("Hide the sidebars (⌘⇧R or Esc)")
        self.reading_button.clicked.connect(self._set_reading_mode)
        toolbar_layout.addWidget(self.reading_button)
        layout.addWidget(toolbar)

        reader = QTextBrowser()
        reader.setOpenLinks(False)
        reader.setOpenExternalLinks(False)
        reader.setHtml(self._welcome_document())
        reader.anchorClicked.connect(self._open_link)
        reader.verticalScrollBar().valueChanged.connect(self._reader_scroll_changed)
        self.diff_reader = QTextBrowser()
        self.diff_reader.setOpenLinks(False)
        self.diff_reader.setOpenExternalLinks(False)
        self.diff_reader.anchorClicked.connect(self._open_link)
        self.image_page = QTextBrowser()
        self.image_page.setOpenLinks(False)
        self.image_page.anchorClicked.connect(self._open_link)
        self.reader_stack = QStackedWidget()
        self.reader_stack.addWidget(reader)
        self.reader_stack.addWidget(self.diff_reader)
        self.reader_stack.addWidget(self.image_page)
        self.reader_layout = layout
        layout.addWidget(self.reader_stack, 1)
        return reader

    def _status_pane(self, parent: QWidget) -> None:
        pane = QFrame(parent, objectName="statusPane")
        layout = QVBoxLayout(pane)
        layout.setContentsMargins(18, 20, 18, 16)
        layout.setSpacing(14)
        header, _ = self._header("REPOSITORY", "Git activity")
        layout.addLayout(header)

        layout.addWidget(QLabel("VIEWING", objectName="metadataLabel"))
        self.branch_selector = QComboBox(objectName="branchSelector")
        layout.addWidget(self.branch_selector)
        badges = QHBoxLayout()
        badges.setSpacing(6)
        badge = QLabel("READ ONLY", objectName="readOnlyBadge")
        badge.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.live_badge = QLabel("● WATCHING", objectName="liveBadge")
        self.live_badge.setProperty("state", "watching")
        self.live_badge.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        badges.addWidget(badge)
        badges.addWidget(self.live_badge)
        badges.addStretch(1)
        layout.addLayout(badges)

        layout.addWidget(QLabel("WORKTREES", objectName="metadataLabel"))
        self.worktree_list = QListWidget(objectName="compactList")
        self.worktree_list.setMaximumHeight(92)
        self.worktree_list.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.worktree_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.worktree_list.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.worktree_list.setCursor(Qt.CursorShape.PointingHandCursor)
        self.worktree_list.itemClicked.connect(self._worktree_selected)
        layout.addWidget(self.worktree_list)

        self.changes_label = QLabel("WORKING CHANGES", objectName="metadataLabel")
        layout.addWidget(self.changes_label)
        self.changes_list = QListWidget(objectName="compactList")
        self.changes_list.setMaximumHeight(170)
        self.changes_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.changes_list.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.changes_list.itemActivated.connect(self._changed_file_activated)
        layout.addWidget(self.changes_list)

        layout.addWidget(QLabel("RECENT COMMITS", objectName="metadataLabel"))
        self.commits_list = QListWidget(objectName="commitList")
        self.commits_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.commits_list.setTextElideMode(Qt.TextElideMode.ElideRight)
        layout.addWidget(self.commits_list, 1)

    def _populate_tree(self, selected_path: Path | None = None) -> None:
        self.folder_tree.blockSignals(True)
        self.folder_tree.clear()
        root_item = QTreeWidgetItem(["All documents"])
        root_item.setData(0, PATH_ROLE, str(self.repository.root))
        root_item.setData(0, BASE_TEXT_ROLE, "All documents")
        root_item.setData(0, BASE_TOOLTIP_ROLE, "")
        self.folder_tree.addTopLevelItem(root_item)
        for folder in self.repository.directories():
            item = QTreeWidgetItem([folder.name])
            item.setData(0, PATH_ROLE, str(folder))
            item.setData(0, BASE_TEXT_ROLE, folder.name)
            item.setData(0, BASE_TOOLTIP_ROLE, str(self.repository.relative(folder)))
            root_item.addChild(item)
            self._add_directory_children(item, folder)
        root_item.setExpanded(True)
        selected_item = self._find_tree_item(selected_path) if selected_path else None
        self.folder_tree.setCurrentItem(selected_item or root_item)
        self.folder_tree.blockSignals(False)
        self._folder_selected()

    def _find_tree_item(self, path: Path | None) -> QTreeWidgetItem | None:
        if path is None:
            return None
        root = self.folder_tree.topLevelItem(0)
        pending = [root]
        while pending:
            item = pending.pop()
            if item.data(0, PATH_ROLE) == str(path):
                return item
            pending.extend(item.child(index) for index in range(item.childCount()))
        return None

    def _add_directory_children(self, parent_item: QTreeWidgetItem, folder: Path) -> None:
        for child in self.repository.directories(folder):
            item = QTreeWidgetItem([child.name])
            item.setData(0, PATH_ROLE, str(child))
            item.setData(0, BASE_TEXT_ROLE, child.name)
            item.setData(0, BASE_TOOLTIP_ROLE, str(self.repository.relative(child)))
            parent_item.addChild(item)
            self._add_directory_children(item, child)

    def _change_colors(self) -> tuple[QColor, QColor, QColor]:
        palette = DARK_PALETTE if self.night_mode else LIGHT_PALETTE
        unseen = QColor("#F08A72" if self.night_mode else "#B94F3D")
        viewed = QColor("#8BAAD2" if self.night_mode else "#4F709B")
        standard = QColor(palette["navigation_text"])
        return unseen, viewed, standard

    def _decorate_tree_item(self, item: QTreeWidgetItem) -> None:
        path_text = item.data(0, PATH_ROLE)
        if not path_text:
            return
        path = Path(str(path_text))
        relative = PurePosixPath(self.repository.relative(path).as_posix())
        state = self.change_tracker.state_for(relative, directory=True)
        base = str(item.data(0, BASE_TEXT_ROLE) or item.text(0))
        base_tooltip = str(item.data(0, BASE_TOOLTIP_ROLE) or "")
        unseen_color, viewed_color, standard_color = self._change_colors()
        font = item.font(0)
        font.setBold(state == ChangeState.UNSEEN)
        item.setFont(0, font)
        if state is None:
            item.setText(0, base)
            item.setForeground(0, standard_color)
            item.setToolTip(0, base_tooltip)
            return

        marker = "●" if state == ChangeState.UNSEEN else "○"
        item.setText(0, f"{marker}  {base}")
        item.setForeground(0, unseen_color if state == ChangeState.UNSEEN else viewed_color)
        unseen_count, viewed_count = self.change_tracker.counts_for(relative)
        status = (
            f"{unseen_count} unseen, {viewed_count} viewed changed file"
            f"{'s' if unseen_count + viewed_count != 1 else ''}"
        )
        item.setToolTip(0, f"{base_tooltip}\n{status}".strip())

    def _decorate_list_item(self, item: QListWidgetItem) -> None:
        path_text = item.data(PATH_ROLE)
        if not path_text:
            return
        path = Path(str(path_text))
        relative = PurePosixPath(self.repository.relative(path).as_posix())
        is_directory = self.repository.is_directory(path)
        state = self.change_tracker.state_for(relative, directory=is_directory)
        base = str(item.data(BASE_TEXT_ROLE) or item.text())
        base_tooltip = str(item.data(BASE_TOOLTIP_ROLE) or "")
        unseen_color, viewed_color, standard_color = self._change_colors()
        font = item.font()
        font.setBold(state == ChangeState.UNSEEN)
        item.setFont(font)
        if state is None:
            item.setText(base)
            item.setForeground(standard_color)
            item.setToolTip(base_tooltip)
            return

        marker = "●" if state == ChangeState.UNSEEN else "○"
        item.setText(f"{marker}  {base.lstrip()}")
        item.setForeground(unseen_color if state == ChangeState.UNSEEN else viewed_color)
        if is_directory:
            unseen_count, viewed_count = self.change_tracker.counts_for(relative)
            status = f"{unseen_count} unseen, {viewed_count} viewed changed file"
            if unseen_count + viewed_count != 1:
                status += "s"
        else:
            status = (
                "Unseen change — open this page to mark the current version viewed"
                if state == ChangeState.UNSEEN
                else "Changed version viewed"
            )
        item.setToolTip(f"{base_tooltip}\n{status}".strip())

    def _refresh_change_decorations(self) -> None:
        if not hasattr(self, "folder_tree"):
            return
        root = self.folder_tree.topLevelItem(0)
        if root is not None:
            pending = [root]
            while pending:
                item = pending.pop()
                self._decorate_tree_item(item)
                pending.extend(
                    item.child(index) for index in range(item.childCount())
                )
        for index in range(self.document_list.count()):
            self._decorate_list_item(self.document_list.item(index))

        unseen = sum(
            state == ChangeState.UNSEEN for state in self.change_tracker.states.values()
        )
        viewed = sum(
            state == ChangeState.VIEWED for state in self.change_tracker.states.values()
        )
        unseen_color, viewed_color, _standard_color = self._change_colors()
        self.change_legend.setText(
            f'<span style="color:{unseen_color.name()}">●</span> {unseen} UNSEEN'
            f'&nbsp;&nbsp;&nbsp;<span style="color:{viewed_color.name()}">○</span> {viewed} VIEWED'
        )
        self.change_legend.setVisible(bool(unseen or viewed))

    def _folder_selected(self) -> None:
        if self.active_query:
            self._show_search_results()
            return
        selected = self.folder_tree.selectedItems()
        if not selected:
            return
        folder = Path(selected[0].data(0, PATH_ROLE))
        self._show_folder(folder)

    def _show_folder(self, folder: Path) -> None:
        self._folder_contents_title = (
            folder.name if folder != self.repository.root else "Repository"
        )
        if self.contents_mode == "folder":
            self.contents_title.setText(self._folder_contents_title)
        self.document_list.clear()
        for path in self.repository.contents(folder):
            if self.repository.is_directory(path):
                prefix = "▸  "
            elif self.repository.is_image(path):
                prefix = "▧  "
            else:
                prefix = "   "
            item = QListWidgetItem(prefix + self._display_name(path))
            item.setData(PATH_ROLE, str(path))
            item.setData(BASE_TEXT_ROLE, prefix + self._display_name(path))
            tooltip = str(self.repository.relative(path))
            item.setData(BASE_TOOLTIP_ROLE, tooltip)
            item.setToolTip(tooltip)
            self.document_list.addItem(item)
        self._refresh_change_decorations()

    def _reveal_document_in_navigation(self, path: Path) -> None:
        """Reveal an open page in both left sidebars without reopening it."""

        folder = path.parent
        folder_item = self._find_tree_item(folder)
        if folder_item is None:
            return

        self.folder_tree.blockSignals(True)
        self.folder_tree.setCurrentItem(folder_item)
        ancestor: QTreeWidgetItem | None = folder_item
        while ancestor is not None:
            ancestor.setExpanded(True)
            ancestor = ancestor.parent()
        self.folder_tree.scrollToItem(folder_item)
        self.folder_tree.blockSignals(False)

        self._show_folder(folder)
        self._set_contents_mode("folder")
        for index in range(self.document_list.count()):
            item = self.document_list.item(index)
            if item.data(PATH_ROLE) != str(path):
                continue
            self.document_list.blockSignals(True)
            self.document_list.setCurrentItem(item)
            self.document_list.scrollToItem(item)
            self.document_list.blockSignals(False)
            break

    def _set_contents_mode(self, mode: str) -> None:
        if mode == "outline" and self.current_document is None:
            mode = "folder"
        self.contents_mode = mode
        showing_outline = mode == "outline"
        self.contents_stack.setCurrentWidget(
            self.outline_list if showing_outline else self.document_list
        )
        self.outline_contents_button.setChecked(showing_outline)
        self.folder_contents_button.setChecked(not showing_outline)
        self.contents_title.setText(
            "On this page" if showing_outline else self._folder_contents_title
        )

    def _populate_outline_list(self) -> None:
        self.outline_list.blockSignals(True)
        self.outline_list.clear()
        heading_levels = [
            entry.level for entry in self.current_outline if entry.kind == "heading"
        ]
        base_level = min(heading_levels, default=1)
        scene_color = QColor("#D0AA65" if self.night_mode else "#9A702F")

        for index, entry in enumerate(self.current_outline):
            if entry.kind == "scene":
                item = QListWidgetItem(f"—  {entry.title}  —")
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item.setForeground(scene_color)
                font = item.font()
                font.setItalic(True)
                item.setFont(font)
                item.setToolTip(f"Jump to scene break {entry.scene_number}")
                item.setSizeHint(QSize(0, 34))
            else:
                indentation = "\u2003" * max(0, entry.level - base_level)
                item = QListWidgetItem(f"{indentation}{entry.title}")
                font = item.font()
                font.setBold(entry.level == base_level)
                item.setFont(font)
                item.setToolTip(f"Heading level {entry.level} · line {entry.line + 1}")
                item.setSizeHint(QSize(0, 30))
            item.setData(OUTLINE_ROLE, index)
            self.outline_list.addItem(item)

        if not self.current_outline:
            item = QListWidgetItem("No headings or scene breaks")
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.outline_list.addItem(item)
        self.outline_list.blockSignals(False)

    def _update_document_outline(self, source: str | None) -> None:
        self.current_outline = document_outline(source) if source is not None else []
        self._outline_document_positions = []
        has_document = source is not None
        has_outline = bool(self.current_outline)
        self.outline_contents_button.setEnabled(has_document)
        self.outline_button.setEnabled(has_outline)
        if hasattr(self, "outline_action"):
            self.outline_action.setEnabled(has_outline)
        self._populate_outline_list()
        if not has_document and self.contents_mode == "outline":
            self._set_contents_mode("folder")

    def _outline_item_activated(self, item: QListWidgetItem) -> None:
        index = item.data(OUTLINE_ROLE)
        if index is not None:
            self._jump_to_outline(int(index))

    def _select_outline_entry(self, index: int) -> None:
        if not 0 <= index < self.outline_list.count():
            return
        self.outline_list.blockSignals(True)
        self.outline_list.setCurrentRow(index)
        self.outline_list.scrollToItem(self.outline_list.item(index))
        self.outline_list.blockSignals(False)

    def _cache_outline_positions(self) -> None:
        if self.current_document is None or self.current_mode != "Rendered":
            self._outline_document_positions = []
            return
        positions: list[int] = []
        block = self.reader.document().begin()
        for entry in self.current_outline:
            while block.isValid():
                is_target = (
                    block.text().strip() == entry.title
                    if entry.kind == "heading"
                    else not block.text().strip()
                )
                if is_target:
                    positions.append(block.position())
                    block = block.next()
                    break
                block = block.next()
            else:
                break
        self._outline_document_positions = positions
        self._reader_scroll_changed()

    def _reader_scroll_changed(self, _value: int = 0) -> None:
        if self._outline_sync_pending:
            return
        self._outline_sync_pending = True
        QTimer.singleShot(0, self._sync_outline_selection)

    def _sync_outline_selection(self) -> None:
        self._outline_sync_pending = False
        if not self.current_outline or self.current_document is None:
            return
        cursor = self.reader.cursorForPosition(QPoint(12, 12))
        if self.current_mode == "Raw":
            location = cursor.blockNumber()
            markers = [entry.line for entry in self.current_outline]
        elif self.current_mode == "Rendered":
            location = cursor.position()
            markers = self._outline_document_positions
        else:
            return
        active = 0
        for index, marker in enumerate(markers):
            if marker > location:
                break
            active = index
        self._select_outline_entry(active)

    def _jump_to_outline(self, index: int) -> None:
        if self.current_document is None or not 0 <= index < len(self.current_outline):
            return
        entry = self.current_outline[index]
        self._cancel_pending_scroll_restore()
        self._select_outline_entry(index)

        if self.current_mode == "Diff":
            self.mode_buttons["Rendered"].setChecked(True)
            self._show_mode("Rendered")

        if self.current_mode == "Raw":
            block = self.reader.document().findBlockByNumber(entry.line)
            if block.isValid():
                self.reader.setTextCursor(QTextCursor(block))
                block_top = self.reader.document().documentLayout().blockBoundingRect(block).top()
                self.reader.verticalScrollBar().setValue(max(0, round(block_top) - 14))
        else:
            self.reader.scrollToAnchor(entry.anchor)
            QTimer.singleShot(0, lambda anchor=entry.anchor: self.reader.scrollToAnchor(anchor))
        self._save_current_scroll()

    def _show_outline_menu(self) -> None:
        if not self.current_outline:
            return
        menu = QMenu(self)
        menu.setObjectName("outlineMenu")
        base_level = min(
            (entry.level for entry in self.current_outline if entry.kind == "heading"),
            default=1,
        )
        for index, entry in enumerate(self.current_outline):
            if entry.kind == "scene":
                label = f"—  {entry.title}  —"
            else:
                label = f"{'    ' * max(0, entry.level - base_level)}{entry.title}"
            action = menu.addAction(label)
            action.triggered.connect(
                lambda _checked=False, target=index: self._jump_to_outline(target)
            )
        menu.popup(
            self.outline_button.mapToGlobal(QPoint(0, self.outline_button.height() + 2))
        )

    def _open_outline_navigation(self) -> None:
        if not self.current_outline:
            return
        if self.reading_mode:
            self._show_outline_menu()
        else:
            self._set_contents_mode("outline")
            self.outline_list.setFocus(Qt.FocusReason.ShortcutFocusReason)

    def _display_name(self, path: Path) -> str:
        return path.stem if self.repository.is_file(path) else path.name

    def _content_selected(self) -> None:
        selected = self.document_list.selectedItems()
        if not selected:
            return
        path = Path(selected[0].data(PATH_ROLE))
        if self.repository.is_file(path):
            if self.active_query:
                self.current_mode = "Rendered"
                self.mode_buttons["Rendered"].setChecked(True)
            self._open_path(path)

    def _content_activated(self, item: QListWidgetItem) -> None:
        path = Path(item.data(PATH_ROLE))
        if self.repository.is_directory(path):
            matches = self.folder_tree.findItems(
                path.name, Qt.MatchFlag.MatchExactly | Qt.MatchFlag.MatchRecursive
            )
            match = next((candidate for candidate in matches if candidate.data(0, PATH_ROLE) == str(path)), None)
            if match:
                self.folder_tree.setCurrentItem(match)
                self.folder_tree.scrollToItem(match)
            else:
                self._show_folder(path)
        else:
            self._open_path(path)

    def _active_reader_widget(self) -> QTextBrowser:
        if self.current_image_path is not None:
            return self.image_page
        if self.current_mode == "Diff":
            return self.diff_reader
        return self.reader

    def _scroll_storage_key(self, path: Path, mode: str) -> str:
        revision = self.repository.revision or "working-tree"
        relative = self.repository.relative(path).as_posix()
        identity = f"{revision}\0{relative}\0{scroll_storage_mode(mode)}"
        digest = hashlib.sha1(identity.encode()).hexdigest()
        return f"{self.settings_prefix}/scroll/{digest}"

    def _capture_navigation_entry(self, *, persist: bool = True) -> NavigationEntry | None:
        path = self.current_document or self.current_image_path
        if path is None:
            return None
        scroll_bar = self._active_reader_widget().verticalScrollBar()
        ratio = normalized_scroll(scroll_bar.value(), scroll_bar.maximum())
        if persist:
            self.settings.setValue(self._scroll_storage_key(path, self.current_mode), ratio)
        return NavigationEntry(
            relative_path=PurePosixPath(self.repository.relative(path).as_posix()),
            mode=self.current_mode,
            scroll_ratio=ratio,
        )

    def _save_current_scroll(self) -> None:
        self._capture_navigation_entry(persist=True)

    def _cancel_pending_scroll_restore(self) -> None:
        pending = self._pending_scroll_restore
        if pending is None:
            return
        scroll_bar, range_handler, action_handler, pressed_handler, _apply = pending
        try:
            scroll_bar.rangeChanged.disconnect(range_handler)
            scroll_bar.actionTriggered.disconnect(action_handler)
            scroll_bar.sliderPressed.disconnect(pressed_handler)
        except RuntimeError:
            pass
        self._pending_scroll_restore = None

    def _finish_pending_scroll_restore(self) -> None:
        pending = self._pending_scroll_restore
        if pending is None:
            return
        _scroll_bar, _range_handler, _action_handler, _pressed_handler, apply = pending
        apply()
        self._cancel_pending_scroll_restore()

    def _restore_document_scroll(
        self,
        path: Path,
        *,
        mode: str | None = None,
        ratio: float | None = None,
        position: tuple[int, int] | None = None,
        on_restored: Callable[[int, int], None] | None = None,
    ) -> None:
        expected_path = self.repository.resolve(path)
        expected_root = self.repository.root
        expected_revision = self.repository.revision
        expected_mode = mode or self.current_mode
        if ratio is None and position is None:
            ratio = self.settings.value(
                self._scroll_storage_key(expected_path, expected_mode), 0.0, type=float
            )

        self._cancel_pending_scroll_restore()
        scroll_bar = self._active_reader_widget().verticalScrollBar()

        def restore() -> None:
            current_path = self.current_document or self.current_image_path
            if (
                self.repository.root != expected_root
                or self.repository.revision != expected_revision
                or current_path != expected_path
                or self.current_mode != expected_mode
            ):
                return
            if position is not None:
                stored_value, stored_maximum = position
                target = (
                    stored_value
                    if scroll_bar.maximum() == stored_maximum
                    else restored_scroll(
                        normalized_scroll(stored_value, stored_maximum),
                        scroll_bar.maximum(),
                    )
                )
            else:
                target = restored_scroll(float(ratio), scroll_bar.maximum())
            scroll_bar.setValue(target)
            if on_restored is not None:
                on_restored(scroll_bar.value(), scroll_bar.maximum())

        def range_changed(_minimum: int, _maximum: int) -> None:
            restore()

        def user_action(_action: int) -> None:
            self._cancel_pending_scroll_restore()

        def user_pressed() -> None:
            self._cancel_pending_scroll_restore()

        scroll_bar.rangeChanged.connect(range_changed)
        scroll_bar.actionTriggered.connect(user_action)
        scroll_bar.sliderPressed.connect(user_pressed)
        self._pending_scroll_restore = (
            scroll_bar,
            range_changed,
            user_action,
            user_pressed,
            restore,
        )
        QTimer.singleShot(0, restore)

    def _remember_current_for(self, target: Path) -> None:
        if self._navigating_history:
            return
        current_path = self.current_document or self.current_image_path
        if current_path is None or current_path == target:
            return
        entry = self._capture_navigation_entry(persist=True)
        if entry is not None:
            self.navigation_history.remember(entry)
            self._update_navigation_controls()

    def _update_navigation_controls(self) -> None:
        can_back = self.navigation_history.can_go_back
        can_forward = self.navigation_history.can_go_forward
        self.back_button.setEnabled(can_back)
        self.forward_button.setEnabled(can_forward)
        if hasattr(self, "back_action"):
            self.back_action.setEnabled(can_back)
            self.forward_action.setEnabled(can_forward)

    def _go_back(self) -> None:
        self._navigate_history(back=True)

    def _go_forward(self) -> None:
        self._navigate_history(back=False)

    def _navigate_history(self, *, back: bool) -> None:
        current = self._capture_navigation_entry(persist=True)
        if current is None:
            return
        while True:
            candidate = (
                self.navigation_history.peek_back()
                if back
                else self.navigation_history.peek_forward()
            )
            if candidate is None:
                self._update_navigation_controls()
                return
            target = self.repository.root / Path(candidate.relative_path.as_posix())
            if self.repository.is_file(target):
                break
            if back:
                self.navigation_history.discard_back()
            else:
                self.navigation_history.discard_forward()

        entry = (
            self.navigation_history.go_back(current)
            if back
            else self.navigation_history.go_forward(current)
        )
        if entry is None:
            return
        target = self.repository.root / Path(entry.relative_path.as_posix())
        self._navigating_history = True
        try:
            self.current_mode = entry.mode
            self.mode_buttons.get(entry.mode, self.mode_buttons["Rendered"]).setChecked(True)
            self._open_path(target)
            self._restore_document_scroll(target, mode=self.current_mode, ratio=entry.scroll_ratio)
        finally:
            self._navigating_history = False
        self._update_navigation_controls()

    def _open_path(self, path: Path) -> None:
        if self.repository.is_image(path):
            self._open_image_document(path)
        else:
            self._open_document(path)

    def _open_document(self, path: Path) -> None:
        path = self.repository.resolve(path)
        try:
            source = self.repository.read_text(path)
        except (OSError, ValueError, GitError) as error:
            message = html.escape(str(error))
            self.reader.setHtml(self.renderer._document(f"<h1>Could not read this document</h1><p>{message}</p>"))
            return
        self._remember_current_for(path)
        if path != self.current_document:
            self._clear_live_change_navigation()
        self.current_document = path
        self.current_image_path = None
        self.current_image_data = b""
        self._reading_mode_handoff = None
        self.current_source = source
        self._mark_version_viewed(path)
        self._update_document_outline(source)
        self.reader_title.setText(path.stem)
        self.reader.setSearchPaths([str(path.parent)])
        self.diff_reader.setSearchPaths([str(path.parent)])
        self.mode_buttons["Raw"].setEnabled(True)
        self.mode_buttons["Diff"].setEnabled(True)
        if self.current_mode == "Diff":
            self._refresh_diff_comparisons()
        else:
            self.diff_selector.setVisible(False)
        self._render_current_document()
        self._update_status(path)
        if self.repository.is_working_tree:
            self.watcher.set_document(path)
            self._set_live_state("watching", "● WATCHING")
        else:
            self.watcher.set_document(None)
            self._set_live_state("snapshot", "● SNAPSHOT")
        self._restore_document_scroll(path)

    def _reload_document(self, path: Path) -> None:
        if not self.repository.is_working_tree or self.current_document is None or path != self.current_document:
            return
        try:
            source = self.repository.read_text(path)
        except (OSError, ValueError):
            self._document_availability_changed(False)
            return
        if source == self.current_source:
            self._set_live_state("watching", "● WATCHING")
            return

        previous_blocks = self._reader_blocks() if self.current_mode == "Rendered" else []
        active_reader = self._active_reader_widget()
        scroll_bar = active_reader.verticalScrollBar()
        position = scroll_bar.value()
        self._clear_live_change_navigation()
        self.current_source = source
        self._refresh_change_awareness()
        self._mark_version_viewed(path)
        self._update_document_outline(source)
        self._render_current_document()
        scroll_bar.setValue(min(position, scroll_bar.maximum()))
        self._update_status(path)
        self._set_live_state("updated", "● UPDATED")

        if self.current_mode == "Rendered":
            changed = changed_block_indices(previous_blocks, self._reader_blocks())
            self._set_live_change_navigation(changed)
            if self.highlight_live_changes:
                self._start_change_highlight(changed)
        QTimer.singleShot(1800, self._finish_updated_state)

    def _asset_changed(self, path: Path) -> None:
        if self.current_image_path is not None and path == self.current_image_path:
            self._reload_image(path)
        else:
            self._reload_document(path)

    def _render_current_document(self) -> None:
        if self.current_document is None:
            return
        if self.current_mode == "Diff":
            try:
                comparison = self.diff_selector.currentData() or "auto"
                versions = self.repository.diff_versions(self.current_document, comparison)
                self.diff_reader.setHtml(
                    self.diff_renderer.render(
                        versions, self.current_document, self._resolve_markdown_image
                    )
                )
            except (OSError, ValueError, GitError) as error:
                message = html.escape(str(error))
                self.diff_reader.setHtml(
                    self.renderer._document(f"<h1>Could not build this diff</h1><p>{message}</p>")
                )
            self.reader_stack.setCurrentWidget(self.diff_reader)
        elif self.current_mode == "Raw":
            self.reader.setHtml(self.renderer.raw(self.current_source))
            self.reader_stack.setCurrentWidget(self.reader)
            self._change_selections = []
            self._change_focus_selections = []
            self._apply_search_highlights()
        else:
            self.reader.setHtml(
                self.renderer.render(
                    self.current_source, self.current_document, self._resolve_markdown_image
                )
            )
            self.reader_stack.setCurrentWidget(self.reader)
            self._change_selections = []
            self._change_focus_selections = []
            self._apply_live_change_focus(center=False)
            self._apply_search_highlights()
        self._update_change_navigation_controls()
        QTimer.singleShot(0, self._cache_outline_positions)

    def _show_mode(self, mode: str) -> None:
        if self.current_document is None:
            return
        if mode == self.current_mode:
            return
        # Long QTextDocuments can keep expanding after their first paint. Finish
        # any layout-aware restoration against the latest range before using
        # this view as the handoff source.
        self._finish_pending_scroll_restore()
        source_mode = self.current_mode
        source_scroll = self._active_reader_widget().verticalScrollBar()
        source_position = (source_scroll.value(), source_scroll.maximum())
        source_ratio = normalized_scroll(*source_position)
        self._save_current_scroll()
        handoff: ReadingModeHandoff | None = None
        if source_mode == "Rendered" and mode == "Raw":
            handoff = ReadingModeHandoff(source_position)
            self._reading_mode_handoff = (
                self.current_document,
                self.repository.revision,
                handoff,
            )
        elif source_mode == "Raw" and mode == "Rendered":
            candidate = self._reading_mode_handoff
            if (
                candidate is not None
                and candidate[0] == self.current_document
                and candidate[1] == self.repository.revision
            ):
                handoff = candidate[2]
        else:
            self._reading_mode_handoff = None
        self.current_mode = mode
        self.diff_selector.setVisible(mode == "Diff")
        if mode == "Diff":
            self._refresh_diff_comparisons()
        self._render_current_document()
        shared_reading_modes = {source_mode, mode} == {"Rendered", "Raw"}
        if (
            source_mode == "Raw"
            and mode == "Rendered"
            and handoff is not None
            and handoff.raw_position_is_unchanged(*source_position)
        ):
            self._restore_document_scroll(
                self.current_document,
                mode=mode,
                position=handoff.rendered_position,
            )
        else:
            on_restored = (
                handoff.record_raw_arrival
                if source_mode == "Rendered" and mode == "Raw"
                else None
            )
            self._restore_document_scroll(
                self.current_document,
                mode=mode,
                ratio=source_ratio if shared_reading_modes else None,
                on_restored=on_restored,
            )
        if source_mode == "Raw" and mode == "Rendered":
            self._reading_mode_handoff = None

    def _refresh_diff_comparisons(self) -> None:
        context = (self.repository.root, self.repository.revision)
        previous = (
            self.diff_selector.currentData()
            if self._diff_comparison_context == context
            else None
        )
        try:
            comparisons = self.repository.diff_comparisons()
        except GitError as error:
            self.diff_selector.setToolTip(str(error))
            return

        self.diff_selector.blockSignals(True)
        self.diff_selector.clear()
        for comparison in comparisons:
            self.diff_selector.addItem(comparison.label, comparison.key)
        previous_index = self.diff_selector.findData(previous) if previous is not None else -1
        self.diff_selector.setCurrentIndex(previous_index if previous_index >= 0 else 0)
        self.diff_selector.blockSignals(False)
        self.diff_selector.setToolTip(
            "Choose whether Diff shows the complete feature branch or only uncommitted edits."
            if any(comparison.key == "branch" for comparison in comparisons)
            else "Choose the two document versions shown in Diff."
        )
        self.diff_selector.setVisible(
            self.current_mode == "Diff" and self.current_document is not None
        )
        self._diff_comparison_context = context

    def _diff_comparison_changed(self, _index: int) -> None:
        if self.current_mode != "Diff" or self.current_document is None:
            return
        position = self.diff_reader.verticalScrollBar().value()
        self._render_current_document()
        self.diff_reader.verticalScrollBar().setValue(position)

    def _refresh_git_sidebar(self) -> None:
        active_revision = self.repository.revision
        try:
            current_branch = self.repository.git.current_branch()
            branches = self.repository.git.branches()
            worktrees = self.repository.git.worktrees()
            changes = self.repository.git.changes()
            commits = self.repository.git.recent_commits(active_revision or "HEAD")
        except GitError as error:
            self.branch_selector.setToolTip(str(error))
            return

        self.branch_selector.blockSignals(True)
        self.branch_selector.clear()
        self.branch_selector.addItem(f"Working tree · {current_branch}", None)
        selected_index = 0
        for branch in branches:
            self.branch_selector.addItem(f"Committed · {branch.name}", branch.name)
            if branch.name == active_revision:
                selected_index = self.branch_selector.count() - 1
        self.branch_selector.setCurrentIndex(selected_index)
        self.branch_selector.blockSignals(False)

        if active_revision is not None and selected_index == 0:
            self._switch_repository_view(None)
            return

        self._refresh_diff_comparisons()
        self._refresh_change_awareness()

        self.worktree_list.clear()
        for worktree in worktrees:
            branch = worktree.branch or f"detached {worktree.revision}"
            marker = "●" if worktree.path.resolve(strict=False) == self.repository.root else "○"
            item = QListWidgetItem(f"{marker}  {branch} · {worktree.path.name}")
            item.setData(PATH_ROLE, str(worktree.path))
            if worktree.bare or not worktree.path.is_dir():
                item.setFlags(Qt.ItemFlag.NoItemFlags)
                item.setToolTip(f"Unavailable worktree\n{worktree.path}")
            elif marker == "●":
                item.setToolTip(f"Currently viewing\n{worktree.path}")
            else:
                item.setToolTip(f"Click to view this worktree\n{worktree.path}")
            self.worktree_list.addItem(item)
        self.worktree_list.setFixedHeight(min(92, max(34, len(worktrees) * 30 + 6)))

        self.changes_label.setText(f"WORKING CHANGES · {len(changes)}")
        self.changes_list.clear()
        if changes:
            for change in changes:
                item = QListWidgetItem(change.label)
                item.setData(PATH_ROLE, change.path.as_posix())
                item.setToolTip(change.path.as_posix())
                self.changes_list.addItem(item)
        else:
            item = QListWidgetItem("Working tree clean")
            item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.changes_list.addItem(item)

        self.commits_list.clear()
        for commit in commits:
            date = commit.committed_at.astimezone().strftime("%b %-d")
            item = QListWidgetItem(f"{commit.short_revision}  {commit.subject}\n{date} · {commit.author}")
            item.setToolTip(f"{commit.revision}\n{commit.committed_at.astimezone():%b %-d, %Y · %-I:%M %p}")
            self.commits_list.addItem(item)

    def _view_revision_changed(self, _index: int) -> None:
        self._switch_repository_view(self.branch_selector.currentData())

    def _worktree_selected(self, item: QListWidgetItem) -> None:
        path_text = item.data(PATH_ROLE)
        if path_text:
            self._switch_worktree(Path(str(path_text)))

    def _switch_worktree(self, path: Path) -> None:
        try:
            target = path.expanduser().resolve(strict=True)
        except OSError as error:
            QMessageBox.warning(self, "Worktree unavailable", str(error))
            self._refresh_git_sidebar()
            return
        if target == self.repository.root:
            return

        try:
            working_tree = Repository.open(target)
            replacement = RepositoryView(working_tree, GitClient(working_tree.root))
        except (OSError, ValueError, GitError) as error:
            QMessageBox.warning(self, "Worktree unavailable", str(error))
            self._refresh_git_sidebar()
            return

        self._save_repository_state()
        self._detach_watchers()
        self.navigation_history.clear()
        self.repository = replacement
        self.settings_prefix = self._settings_prefix_for(replacement.root)
        self.change_tracker = self._load_change_tracker()
        self.repository_name.setText(replacement.root.name)
        self.setWindowTitle(f"Elvandar Viewer — {replacement.root.name}")
        self.settings.setValue("repository/path", str(replacement.root))
        self.search_field.blockSignals(True)
        self.search_field.clear()
        self.search_field.blockSignals(False)
        self.active_query = ""
        self.search_index = SearchIndex()
        self._clear_document()
        self._attach_watchers()
        self._populate_tree()
        self._refresh_git_sidebar()
        self._rebuild_search_index()
        self._restore_repository_state(restore_layout=True)
        self._set_reading_mode(self.reading_mode, persist=False)
        self._update_navigation_controls()
        self.settings.sync()

    def _switch_repository_view(self, revision: str | None) -> None:
        if revision == self.repository.revision:
            return
        self._save_current_scroll()
        current_path = self.current_document or self.current_image_path
        relative_document = (
            self.repository.relative(current_path) if current_path is not None else None
        )
        try:
            if revision is None:
                self.repository.show_working_tree()
            else:
                self.repository.show_revision(revision)
        except GitError as error:
            self.branch_selector.setToolTip(str(error))
            self._refresh_git_sidebar()
            return

        self.watcher.set_document(None)
        self.navigation_history.clear()
        self._clear_document()
        self._rebuild_search_index()
        self._populate_tree()
        if relative_document is not None:
            candidate = self.repository.root / relative_document
            if self.repository.is_file(candidate):
                self._navigating_history = True
                try:
                    self._open_path(candidate)
                finally:
                    self._navigating_history = False

        if revision is None:
            self._set_live_state("watching", "● WATCHING")
        else:
            self._set_live_state("snapshot", "● SNAPSHOT")
        self._update_navigation_controls()
        self._refresh_git_sidebar()

    def _clear_document(self) -> None:
        self._clear_live_change_navigation()
        self.current_document = None
        self.current_image_path = None
        self.current_image_data = b""
        self.current_source = ""
        self._update_document_outline(None)
        self._reading_mode_handoff = None
        self.reader_title.setText("Choose a document")
        self.reader_title.setToolTip("")
        self.reader.setHtml(self._welcome_document())
        self.reader_stack.setCurrentWidget(self.reader)
        self.current_mode = "Rendered"
        self.mode_buttons["Rendered"].setChecked(True)
        self.mode_buttons["Raw"].setEnabled(True)
        self.mode_buttons["Diff"].setEnabled(False)
        self.diff_selector.setVisible(False)
        self._search_selections = []
        self._change_selections = []
        self._change_focus_selections = []

    def _changed_file_activated(self, item: QListWidgetItem) -> None:
        relative = item.data(PATH_ROLE)
        if not relative:
            return
        if not self.repository.is_working_tree:
            self.branch_selector.setCurrentIndex(0)
        target = self.repository.root / str(relative)
        if self.repository.is_file(target) and target.suffix.casefold() in {".md", ".markdown", ".txt"}:
            self._open_document(target)
        elif target.suffix.casefold() in {".md", ".markdown", ".txt"}:
            baseline = self.repository.git.show_file_optional("HEAD", PurePosixPath(str(relative)))
            if baseline is not None:
                self._open_deleted_document(target)

    def _open_deleted_document(self, path: Path) -> None:
        path = self.repository.resolve(path)
        self._remember_current_for(path)
        if path != self.current_document:
            self._clear_live_change_navigation()
        self.current_document = path
        self.current_source = ""
        self._update_document_outline("")
        self.reader_title.setText(path.stem)
        self.reader_title.setToolTip(f"{self.repository.relative(path)}\nDeleted from working tree")
        self.reader.setSearchPaths([str(path.parent)])
        self.diff_reader.setSearchPaths([str(path.parent)])
        self.current_mode = "Diff"
        self.mode_buttons["Raw"].setEnabled(True)
        self.mode_buttons["Diff"].setEnabled(True)
        self.mode_buttons["Diff"].setChecked(True)
        self._refresh_diff_comparisons()
        self._render_current_document()
        self.watcher.set_document(path)
        self._set_live_state("waiting", "● DELETED")
        self._restore_document_scroll(path, mode="Diff")

    def _open_image_document(self, path: Path) -> None:
        path = self.repository.resolve(path)
        try:
            data = self.repository.read_binary(path)
        except (OSError, ValueError, GitError) as error:
            message = html.escape(str(error))
            self.image_page.setHtml(
                self.renderer._document(f"<h1>Could not read this image</h1><p>{message}</p>")
            )
            self.reader_stack.setCurrentWidget(self.image_page)
            return

        self._remember_current_for(path)
        self._clear_live_change_navigation()
        self._set_image_preview(path, data)
        self.current_document = None
        self.current_image_path = path
        self.current_image_data = data
        self.current_source = ""
        self._mark_version_viewed(path)
        self._update_document_outline(None)
        self.current_mode = "Rendered"
        self.mode_buttons["Rendered"].setChecked(True)
        self.mode_buttons["Raw"].setEnabled(False)
        self.mode_buttons["Diff"].setEnabled(False)
        self.diff_selector.setVisible(False)
        self.reader_title.setText(path.stem)
        self._update_image_status(path, data)
        if self.repository.is_working_tree:
            self.watcher.set_document(path)
            self._set_live_state("watching", "● WATCHING")
        else:
            self.watcher.set_document(None)
            self._set_live_state("snapshot", "● SNAPSHOT")
        self._restore_document_scroll(path, mode="Rendered")

    def _reload_image(self, path: Path) -> None:
        if not self.repository.is_working_tree or path != self.current_image_path:
            return
        try:
            data = self.repository.read_binary(path)
        except (OSError, ValueError):
            self._document_availability_changed(False)
            return
        if data == self.current_image_data:
            return
        self.current_image_data = data
        self._refresh_change_awareness()
        self._mark_version_viewed(path)
        self._set_image_preview(path, data)
        self._update_image_status(path, data)
        self._set_live_state("updated", "● UPDATED")
        QTimer.singleShot(1800, self._finish_updated_state)

    def _set_image_preview(self, path: Path, data: bytes) -> None:
        image = QImage.fromData(data)
        if image.isNull():
            raise ValueError(f"Could not decode image: {path.name}")
        source = self._image_source(path, data)
        name = html.escape(path.name)
        size = self._human_size(len(data))
        scale = min(720 / image.width(), 610 / image.height(), 1.0)
        display_width = max(1, round(image.width() * scale))
        display_height = max(1, round(image.height() * scale))
        if self.night_mode:
            background, text, frame, border, muted, link = (
                "#191C21",
                "#E1E4E9",
                "#24282F",
                "#3B414B",
                "#969EAA",
                "#8FB5E6",
            )
        else:
            background, text, frame, border, muted, link = (
                "#F7F8FA",
                "#252932",
                "#FFFFFF",
                "#D9DDE3",
                "#7A8290",
                "#315D9B",
            )
        self.image_page.setHtml(
            f"""<!doctype html><html><head><meta charset="utf-8"><style>
            body {{ margin: 0; padding: 44px; background: {background}; color: {text};
              font-family: -apple-system, BlinkMacSystemFont, sans-serif; text-align: center; }}
            .frame {{ display: inline-block; padding: 12px; background: {frame};
              border: 1px solid {border}; border-radius: 9px; }}
            img {{ max-width: 100%; }}
            .name {{ margin-top: 18px; font-size: 14px; font-weight: 600; }}
            .details {{ margin-top: 6px; color: {muted}; font-size: 11px; }}
            .hint {{ margin-top: 12px; color: {link}; font-size: 11px; }}
            </style></head><body><div class="frame"><a href="elvandar-current-image:">
            <img src="{html.escape(source, quote=True)}" alt="{name}"
              width="{display_width}" height="{display_height}"></a></div>
            <div class="name">{name}</div><div class="details">{image.width():,} × {image.height():,} px · {size}</div>
            <div class="hint">Click the image to zoom and pan</div></body></html>"""
        )
        self.reader_stack.setCurrentWidget(self.image_page)

    def _update_image_status(self, path: Path, data: bytes) -> None:
        location = self.repository.relative(path).as_posix()
        if self.repository.is_working_tree and path.is_file():
            changed = datetime.fromtimestamp(path.stat().st_mtime).strftime("%b %-d, %Y · %-I:%M %p")
        else:
            changed = f"Committed snapshot · {self.repository.revision}"
        self.reader_title.setToolTip(f"{location}\n{changed}\n{self._human_size(len(data))}")

    def _resolve_markdown_image(self, source: str, parent: Path) -> str:
        try:
            target = self.repository.resolve(parent / source)
            if not self.repository.is_image(target):
                return source
            data = self.repository.read_binary(target)
        except (OSError, ValueError, GitError):
            return source
        return self._image_source(target, data)

    def _image_source(self, path: Path, data: bytes) -> str:
        if self.repository.is_working_tree:
            return QUrl.fromLocalFile(str(path)).toString()
        mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        encoded = base64.b64encode(data).decode("ascii")
        return f"data:{mime_type};base64,{encoded}"

    def _open_image_window(self, path: Path) -> None:
        try:
            data = (
                self.current_image_data
                if self.current_image_path == path and self.current_image_data
                else self.repository.read_binary(path)
            )
            viewer = ImageViewerDialog(data, path.name, self)
        except (OSError, ValueError, GitError):
            return
        self.image_windows.append(viewer)

        def release() -> None:
            if viewer in self.image_windows:
                self.image_windows.remove(viewer)

        viewer.destroyed.connect(release)
        viewer.show()
        viewer.raise_()

    def _repository_structure_changed(self) -> None:
        if not self.repository.is_working_tree:
            return
        self._rebuild_search_index()
        selected = self.folder_tree.selectedItems()
        selected_path = Path(selected[0].data(0, PATH_ROLE)) if selected else self.repository.root
        if not self.repository.is_directory(selected_path):
            selected_path = self.repository.root
        self._populate_tree(selected_path)

    def _setup_shortcuts(self) -> None:
        self.find_shortcut = QShortcut(QKeySequence.StandardKey.Find, self)
        self.find_shortcut.activated.connect(self._focus_search)
        self.escape_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape), self)
        self.escape_shortcut.activated.connect(self._handle_escape)

    def _build_menus(self) -> None:
        file_menu = self.menuBar().addMenu("File")
        settings_action = QAction("Settings…", self)
        settings_action.setMenuRole(QAction.MenuRole.PreferencesRole)
        settings_action.setShortcut(QKeySequence("Ctrl+,"))
        settings_action.triggered.connect(self._show_settings)
        file_menu.addAction(settings_action)
        file_menu.addSeparator()
        close_action = QAction("Close Window", self)
        close_action.setShortcut(QKeySequence.StandardKey.Close)
        close_action.triggered.connect(self.close)
        file_menu.addAction(close_action)

        go_menu = self.menuBar().addMenu("Go")
        self.back_action = QAction("Back", self)
        self.back_action.setShortcut(QKeySequence("Ctrl+["))
        self.back_action.triggered.connect(self._go_back)
        go_menu.addAction(self.back_action)
        self.forward_action = QAction("Forward", self)
        self.forward_action.setShortcut(QKeySequence("Ctrl+]"))
        self.forward_action.triggered.connect(self._go_forward)
        go_menu.addAction(self.forward_action)
        go_menu.addSeparator()
        self.previous_change_action = QAction("Previous Change", self)
        self.previous_change_action.setShortcut(QKeySequence("Ctrl+Alt+Up"))
        self.previous_change_action.triggered.connect(self._go_to_previous_change)
        go_menu.addAction(self.previous_change_action)
        self.next_change_action = QAction("Next Change", self)
        self.next_change_action.setShortcut(QKeySequence("Ctrl+Alt+Down"))
        self.next_change_action.triggered.connect(self._go_to_next_change)
        go_menu.addAction(self.next_change_action)

        view_menu = self.menuBar().addMenu("View")
        search_action = QAction("Search Library", self)
        search_action.triggered.connect(self._focus_search)
        view_menu.addAction(search_action)
        view_menu.addSeparator()
        for label, shortcut in (("Rendered", "Ctrl+1"), ("Raw", "Ctrl+2"), ("Diff", "Ctrl+3")):
            action = QAction(label, self)
            action.setShortcut(QKeySequence(shortcut))
            action.triggered.connect(self.mode_buttons[label].click)
            view_menu.addAction(action)
        view_menu.addSeparator()

        self.outline_action = QAction("Document Outline", self)
        self.outline_action.setShortcut(QKeySequence("Ctrl+Shift+O"))
        self.outline_action.setEnabled(bool(self.current_outline))
        self.outline_action.triggered.connect(self._open_outline_navigation)
        view_menu.addAction(self.outline_action)
        view_menu.addSeparator()

        text_size_menu = view_menu.addMenu("Text Size")
        increase_text_action = QAction("Increase Text Size", self)
        increase_text_action.setShortcuts(
            [QKeySequence(QKeySequence.StandardKey.ZoomIn), QKeySequence("Ctrl+=")]
        )
        increase_text_action.triggered.connect(self._increase_text_size)
        text_size_menu.addAction(increase_text_action)

        decrease_text_action = QAction("Decrease Text Size", self)
        decrease_text_action.setShortcut(QKeySequence(QKeySequence.StandardKey.ZoomOut))
        decrease_text_action.triggered.connect(self._decrease_text_size)
        text_size_menu.addAction(decrease_text_action)

        reset_text_action = QAction("Actual Text Size", self)
        reset_text_action.setShortcut(QKeySequence("Ctrl+0"))
        reset_text_action.triggered.connect(self._reset_text_size)
        text_size_menu.addAction(reset_text_action)
        view_menu.addSeparator()

        self.reading_action = QAction("Reading Mode", self)
        self.reading_action.setCheckable(True)
        self.reading_action.setChecked(self.reading_mode)
        self.reading_action.setShortcut(QKeySequence("Ctrl+Shift+R"))
        self.reading_action.triggered.connect(self._set_reading_mode)
        view_menu.addAction(self.reading_action)

        help_menu = self.menuBar().addMenu("Help")
        help_action = QAction("Elvandar Viewer Help", self)
        help_action.setShortcut(QKeySequence("Ctrl+?"))
        help_action.triggered.connect(lambda _checked=False: self._show_help("welcome"))
        help_menu.addAction(help_action)

        shortcuts_action = QAction("Keyboard Shortcuts", self)
        shortcuts_action.triggered.connect(lambda _checked=False: self._show_help("shortcuts"))
        help_menu.addAction(shortcuts_action)

        live_help_action = QAction("How Live Updates Work", self)
        live_help_action.triggered.connect(lambda _checked=False: self._show_help("live"))
        help_menu.addAction(live_help_action)

        safety_action = QAction("Read-Only Safety", self)
        safety_action.triggered.connect(lambda _checked=False: self._show_help("safety"))
        help_menu.addAction(safety_action)
        help_menu.addSeparator()

        about_action = QAction("About Elvandar Viewer", self)
        about_action.triggered.connect(self._show_about)
        help_menu.addAction(about_action)
        self._update_navigation_controls()
        self._update_change_navigation_controls()

    def _set_appearance_mode(self, mode: str, *, persist: bool = True) -> None:
        self.appearance_mode = mode if mode in {"system", "day", "night"} else "system"
        if persist:
            self.settings.setValue("appearance/mode", self.appearance_mode)
            self.settings.remove("appearance/night_mode")
        application = QApplication.instance()
        system_is_dark = system_uses_dark_mode(application) if application is not None else False
        self._apply_night_mode(night_mode_for(self.appearance_mode, system_is_dark))

    def _apply_night_mode(self, enabled: bool) -> None:
        self.night_mode = enabled
        application = QApplication.instance()
        if application is not None:
            application.setStyleSheet(app_stylesheet(enabled))

        self.renderer = MarkdownRenderer(enabled, self.reading_font_size)
        self.diff_renderer = DiffRenderer(self.renderer)
        if self.help_dialog is not None:
            self.help_dialog.set_night_mode(enabled)
        if hasattr(self, "outline_list"):
            self._populate_outline_list()
        if hasattr(self, "change_legend"):
            self._refresh_change_decorations()

        active_reader = self._active_reader_widget()
        position = active_reader.verticalScrollBar().value()
        if self.current_image_path is not None and self.current_image_data:
            self._set_image_preview(self.current_image_path, self.current_image_data)
        elif self.current_document is not None:
            self._render_current_document()
            self._apply_search_highlights()
        else:
            self.reader.setHtml(self._welcome_document())
        active_reader.verticalScrollBar().setValue(position)

    def _system_color_scheme_changed(self, _scheme: Qt.ColorScheme) -> None:
        if self.appearance_mode != "system":
            return
        application = QApplication.instance()
        if application is not None:
            self._apply_night_mode(system_uses_dark_mode(application))

    def _show_settings(self) -> None:
        dialog = SettingsDialog(
            SettingsValues(
                appearance_mode=self.appearance_mode,
                reading_width=self.reading_width,
                font_size=self.reading_font_size,
                remember_reading_mode=self.remember_reading_mode,
                highlight_live_changes=self.highlight_live_changes,
            ),
            self,
        )
        if not dialog.exec():
            return

        values = dialog.values()
        self.reading_width = values.reading_width
        self.reading_font_size = clamp_font_size(values.font_size)
        self.remember_reading_mode = values.remember_reading_mode
        self.highlight_live_changes = values.highlight_live_changes
        self.settings.setValue("reading/page_width", self.reading_width)
        self.settings.setValue("reading/page_width_version", 2)
        self.settings.setValue("reading/font_size", self.reading_font_size)
        self.settings.setValue("reading/remember_mode", self.remember_reading_mode)
        self.settings.setValue("live_updates/highlight_changes", self.highlight_live_changes)
        if self.remember_reading_mode:
            self.settings.setValue("appearance/reading_mode", self.reading_mode)
        else:
            self.settings.remove("appearance/reading_mode")
        self._set_appearance_mode(values.appearance_mode)
        self._set_reading_mode(self.reading_mode, persist=False)
        self.settings.sync()

    def _set_reading_font_size(self, font_size: int, *, persist: bool = True) -> None:
        self.reading_font_size = clamp_font_size(font_size)
        if persist:
            self.settings.setValue("reading/font_size", self.reading_font_size)
        self._apply_night_mode(self.night_mode)

    def _increase_text_size(self) -> None:
        self._set_reading_font_size(self.reading_font_size + 1)

    def _decrease_text_size(self) -> None:
        self._set_reading_font_size(self.reading_font_size - 1)

    def _reset_text_size(self) -> None:
        self._set_reading_font_size(DEFAULT_FONT_SIZE)

    def _set_reading_mode(self, enabled: bool, *, persist: bool = True) -> None:
        if enabled and not self.reading_mode:
            self._splitter_state_before_reading = self.splitter.saveState()
        elif enabled and self._splitter_state_before_reading is None:
            self._splitter_state_before_reading = self.splitter.saveState()

        self.reading_mode = enabled
        for index in (0, 1, 3):
            self.splitter.widget(index).setVisible(not enabled)
        self.reader_layout.setAlignment(
            self.reader_stack,
            Qt.AlignmentFlag.AlignHCenter if enabled else Qt.AlignmentFlag(0),
        )
        if enabled:
            self._update_reading_page_width()
        else:
            self.reader_stack.setMinimumWidth(0)
            self.reader_stack.setMaximumWidth(16_777_215)

        if not enabled and self._splitter_state_before_reading is not None:
            self.splitter.restoreState(self._splitter_state_before_reading)
            self._splitter_state_before_reading = None

        self.reading_button.setChecked(enabled)
        if hasattr(self, "reading_action"):
            self.reading_action.setChecked(enabled)
        if persist and self.remember_reading_mode:
            self.settings.setValue("appearance/reading_mode", enabled)
        if enabled:
            self._active_reader_widget().setFocus(Qt.FocusReason.OtherFocusReason)

    def _update_reading_page_width(self) -> None:
        page_width = reading_page_width(self.reading_width, self.width())
        self.reader_stack.setMinimumWidth(page_width)
        self.reader_stack.setMaximumWidth(page_width)

    def resizeEvent(self, event: QResizeEvent) -> None:  # noqa: N802 - Qt API
        super().resizeEvent(event)
        if self.reading_mode and hasattr(self, "reader_stack"):
            self._update_reading_page_width()

    def _handle_escape(self) -> None:
        if self.active_query:
            self.search_field.clear()
        elif self.reading_mode:
            self._set_reading_mode(False)

    def _show_about(self) -> None:
        QMessageBox.about(
            self,
            "About Elvandar Viewer",
            f"<b>Elvandar Viewer {__version__}</b><br><br>"
            "A private, read-only library for watching the Elvandar manuscript evolve.<br><br>"
            "Git remains the source of truth. The viewer never edits the repository.",
        )

    def _show_help(self, topic: str = "welcome") -> None:
        if self.help_dialog is None:
            self.help_dialog = HelpDialog(self.night_mode, self)
        self.help_dialog.set_night_mode(self.night_mode)
        self.help_dialog.open_topic(topic)
        self.help_dialog.show()
        self.help_dialog.raise_()
        self.help_dialog.activateWindow()

    def _restore_window_state(self) -> None:
        geometry = self.settings.value(f"{self.settings_prefix}/geometry")
        if geometry:
            self.restoreGeometry(geometry)
        self._restore_repository_state(restore_layout=True)

    def _restore_repository_state(self, *, restore_layout: bool) -> None:
        splitter_state = self.settings.value(f"{self.settings_prefix}/splitter")
        if restore_layout and splitter_state:
            self.splitter.restoreState(splitter_state)

        document_text = self.settings.value(f"{self.settings_prefix}/document", "", type=str)
        if document_text:
            document = self.repository.root / document_text
            if self.repository.is_file(document):
                self._navigating_history = True
                try:
                    self._open_path(document)
                    self._reveal_document_in_navigation(document)
                finally:
                    self._navigating_history = False
                return

        folder_text = self.settings.value(f"{self.settings_prefix}/folder", "", type=str)
        if folder_text:
            folder = self.repository.root / folder_text
            item = self._find_tree_item(folder)
            if item is not None:
                self.folder_tree.setCurrentItem(item)

    def _save_repository_state(self) -> None:
        self._save_current_scroll()
        self.settings.setValue(f"{self.settings_prefix}/geometry", self.saveGeometry())
        splitter_state = (
            self._splitter_state_before_reading
            if self._splitter_state_before_reading is not None
            else self.splitter.saveState()
        )
        self.settings.setValue(f"{self.settings_prefix}/splitter", splitter_state)
        selected = self.folder_tree.selectedItems()
        if selected:
            folder = Path(selected[0].data(0, PATH_ROLE))
            self.settings.setValue(
                f"{self.settings_prefix}/folder", self.repository.relative(folder).as_posix()
            )
        current_path = self.current_document or self.current_image_path
        if current_path is not None:
            self.settings.setValue(
                f"{self.settings_prefix}/document", self.repository.relative(current_path).as_posix()
            )
        else:
            self.settings.remove(f"{self.settings_prefix}/document")

    def closeEvent(self, event: QCloseEvent) -> None:  # noqa: N802 - Qt API
        self._save_repository_state()
        self.settings.sync()
        super().closeEvent(event)

    def _focus_search(self) -> None:
        self.search_field.setFocus(Qt.FocusReason.ShortcutFocusReason)
        self.search_field.selectAll()

    def _search_changed(self, query: str) -> None:
        self.active_query = query.strip()
        if self.active_query:
            self._show_search_results()
        else:
            self._search_selections = []
            self._apply_combined_selections()
            selected = self.folder_tree.selectedItems()
            folder = Path(selected[0].data(0, PATH_ROLE)) if selected else self.repository.root
            self._show_folder(folder)

    def _show_search_results(self) -> None:
        results = self.search_index.search(self.active_query)
        self._folder_contents_title = f"Search · {len(results)}"
        if self.contents_mode == "folder":
            self.contents_title.setText(self._folder_contents_title)
        self.document_list.clear()
        if not results:
            item = QListWidgetItem("No documents match")
            item.setFlags(Qt.ItemFlag.NoItemFlags)
            self.document_list.addItem(item)
            self._apply_search_highlights()
            return

        for result in results:
            section = result.location.split("/", 1)[0]
            display = f"{result.title}\n{section} · {result.excerpt}"
            item = QListWidgetItem(display)
            item.setData(PATH_ROLE, str(result.path))
            item.setData(BASE_TEXT_ROLE, display)
            tooltip = f"{result.location}\n\n{result.excerpt}"
            item.setData(BASE_TOOLTIP_ROLE, tooltip)
            item.setToolTip(tooltip)
            item.setSizeHint(QSize(0, 58))
            self.document_list.addItem(item)
        self._refresh_change_decorations()
        self._apply_search_highlights()

    def _open_first_search_result(self) -> None:
        if not self.active_query or not self.document_list.count():
            return
        first = self.document_list.item(0)
        if first.data(PATH_ROLE):
            self.document_list.setCurrentItem(first)

    def _rebuild_search_index(self) -> None:
        try:
            self.search_index.rebuild(self.repository)
            self.search_field.setToolTip("")
        except (OSError, ValueError, GitError) as error:
            self.search_field.setToolTip(str(error))
        if self.active_query:
            self._show_search_results()

    def _search_files_changed(self, paths: list[Path]) -> None:
        if not self.repository.is_working_tree:
            return
        for path in paths:
            self.search_index.update(self.repository, path)
        if self.active_query:
            self._show_search_results()

    def _git_metadata_changed(self) -> None:
        if self.repository.revision is not None:
            revision = self.repository.revision
            current_path = self.current_document or self.current_image_path
            relative_document = (
                self.repository.relative(current_path) if current_path is not None else None
            )
            try:
                self.repository.show_revision(revision)
                self._rebuild_search_index()
                self._populate_tree()
                if relative_document is not None:
                    candidate = self.repository.root / relative_document
                    if self.repository.is_file(candidate):
                        self._open_path(candidate)
                    else:
                        self._clear_document()
            except GitError:
                pass
        self._refresh_git_sidebar()

    def _document_availability_changed(self, available: bool) -> None:
        if not self.repository.is_working_tree:
            return
        if available:
            self._set_live_state("watching", "● WATCHING")
        else:
            self._set_live_state("waiting", "● WAITING")

    def _finish_updated_state(self) -> None:
        if self.live_badge.property("state") == "updated":
            self._set_live_state("watching", "● WATCHING")

    def _set_live_state(self, state: str, text: str) -> None:
        self.live_badge.setText(text)
        self.live_badge.setProperty("state", state)
        self.live_badge.style().unpolish(self.live_badge)
        self.live_badge.style().polish(self.live_badge)

    def _reader_blocks(self) -> list[str]:
        blocks: list[str] = []
        block = self.reader.document().begin()
        while block.isValid():
            blocks.append(block.text())
            block = block.next()
        return blocks

    def _set_live_change_navigation(self, blocks: list[int]) -> None:
        block_count = self.reader.document().blockCount()
        self._live_change_blocks = sorted(
            {index for index in blocks if 0 <= index < block_count}
        )
        self._live_change_index = None
        self._live_change_document = (
            self.current_document if self._live_change_blocks else None
        )
        self._change_focus_selections = []
        self._apply_combined_selections()
        self._update_change_navigation_controls()

    def _clear_live_change_navigation(self) -> None:
        if hasattr(self, "_highlight_timer"):
            self._highlight_timer.stop()
        self._highlighted_blocks = []
        self._change_selections = []
        self._change_focus_selections = []
        self._live_change_blocks = []
        self._live_change_index = None
        self._live_change_document = None
        if hasattr(self, "reader"):
            self._apply_combined_selections()
        if hasattr(self, "change_navigator"):
            self._update_change_navigation_controls()

    def _update_change_navigation_controls(self) -> None:
        available = bool(
            self._live_change_blocks
            and self.current_document == self._live_change_document
            and self.current_mode == "Rendered"
        )
        if self._live_change_index is None:
            count = len(self._live_change_blocks)
            label = f"{count} CHANGE{'S' if count != 1 else ''}"
        else:
            label = f"{self._live_change_index + 1} OF {len(self._live_change_blocks)}"
        self.change_position.setText(label)
        self.change_navigator.setVisible(available)
        self.previous_change_button.setEnabled(available)
        self.next_change_button.setEnabled(available)
        if hasattr(self, "previous_change_action"):
            self.previous_change_action.setEnabled(available)
            self.next_change_action.setEnabled(available)

    def _go_to_previous_change(self) -> None:
        self._go_to_live_change(-1)

    def _go_to_next_change(self) -> None:
        self._go_to_live_change(1)

    def _go_to_live_change(self, step: int) -> None:
        if (
            self.current_mode != "Rendered"
            or self.current_document != self._live_change_document
        ):
            return
        viewport_center = QPoint(0, max(0, self.reader.viewport().height() // 2))
        current_block = self.reader.cursorForPosition(viewport_center).blockNumber()
        target_index = adjacent_change_index(
            self._live_change_blocks,
            current_block=current_block,
            active_index=self._live_change_index,
            step=step,
        )
        if target_index is None:
            return
        self._live_change_index = target_index
        self._apply_live_change_focus(center=True)
        self._update_change_navigation_controls()

    def _apply_live_change_focus(self, *, center: bool) -> None:
        self._change_focus_selections = []
        if (
            self.current_mode != "Rendered"
            or self.current_document != self._live_change_document
            or self._live_change_index is None
            or not 0 <= self._live_change_index < len(self._live_change_blocks)
        ):
            self._apply_combined_selections()
            return
        block_number = self._live_change_blocks[self._live_change_index]
        block = self.reader.document().findBlockByNumber(block_number)
        if not block.isValid():
            self._apply_combined_selections()
            return
        selection = QTextEdit.ExtraSelection()
        selection.cursor = QTextCursor(block)
        selection.cursor.select(QTextCursor.SelectionType.BlockUnderCursor)
        selection.format.setBackground(
            QColor("#4B4029" if self.night_mode else "#F4E4B5")
        )
        self._change_focus_selections = [selection]
        self._apply_combined_selections()
        if center:
            self.reader.setTextCursor(QTextCursor(block))
            self.reader.ensureCursorVisible()
            cursor_rect = self.reader.cursorRect()
            scroll_bar = self.reader.verticalScrollBar()
            scroll_bar.setValue(
                scroll_bar.value()
                + cursor_rect.center().y()
                - self.reader.viewport().height() // 2
            )

    def _start_change_highlight(self, blocks: list[int]) -> None:
        self._highlight_timer.stop()
        self._highlighted_blocks = blocks
        self._highlight_frame = 0
        self._change_selections = []
        self._apply_change_highlight(0.0)
        if blocks:
            self._highlight_timer.start()

    def _fade_change_highlight(self) -> None:
        self._highlight_frame += 1
        progress = min(self._highlight_frame / 16, 1.0)
        self._apply_change_highlight(progress)
        if progress >= 1.0:
            self._highlight_timer.stop()
            self._highlighted_blocks = []
            self._change_selections = []
            self._apply_combined_selections()

    def _apply_change_highlight(self, progress: float) -> None:
        start = QColor("#66552E" if self.night_mode else "#F1DFA9")
        end = QColor("#191C21" if self.night_mode else "#FCFCFD")
        red = round(start.red() + (end.red() - start.red()) * progress)
        green = round(start.green() + (end.green() - start.green()) * progress)
        blue = round(start.blue() + (end.blue() - start.blue()) * progress)
        color = QColor(red, green, blue)
        selections: list[QTextEdit.ExtraSelection] = []
        document = self.reader.document()
        for index in self._highlighted_blocks:
            block = document.findBlockByNumber(index)
            if not block.isValid():
                continue
            selection = QTextEdit.ExtraSelection()
            selection.cursor = QTextCursor(block)
            selection.cursor.select(QTextCursor.SelectionType.BlockUnderCursor)
            selection.format.setBackground(color)
            selections.append(selection)
        self._change_selections = selections
        self._apply_combined_selections()

    def _apply_search_highlights(self) -> None:
        self._search_selections = []
        if not self.active_query or self.current_document is None:
            self._apply_combined_selections()
            return
        document = self._active_reader_widget().document()
        for term in list(dict.fromkeys(self.active_query.split())):
            position = 0
            while len(self._search_selections) < 200:
                cursor = document.find(term, position)
                if cursor.isNull():
                    break
                selection = QTextEdit.ExtraSelection()
                selection.cursor = cursor
                selection.format.setBackground(QColor("#314A68" if self.night_mode else "#DCE9F7"))
                selection.format.setForeground(QColor("#E5EEF9" if self.night_mode else "#203B5F"))
                self._search_selections.append(selection)
                position = max(cursor.selectionEnd(), position + 1)
        self._apply_combined_selections()

    def _apply_combined_selections(self) -> None:
        reader = self._active_reader_widget()
        changes = self._change_selections if self.current_mode == "Rendered" else []
        focus = self._change_focus_selections if self.current_mode == "Rendered" else []
        reader.setExtraSelections(self._search_selections + changes + focus)

    def _update_status(self, path: Path) -> None:
        location = str(self.repository.relative(path))
        if self.repository.is_working_tree:
            if path.is_file():
                stat = path.stat()
                changed = datetime.fromtimestamp(stat.st_mtime).strftime("%b %-d, %Y · %-I:%M %p")
            else:
                changed = "Deleted from working tree"
        else:
            changed = f"Committed snapshot · {self.repository.revision}"
        self.reader_title.setToolTip(f"{location}\n{changed}\n{self._human_size(len(self.current_source.encode('utf-8')))}")

    @staticmethod
    def _human_size(byte_count: int) -> str:
        if byte_count < 1024:
            return f"{byte_count} bytes"
        if byte_count < 1024 * 1024:
            return f"{byte_count / 1024:.1f} KB"
        return f"{byte_count / (1024 * 1024):.1f} MB"

    def _open_link(self, url: QUrl) -> None:
        if url.scheme() == "elvandar-current-image" and self.current_image_path is not None:
            self._open_image_window(self.current_image_path)
            return
        if url.scheme() == "elvandar-image" and self.current_document is not None:
            encoded = url.toString()[len("elvandar-image:") :]
            source = unquote(encoded)
            try:
                target = self.repository.resolve(self.current_document.parent / source)
            except ValueError:
                return
            if self.repository.is_image(target):
                self._open_image_window(target)
            return
        if url.isRelative() and self.current_document is not None:
            try:
                target = self.repository.resolve(self.current_document.parent / url.path())
            except ValueError:
                return
            if target.suffix.casefold() in {".md", ".markdown", ".txt"} and self.repository.is_file(target):
                self._open_document(target)
                return
        if url.isLocalFile():
            target = Path(url.toLocalFile())
            try:
                target = self.repository.resolve(target)
            except ValueError:
                return
            if target.suffix.casefold() in {".md", ".markdown", ".txt"} and self.repository.is_file(target):
                self._open_document(target)
                return
        QDesktopServices.openUrl(url)

    def _welcome_document(self) -> str:
        return self.renderer._document(
            "<h1>Elvandar</h1>"
            "<p>Choose a book, person, place, or history from the library. "
            "The page will appear here as a reading document, never an editor.</p>"
            "<blockquote>The repository stays untouched. This window only reads.</blockquote>"
        )
