# Elvandar Viewer

A read-only macOS desktop reader for the Elvandar Git repository. The viewer
never writes to the repository; Claude remains the author and Git remains the
source of truth.

## Open the macOS application

Double-click `Elvandar Viewer.app`. On this Mac it finds the Elvandar repository
automatically. If the repository moves, the app asks for its new folder and
remembers that choice outside the repository.

## Implemented

- Four-pane reading interface
- Folder and document navigation
- GitHub-flavoured Markdown rendering
- Inline local images and clickable links
- Raw Markdown view
- Repository-bound path validation
- Native filesystem notifications (no one-second polling loop)
- Debounced live document reloads
- Recovery after atomic saves and temporary file replacement
- Paragraph-level change highlights with a gentle fade
- Automatic folder-tree updates when files are added, renamed, or removed
- Current branch and read-only branch snapshot selector
- Clickable read-only worktree switching with independent live watchers
- Working-tree change list with document shortcuts
- Recent commit history for the selected view
- Event-driven Git metadata refresh
- Virtual branch reading through Git objects, with no checkout or index writes
- Semantic side-by-side Markdown diff reader
- Paired red/green paragraph changes with aligned blocks
- Collapsed unchanged context for long documents
- Working-tree, untracked, deleted-file, and committed-snapshot comparisons
- Clear no-differences state
- Instant global title, path, and document search
- Relevance ranking with contextual excerpts
- Multi-term matching and in-document highlights
- `Command-F`, Return, and Escape keyboard controls
- Live search-index updates as repository files change
- Batched branch-snapshot indexing through Git objects
- First-class PNG, JPEG, GIF, WebP, BMP, TIFF, and SVG browsing
- Dedicated image previews in the reading pane
- Separate zoom-and-pan inspection windows
- Fit, 100%, wheel zoom, keyboard zoom, and drag navigation
- Click-to-open inline Markdown images
- Revision-correct inline images in committed branch snapshots
- Live image refresh when artwork changes
- Day, Night, and Match macOS appearance modes across every reader surface
- Native `Elvandar Viewer → Settings…` menu with reading and live-update preferences
- Distraction-free reading mode that hides every sidebar without losing reading position
- Configurable narrow, comfortable, and wide Reading Mode page widths
- Persistent 14–30px document text sizing for rendered prose, raw Markdown, and diffs
- `Command-Plus`, `Command-Minus`, and `Command-0` text-size controls
- `Command-Shift-R` Reading Mode shortcut
- Browser-style Back and Forward navigation with `Command-[` and `Command-]`
- Per-document, per-view reading-position restoration across launches

## Run locally

From this directory:

```bash
python3 -m venv .venv
.venv/bin/pip install -e .
.venv/bin/elvandar-viewer ../..
```

Or pass any other repository path as the first argument. When no path is
provided, the app looks upward from the current directory for a `.git` folder.

## Build the macOS application

```bash
.venv/bin/pip install -e '.[build]'
.venv/bin/python scripts/build_macos.py
```

The build creates `dist/Elvandar Viewer.app`, applies the project icon, and
ad-hoc signs the private local bundle. Distribution to other Macs would require
an Apple Developer ID signature and notarization.
