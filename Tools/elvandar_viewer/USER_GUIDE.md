# Elvandar Viewer User Guide

Elvandar Viewer is a read-only macOS application for comfortably watching the Elvandar
repository evolve. Claude or another writing tool remains the author; Git remains the source of
truth. The viewer never edits, commits, merges, pushes, pulls, or checks out repository content.

## Start here

1. Open **Elvandar Viewer** from `/Applications`.
2. Choose a folder in the Library sidebar.
3. Choose a document or image in Contents.
4. Read in the main pane. Changes made on disk appear automatically after the file becomes stable.

The app remembers the last open document and reading position for each worktree (or the selected
folder when no page is open). When it reopens a document, it also expands and selects that
document’s folder in Library and selects the document itself in Contents, so all three reading
panes resume together.

## The four panes

- **Library** browses the repository by folder and provides global search.
- **Contents** switches between the selected folder’s documents and the open page’s outline.
- **Reader** displays rendered Markdown, raw source, diffs, or image previews.
- **Repository** shows the current view, available worktrees, working changes, and recent commits.

Reading Mode hides the three sidebars without losing your place.

## Find and navigate

- Type in **Search Elvandar** to search titles, paths, and document text.
- Press **Return** to open the first search result.
- Use the back and forward buttons above the reader to revisit documents.
- Click a worktree in the Repository sidebar to view that working folder. This changes only what
  the app reads; it does not run `git checkout` or modify either worktree.
- Choose a committed branch snapshot from **Viewing** to read that revision through Git objects.
  Choose the working tree again to return to live files.

Each worktree keeps its own active document, navigation selection, layout, and reading position.

Numbered folders and files use natural reading order. For example, Chapter 2 appears before
Chapter 10 rather than following strict alphabetical order.

### Changed-page markers

The Library and Contents sidebars distinguish changed pages from ordinary navigation:

- A solid coral **●** and semibold title mean this version changed and has not yet been opened.
- A hollow blue **○** means the changed version has already been viewed.
- A marked folder contains changed pages. It inherits the strongest state below it, so one unseen
  chapter makes its Chapters and Book folders coral.

The legend at the bottom of Contents counts unseen and viewed changed pages. Opening a file marks
that exact version viewed; if Claude changes it again, it returns to unseen. The state is stored in
macOS application preferences outside the repository and remains separate for each worktree.

On a feature worktree, markers use the same complete Branch-vs-main comparison as Diff, including
committed work. On `main`, they include the latest commit and current working changes. An unseen
version remains marked across later commits until it is opened. Immutable committed snapshots do
not show activity markers.

## Document outline

Choose **Page** in the Contents sidebar to see the current document’s headings and scene breaks.
Heading indentation follows the Markdown hierarchy; scene breaks use gold manuscript-style passage
markers. The selected outline entry follows your reading position as you scroll.

Click an entry to jump instantly. In Rendered view it lands on the visible section; in Raw view it
lands on the corresponding Markdown line. Choosing an outline entry from Diff returns to Rendered
view because paired diff rows do not have one unambiguous document position.

The **Outline** button above the reader provides the same navigation as a compact menu, including in
Reading Mode when the sidebars are hidden. Press **Command-Shift-O** to focus the Page outline or
open that compact menu in Reading Mode.

## Reader views

- **Rendered** presents GitHub Flavored Markdown with reading typography, tables, links, images,
  task lists, code blocks, blockquotes, and footnotes.
- **Raw** displays the Markdown source without making it editable.
- **Diff** defaults to the complete feature-worktree change against its `main` merge base, including
  committed and uncommitted edits. Use its comparison menu to show only **Uncommitted** changes.
  On `main`, Diff compares the working document with `HEAD`; a committed snapshot is compared with
  its parent.
- **Reading** hides the sidebars and centers the page at the width selected in Settings.

Rendered and Raw share one document position. A simple round trip returns to the exact Rendered
position; intentionally scrolling in Raw transfers the new location back proportionally. Diff
retains its own position because its paired and collapsed structure does not map directly to the
source.

Click an inline image to open the image viewer. It supports zooming, panning, fitting the image,
and returning to 100% size.

## Live updates

The viewer uses filesystem notifications rather than a one-second polling loop. When an AI tool
rewrites a document, the app waits briefly for the file's size and modification time to settle.
It then reloads the page and can highlight changed paragraphs. If a file temporarily disappears
during an atomic save, the status changes to **WAITING** and recovers automatically.

After a rendered page changes, an amber **N CHANGES** control appears above the document. Its up
and down arrows jump to the previous or next revised paragraph and wrap at the beginning or end.
The first jump starts near the current reading position; the selected paragraph remains gently
highlighted after the initial live-update animation fades. The controls remain available until
the page changes again or another document opens.

The Repository sidebar uses these states:

- **WATCHING** — the active working-tree file is stable and being observed.
- **UPDATED** — a stable change was just rendered.
- **WAITING** — the file is temporarily unavailable or still being replaced.
- **SNAPSHOT** — the app is showing an immutable committed view rather than live files.

## Appearance and reading preferences

Open **Elvandar Viewer → Settings…** or press **Command-,**.

Settings include:

- Match macOS, Day, or Night appearance
- Reading Mode page width
- Default document text size
- Whether Reading Mode persists between launches
- Whether live paragraph changes are highlighted

Text Size scales the complete document hierarchy rather than body prose alone. Headings, lists,
blockquotes, tables, code, and footnotes retain their relative proportions at every supported size.

## Help

Open **Help → Elvandar Viewer Help** or press **Command-?** for the native Reader’s Guide. Its
topic index covers navigation, reader views, live-update states, Git terminology, the application’s
read-only guarantees, and keyboard shortcuts. The Help menu also links directly to the shortcut,
live-update, and safety sections.

Help follows the current Day, Night, or Match macOS appearance and remains open beside the reader
until you close it.

## Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| Command-F | Search the library |
| Command-[ | Back |
| Command-] | Forward |
| Command-Option-Up | Previous changed paragraph |
| Command-Option-Down | Next changed paragraph |
| Command-1 | Rendered view |
| Command-2 | Raw view |
| Command-3 | Diff view |
| Command-Plus | Increase document text size |
| Command-Minus | Decrease document text size |
| Command-0 | Restore the default text size |
| Command-Shift-O | Open the document outline |
| Command-Shift-R | Toggle Reading Mode |
| Command-, | Open Settings |
| Command-? | Open the Reader’s Guide |
| Escape | Clear search, or leave Reading Mode |

## If something looks wrong

- If an AI is in the middle of replacing a file, wait for **WAITING** to return to **WATCHING**.
- If a worktree has been removed outside the app, select an available worktree from the sidebar.
- If the repository has moved, relaunch the app and choose its new folder when prompted.
- If an older build is still running after an update, quit and reopen the app from `/Applications`.

Feature candidates and their current priority live in [ROADMAP.md](ROADMAP.md).
