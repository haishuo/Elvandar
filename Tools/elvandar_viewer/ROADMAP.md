# Elvandar Viewer Roadmap

This is a prioritized list of optional product ideas, not a delivery promise. Elvandar Viewer
remains a read-only reading application: a feature that turns it into an editor, IDE, or Git
client does not belong here.

When a feature ships, remove it from this file and document the finished behavior in
[USER_GUIDE.md](USER_GUIDE.md) and the implemented list in [README.md](README.md). Revisit the
ordering after each release rather than treating old priorities as permanent.

## Priority 1 — make everyday reading easier

These offer the most value during normal chapter-reading sessions.

- [ ] **Recently Viewed and Favorites.** Provide a small reader-oriented way to return to active
  chapters and frequently consulted canon without reproducing the folder hierarchy.
- [ ] **Session continuity polish.** Restore the current branch snapshot, selected reader view,
  and search state where that behavior remains predictable rather than surprising. The last open
  page, reading position, and synchronized Library/Contents selections already persist.

## Priority 2 — connect the private wiki

These make the repository's existing structure easier to understand without inventing new canon.

- [ ] **Backlinks.** Show which documents link to the current character, location, event, or
  chapter.
- [ ] **Character browser.** Build a focused visual index from existing character sheets, with no
  separate database to drift away from the Markdown.
- [ ] **Chapter statistics.** Show word count, estimated reading time, heading/scene structure,
  and change size as unobtrusive reading metadata.
- [ ] **Reading progress.** Track local, optional progress through books and chapters without
  writing progress markers into the repository.
- [ ] **Royal Road preview.** Present the generated Royal Road output as it will read on the site,
  while preserving `Royal Road/` as generated, read-only content.

## Priority 3 — visual ways to explore canon

These are valuable but require stronger conventions or metadata to avoid unreliable inference.

- [ ] **Map library and viewer.** Add map-specific browsing, full-screen inspection, pins, and
  links to relevant place pages.
- [ ] **Timeline visualization.** Render events from the authoritative timeline files across books
  and historical eras.
- [ ] **Relationship graph.** Explore links among characters, places, factions, and events while
  clearly distinguishing explicit repository links from inferred relationships.

## Priority 4 — advanced and longer-term options

- [ ] **Compare arbitrary revisions.** Allow read-only comparison of two branches or commits
  without checking either one out.
- [ ] **Local semantic search.** Add optional meaning-based search with an explicit privacy model,
  predictable indexing, and ordinary text search as the dependable default.
- [ ] **Cross-platform packaging.** Package and test Windows and Linux builds after the macOS
  experience is stable.
- [ ] **Accessible reading audit.** Validate keyboard-only navigation, VoiceOver labels, contrast,
  focus order, and scalable typography across every view.

## Explicitly out of scope

- Editing Markdown or repository files
- Commit, merge, push, pull, rebase, or checkout operations
- Automatic prose or canon generation
- Any index or metadata store that becomes a competing source of truth
