from __future__ import annotations

from dataclasses import dataclass

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)


@dataclass(frozen=True, slots=True)
class HelpTopic:
    key: str
    title: str
    eyebrow: str
    summary: str
    body: str


HELP_TOPICS = (
    HelpTopic(
        "welcome",
        "Welcome to Elvandar Viewer",
        "READER’S GUIDE",
        "A private library for watching the manuscript evolve without touching it.",
        """
        <div class="covenant"><b>Claude writes. Git remembers. Elvandar Viewer reads.</b><br>
        The viewer never edits repository files and never asks for exclusive access to them.</div>
        <h2>Start here</h2>
        <ol>
          <li>Choose a folder in <b>Library</b>.</li>
          <li>Choose a chapter, lore page, research document, or image in <b>Contents</b>.</li>
          <li>Read in <b>Rendered</b>, inspect the source in <b>Raw</b>, or review changes in <b>Diff</b>.</li>
          <li>Use <b>Reading Mode</b> when you want the page and nothing else.</li>
        </ol>
        <h2>Designed for a moving repository</h2>
        <p>Files may change while they are on screen. The viewer waits for an AI tool to finish
        replacing a file, reloads the stable result, and recovers automatically from temporary
        incomplete writes.</p>
        """,
    ),
    HelpTopic(
        "navigate",
        "Finding your way",
        "LIBRARY",
        "The four panes keep repository structure, reading, and activity separate.",
        """
        <table class="feature-table">
          <tr><td><b>Library</b></td><td>Browse folders and search the complete repository.</td></tr>
          <tr><td><b>Contents</b></td><td>Switch between the selected folder and the open page’s outline.</td></tr>
          <tr><td><b>Reader</b></td><td>Read rendered Markdown, raw source, diffs, and image previews.</td></tr>
          <tr><td><b>Repository</b></td><td>See the current view, worktrees, changes, and recent commits.</td></tr>
        </table>
        <h2>Search and history</h2>
        <p>Press <span class="key">⌘F</span> to search titles, paths, and document text. Press Return
        to open the first result. Back and Forward revisit documents without changing Git state.</p>
        <h2>Reading order and changed pages</h2>
        <p>Numbered names use natural reading order, so Chapter 2 appears before Chapter 10.
        A solid coral <b>●</b> marks a changed version you have not opened; a hollow blue
        <b>○</b> marks a changed version already viewed. Folders inherit the strongest state
        beneath them, leading you from a book to its changed page.</p>
        <p>Feature worktrees follow Branch vs main, including committed work. Main includes its
        latest commit and current working changes. Unseen versions remain marked until opened.</p>
        <h2>Jump through long pages</h2>
        <p>Choose <b>Page</b> in Contents, click <b>Outline</b> above the reader, or press
        <span class="key">⌘⇧O</span>. Headings retain their hierarchy, manuscript scene breaks
        appear as passage markers, and the selected entry follows your reading position. Outline
        jumps also land on the corresponding Markdown line in Raw view.</p>
        <h2>Images</h2>
        <p>Images display inline and as first-class library items. Click an image to open the
        zoom-and-pan viewer; the original repository file remains untouched.</p>
        """,
    ),
    HelpTopic(
        "views",
        "Reader views",
        "READING",
        "Each view answers a different reading question.",
        """
        <table class="feature-table">
          <tr><td><b>Rendered</b></td><td>How does this document read?</td></tr>
          <tr><td><b>Raw</b></td><td>What Markdown should I copy when asking Claude for a change?</td></tr>
          <tr><td><b>Diff</b></td><td>What changed compared with the useful Git baseline?</td></tr>
          <tr><td><b>Reading</b></td><td>Can I hide everything except the page?</td></tr>
        </table>
        <h2>Rendered and Raw share your place</h2>
        <p>Switching between them keeps you in the same part of the document. A simple round trip
        returns to the exact Rendered position; if you deliberately scroll in Raw, that new
        location transfers back proportionally.</p>
        <h2>Diff comparisons</h2>
        <p>Feature worktrees default to <b>Branch vs main</b>, including committed and uncommitted
        work. Choose <b>Uncommitted</b> to inspect only working-tree changes. On main, Diff compares
        the working file with HEAD.</p>
        """,
    ),
    HelpTopic(
        "live",
        "How live updates work",
        "CLAUDE ACTIVITY",
        "The viewer follows stable filesystem events instead of constantly polling.",
        """
        <p>When an AI tool rewrites the open document, Elvandar Viewer waits briefly for the file’s
        size and modification time to settle. It then reloads the page and can briefly highlight
        changed paragraphs.</p>
        <h2>Revisit every changed paragraph</h2>
        <p>An amber <b>N CHANGES</b> control appears above a rendered page after a live rewrite.
        Use its arrows—or <span class="key">⌘⌥↑</span> and <span class="key">⌘⌥↓</span>—to move
        backward and forward through the revised paragraphs. Navigation wraps at either end and
        begins near your current reading position.</p>
        <table class="status-table">
          <tr><td><span class="status watching">● WATCHING</span></td><td>The live file is stable and observed.</td></tr>
          <tr><td><span class="status updated">● UPDATED</span></td><td>A stable change was just rendered.</td></tr>
          <tr><td><span class="status waiting">● WAITING</span></td><td>The file is temporarily missing or still being replaced.</td></tr>
          <tr><td><span class="status snapshot">● SNAPSHOT</span></td><td>You are reading immutable committed content.</td></tr>
        </table>
        <h2>If a page looks incomplete</h2>
        <p>Give the writer a moment to finish. WAITING should return to WATCHING automatically;
        no refresh button or file intervention is required.</p>
        """,
    ),
    HelpTopic(
        "git",
        "Working trees and committed views",
        "GIT, QUIETLY",
        "Git powers the library, but reading never requires source-control work.",
        """
        <h2>Working tree</h2>
        <p>The live files currently being edited. Uncommitted changes appear here immediately and
        continue updating through filesystem notifications.</p>
        <h2>Committed view</h2>
        <p>An immutable branch or commit snapshot read directly through Git objects. It is useful
        for asking “what was committed?” without checking anything out.</p>
        <h2>Worktrees</h2>
        <p>Selecting a worktree changes only which folder the viewer observes. It does not run
        <code>git checkout</code>, move a branch, or alter another tool’s working directory.</p>
        <div class="note"><b>Working tree</b> means live and potentially unfinished.
        <b>Committed</b> means recorded and immutable. Neither is automatically “better”; choose
        the one that answers the question you are asking.</div>
        """,
    ),
    HelpTopic(
        "safety",
        "The read-only promise",
        "SAFETY",
        "The application is a visualization layer, never a participant in authorship.",
        """
        <div class="covenant"><b>Repository contents are never modified.</b><br>
        Reading position and preferences are stored in macOS application settings, outside the
        repository.</div>
        <h2>Elvandar Viewer can</h2>
        <ul>
          <li>Read working files and committed Git objects.</li>
          <li>Watch filesystem notifications.</li>
          <li>Calculate diffs and build a local search index in memory.</li>
          <li>Remember local interface preferences and reading positions.</li>
        </ul>
        <h2>Elvandar Viewer will never</h2>
        <ul>
          <li>Edit Markdown, images, lore, or chapter files.</li>
          <li>Commit, merge, push, pull, rebase, or check out.</li>
          <li>Lock repository files or expect exclusive access.</li>
          <li>Generate prose or create a competing source of truth.</li>
        </ul>
        """,
    ),
    HelpTopic(
        "shortcuts",
        "Keyboard shortcuts",
        "QUICK REFERENCE",
        "The complete set of reader controls available from the keyboard.",
        """
        <table class="shortcut-table">
          <tr><td><span class="key">⌘F</span></td><td>Search the library</td></tr>
          <tr><td><span class="key">⌘[</span> <span class="key">⌘]</span></td><td>Back and Forward</td></tr>
          <tr><td><span class="key">⌘⌥↑</span> <span class="key">⌘⌥↓</span></td><td>Previous and next changed paragraph</td></tr>
          <tr><td><span class="key">⌘1</span> <span class="key">⌘2</span> <span class="key">⌘3</span></td><td>Rendered, Raw, and Diff</td></tr>
          <tr><td><span class="key">⌘+</span> <span class="key">⌘−</span></td><td>Increase or decrease document text size</td></tr>
          <tr><td><span class="key">⌘0</span></td><td>Restore the default text size</td></tr>
          <tr><td><span class="key">⌘⇧O</span></td><td>Open the current document outline</td></tr>
          <tr><td><span class="key">⌘⇧R</span></td><td>Toggle Reading Mode</td></tr>
          <tr><td><span class="key">⌘,</span></td><td>Open Settings</td></tr>
          <tr><td><span class="key">⌘?</span></td><td>Open this Reader’s Guide</td></tr>
          <tr><td><span class="key">Esc</span></td><td>Clear search or leave Reading Mode</td></tr>
        </table>
        """,
    ),
)

HELP_TOPIC_BY_KEY = {topic.key: topic for topic in HELP_TOPICS}
HELP_NAVIGATION_TITLES = {
    "welcome": "Welcome",
    "git": "Git views",
    "safety": "Read-only safety",
}


def help_topic_document(topic: HelpTopic, night_mode: bool) -> str:
    palette = (
        {
            "background": "#191C21",
            "text": "#D7DBE4",
            "heading": "#F1F3F6",
            "muted": "#A1A8B4",
            "panel": "#22262D",
            "border": "#3A414C",
            "accent": "#8FB5E6",
            "gold": "#D2AC69",
            "key": "#2B3543",
            "code": "#202832",
        }
        if night_mode
        else {
            "background": "#FCFCFD",
            "text": "#303641",
            "heading": "#1D222C",
            "muted": "#69717F",
            "panel": "#F4F5F7",
            "border": "#D9DDE3",
            "accent": "#315D9B",
            "gold": "#9A6B22",
            "key": "#E8EDF4",
            "code": "#EEF1F5",
        }
    )
    return """<!doctype html><html><head><meta charset="utf-8"><style>
    body { margin: 0; padding: 38px 44px 54px; background: %(background)s; color: %(text)s;
      font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
      font-size: 15px; line-height: 1.62; }
    .eyebrow { color: %(gold)s; font-size: 10px; font-weight: 700; letter-spacing: 1.5px;
      margin-bottom: 8px; }
    h1 { color: %(heading)s; font-family: Georgia, "Times New Roman", serif; font-size: 30px;
      font-weight: 600; margin: 0 0 8px; }
    .summary { color: %(muted)s; font-size: 15px; margin: 0 0 30px; }
    h2 { color: %(heading)s; font-family: Georgia, "Times New Roman", serif; font-size: 19px;
      font-weight: 600; margin: 30px 0 8px; }
    p { margin: 7px 0 13px; } li { margin: 6px 0; } ul, ol { margin: 8px 0 16px; }
    .covenant { background: %(panel)s; border: 1px solid %(border)s; border-left: 4px solid %(gold)s;
      border-radius: 7px; padding: 15px 18px; margin: 4px 0 28px; }
    .note { background: %(panel)s; border: 1px solid %(border)s; border-radius: 7px;
      padding: 14px 17px; margin-top: 24px; }
    table { width: 100%%; border-collapse: collapse; margin: 12px 0 22px; }
    td { border-bottom: 1px solid %(border)s; padding: 11px 9px; vertical-align: top; }
    td:first-child { width: 29%%; color: %(heading)s; }
    .status-table td:first-child { width: 34%%; }
    .shortcut-table td:first-child { width: 42%%; white-space: nowrap; }
    .key, code { color: %(heading)s; background: %(key)s; border: 1px solid %(border)s;
      border-radius: 4px; padding: 2px 6px; font-family: "SF Mono", Menlo, monospace;
      font-size: 12px; }
    code { background: %(code)s; }
    .status { font-size: 11px; font-weight: 700; letter-spacing: .3px; }
    .watching { color: #63A276; } .updated { color: %(gold)s; }
    .waiting { color: #C88963; } .snapshot { color: %(accent)s; }
    b { color: %(heading)s; }
    </style></head><body><div class="eyebrow">%(eyebrow)s</div><h1>%(title)s</h1>
    <p class="summary">%(summary)s</p>%(body)s</body></html>""" % {
        **palette,
        "eyebrow": topic.eyebrow,
        "title": topic.title,
        "summary": topic.summary,
        "body": topic.body,
    }


class HelpDialog(QDialog):
    def __init__(self, night_mode: bool, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.night_mode = night_mode
        self.setObjectName("helpDialog")
        self.setWindowTitle("Elvandar Viewer Help")
        self.setWindowModality(Qt.WindowModality.NonModal)
        self.resize(900, 680)
        self.setMinimumSize(720, 520)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        header = QFrame(objectName="helpHeader")
        header_layout = QVBoxLayout(header)
        header_layout.setContentsMargins(26, 20, 26, 18)
        header_layout.setSpacing(3)
        header_layout.addWidget(QLabel("ELVANDAR VIEWER", objectName="helpEyebrow"))
        header_layout.addWidget(QLabel("Reader’s Guide", objectName="helpTitle"))
        header_layout.addWidget(
            QLabel(
                "Read comfortably. Follow the work. Leave the repository untouched.",
                objectName="helpSubtitle",
            )
        )
        layout.addWidget(header)

        body = QFrame(objectName="helpBody")
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        self.topic_list = QListWidget(objectName="helpTopicList")
        self.topic_list.setAccessibleName("Help topics")
        self.topic_list.setFixedWidth(210)
        self.topic_list.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        for topic in HELP_TOPICS:
            item = QListWidgetItem(HELP_NAVIGATION_TITLES.get(topic.key, topic.title))
            item.setData(Qt.ItemDataRole.UserRole, topic.key)
            item.setToolTip(topic.summary)
            self.topic_list.addItem(item)
        self.topic_list.currentRowChanged.connect(self._show_row)
        body_layout.addWidget(self.topic_list)

        self.content = QTextBrowser(objectName="helpContent")
        self.content.setAccessibleName("Help article")
        self.content.setOpenExternalLinks(True)
        body_layout.addWidget(self.content, 1)
        layout.addWidget(body, 1)

        self._close_shortcut = QShortcut(QKeySequence(Qt.Key.Key_Escape), self)
        self._close_shortcut.activated.connect(self.close)
        self.open_topic("welcome")

    @property
    def current_topic_key(self) -> str:
        item = self.topic_list.currentItem()
        return str(item.data(Qt.ItemDataRole.UserRole)) if item is not None else "welcome"

    def open_topic(self, key: str) -> None:
        selected = key if key in HELP_TOPIC_BY_KEY else "welcome"
        for row in range(self.topic_list.count()):
            item = self.topic_list.item(row)
            if item.data(Qt.ItemDataRole.UserRole) == selected:
                self.topic_list.setCurrentRow(row)
                return

    def set_night_mode(self, enabled: bool) -> None:
        if self.night_mode == enabled:
            return
        self.night_mode = enabled
        self._render_topic(self.current_topic_key)

    def _show_row(self, row: int) -> None:
        if row < 0:
            return
        key = str(self.topic_list.item(row).data(Qt.ItemDataRole.UserRole))
        self._render_topic(key)

    def _render_topic(self, key: str) -> None:
        topic = HELP_TOPIC_BY_KEY.get(key, HELP_TOPIC_BY_KEY["welcome"])
        self.content.setHtml(help_topic_document(topic, self.night_mode))
        self.content.verticalScrollBar().setValue(0)
