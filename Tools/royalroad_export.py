#!/usr/bin/env python3
"""
Generate Royal Road paste-ready HTML from chapter markdown.

For each `Book N - Title/Chapters/*.md`, writes `Book N - Title/Royal Road/*.html`,
and deletes any .html there that no longer has a chapter behind it — a renamed or
cut chapter otherwise leaves its old file sitting in a paste-ready folder looking
finished. Every deletion is named on stdout.

The output is a bare fragment — no <html>, <head>, or <body> — because Royal Road's
chapter editor takes body content only. Paste the whole file into the HTML view.

Conventions (derived from the author's existing Royal Road posts):
  - every paragraph becomes a single <p>...</p> on its own line
  - the `---` scene break becomes a literal <p>---</p>
  - typographic characters become named entities, so nothing depends on the
    editor guessing an encoding:
        —  &mdash;      …  &hellip;
        “  &ldquo;      ”  &rdquo;      ’  &rsquo;      ‘  &lsquo;
  - emphasis becomes real tags: **bold** -> <strong>, *italic* -> <em>
    (see EMPHASIS_AS_TAGS below)

Usage:
    python3 Tools/royalroad_export.py              # every book
    python3 Tools/royalroad_export.py "Book 1"     # books matching a prefix
"""

import glob
import html
import os
import re
import sys

# Royal Road's editor does not interpret markdown, so a literal *word* posts as
# an asterisk-wrapped word. Tags are what actually render. Set this False only if
# you want the raw asterisks carried through untouched.
EMPHASIS_AS_TAGS = True

ENTITIES = {
    "—": "&mdash;",   # — em dash
    "…": "&hellip;",  # … ellipsis
    "“": "&ldquo;",   # " left double
    "”": "&rdquo;",   # " right double
    "‘": "&lsquo;",   # ' left single
    "’": "&rsquo;",   # ' right single
    "–": "&ndash;",   # – en dash
}

BOLD = re.compile(r"\*\*([^*\n]+)\*\*")
ITALIC = re.compile(r"(?<!\*)\*(?!\*)([^*\n]+)\*(?!\*)")
SCENE_BREAK = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")


def convert(md: str) -> str:
    """Markdown chapter body -> Royal Road HTML fragment."""
    lines = []
    for block in re.split(r"\n\s*\n", md.strip()):
        block = block.strip()
        if not block:
            continue

        if SCENE_BREAK.match(block):
            lines.append("<p>---</p>")
            continue

        # A paragraph may be soft-wrapped across source lines; join it up.
        text = " ".join(part.strip() for part in block.split("\n"))

        # Escape first, so any literal &, < or > in the prose stays literal and
        # cannot collide with the tags and entities added below.
        text = html.escape(text, quote=False)

        if EMPHASIS_AS_TAGS:
            text = BOLD.sub(r"<strong>\1</strong>", text)
            text = ITALIC.sub(r"<em>\1</em>", text)

        for char, entity in ENTITIES.items():
            text = text.replace(char, entity)

        lines.append(f"<p>{text}</p>")

    return "\n".join(lines) + "\n"


def prune(out_dir, written):
    """Delete .html in out_dir that this run did not write, and name each one.

    A chapter that is renamed or deleted leaves its old .html behind, and a stale
    file in a paste-ready folder is worse than a missing one: it looks finished.

    Files are matched by identity (device, inode) rather than by name, because on
    a case-insensitive filesystem a case-only rename means the name we wrote and
    the name on disk differ while the file is the same one — comparing names
    there would delete the output this run had just produced.
    """
    keep = set()
    for path in written:
        info = os.stat(path)
        keep.add((info.st_dev, info.st_ino))

    removed = []
    for name in sorted(os.listdir(out_dir)):
        path = os.path.join(out_dir, name)
        if not name.lower().endswith(".html") or not os.path.isfile(path):
            continue
        info = os.stat(path)
        if (info.st_dev, info.st_ino) in keep:
            continue
        os.remove(path)
        removed.append(name)
    return removed


def main(argv):
    prefix = argv[1] if len(argv) > 1 else ""
    books = sorted(
        d for d in glob.glob("Book * - */Chapters")
        if os.path.basename(os.path.dirname(d)).startswith(prefix)
    )
    if not books:
        sys.exit(f"No book chapter folders matched {prefix!r}")

    total = 0
    for chapters_dir in books:
        book = os.path.dirname(chapters_dir)
        sources = sorted(glob.glob(os.path.join(chapters_dir, "*.md")))
        if not sources:
            # No chapters is not authority to empty an existing Royal Road
            # folder — it is far likelier to mean the wrong directory.
            continue

        out_dir = os.path.join(book, "Royal Road")
        os.makedirs(out_dir, exist_ok=True)

        written = []
        for src in sources:
            stem = os.path.splitext(os.path.basename(src))[0]
            dest = os.path.join(out_dir, stem + ".html")
            with open(src, encoding="utf-8") as fh:
                body = convert(fh.read())
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(body)
            written.append(dest)
            total += 1

        print(f"{book}: {len(sources)} chapters -> {out_dir}/")
        for name in prune(out_dir, written):
            print(f"  pruned stale output: {name}")

    print(f"Total: {total} files")


if __name__ == "__main__":
    main(sys.argv)
