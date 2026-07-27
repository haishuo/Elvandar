#!/usr/bin/env python3
"""
Generate Royal Road paste-ready HTML from chapter markdown.

For each `Book N - Title/Chapters/*.md`, writes `Book N - Title/Royal Road/*.html`.
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
            continue

        out_dir = os.path.join(book, "Royal Road")
        os.makedirs(out_dir, exist_ok=True)

        for src in sources:
            stem = os.path.splitext(os.path.basename(src))[0]
            dest = os.path.join(out_dir, stem + ".html")
            with open(src, encoding="utf-8") as fh:
                body = convert(fh.read())
            with open(dest, "w", encoding="utf-8") as fh:
                fh.write(body)
            total += 1

        print(f"{book}: {len(sources)} chapters -> {out_dir}/")

    print(f"Total: {total} files")


if __name__ == "__main__":
    main(sys.argv)
