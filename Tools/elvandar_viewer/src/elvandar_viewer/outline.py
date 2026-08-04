from __future__ import annotations

import html
import re
from dataclasses import dataclass
from typing import Literal

from markdown_it import MarkdownIt


OUTLINE_ANCHOR_PREFIX = "elvandar-section-"
_HTML_TAG = re.compile(r"<[^>]+>")
_OUTLINE_TARGET = re.compile(
    r"<h[1-6](?:\s[^>]*)?>.*?</h[1-6]>|<hr\s*/?>",
    re.IGNORECASE | re.DOTALL,
)


@dataclass(frozen=True)
class OutlineEntry:
    kind: Literal["heading", "scene"]
    title: str
    anchor: str
    line: int
    level: int = 0
    scene_number: int = 0


def outline_anchor(index: int) -> str:
    return f"{OUTLINE_ANCHOR_PREFIX}{index}"


def document_outline(source: str) -> list[OutlineEntry]:
    """Return the headings and manuscript scene breaks in source order."""

    markdown = MarkdownIt("commonmark", {"html": False})
    tokens = markdown.parse(source)
    entries: list[OutlineEntry] = []
    scene_number = 0

    for index, token in enumerate(tokens):
        line = token.map[0] if token.map else 0
        if token.type == "heading_open":
            inline = tokens[index + 1] if index + 1 < len(tokens) else None
            raw_title = inline.content if inline is not None and inline.type == "inline" else ""
            rendered_title = markdown.renderInline(raw_title)
            title = html.unescape(_HTML_TAG.sub("", rendered_title)).strip() or "Untitled section"
            entries.append(
                OutlineEntry(
                    kind="heading",
                    title=title,
                    anchor=outline_anchor(len(entries)),
                    line=line,
                    level=int(token.tag[1:]),
                )
            )
        elif token.type == "hr":
            scene_number += 1
            entries.append(
                OutlineEntry(
                    kind="scene",
                    title=f"Scene {scene_number}",
                    anchor=outline_anchor(len(entries)),
                    line=line,
                    scene_number=scene_number,
                )
            )
    return entries


def add_outline_anchors(rendered: str) -> str:
    """Attach stable named anchors to rendered headings and scene breaks."""

    index = 0

    def add_anchor(match: re.Match[str]) -> str:
        nonlocal index
        anchor = outline_anchor(index)
        index += 1
        return f'<a name="{anchor}"></a>{match.group(0)}'

    return _OUTLINE_TARGET.sub(add_anchor, rendered)
