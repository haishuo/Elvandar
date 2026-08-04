from __future__ import annotations

import html
import re
from pathlib import Path
from collections.abc import Callable
from urllib.parse import quote, unquote

from markdown_it import MarkdownIt
from mdit_py_plugins.footnote import footnote_plugin
from mdit_py_plugins.tasklists import tasklists_plugin


_IMAGE_SOURCE = re.compile(r'(<img\s+[^>]*src=["\'])([^"\']+)(["\'])', re.IGNORECASE)
_IMAGE_TAG = re.compile(r"<img\s+[^>]*>", re.IGNORECASE)
ImageResolver = Callable[[str, Path], str]


class MarkdownRenderer:
    def __init__(self, night_mode: bool = False, font_size: int = 18) -> None:
        self.night_mode = night_mode
        self.font_size = font_size
        self._markdown = (
            MarkdownIt("commonmark", {"html": False, "linkify": True, "typographer": True})
            .enable(["table", "strikethrough"])
            .use(footnote_plugin)
            .use(tasklists_plugin, enabled=False)
        )

    def render(
        self, source: str, document_path: Path, image_resolver: ImageResolver | None = None
    ) -> str:
        rendered = self.render_fragment(source, document_path, image_resolver)
        return self._document(rendered)

    def render_fragment(
        self, source: str, document_path: Path, image_resolver: ImageResolver | None = None
    ) -> str:
        rendered = self._markdown.render(source)
        return self._resolve_images(rendered, document_path.parent, image_resolver)

    def raw(self, source: str) -> str:
        return self._document(f'<pre class="raw-markdown">{html.escape(source)}</pre>', raw=True)

    @staticmethod
    def _resolve_images(
        rendered: str, parent: Path, image_resolver: ImageResolver | None = None
    ) -> str:
        def replace_tag(tag_match: re.Match[str]) -> str:
            tag = tag_match.group(0)
            source_match = _IMAGE_SOURCE.search(tag)
            if source_match is None:
                return tag
            source = source_match.group(2)
            if "://" in source or source.startswith(("data:", "file:")):
                return tag
            decoded = unquote(source)
            if image_resolver is not None:
                resolved = image_resolver(decoded, parent)
            else:
                local = (parent / decoded).resolve(strict=False)
                resolved = "file://" + quote(str(local))
            start, end = source_match.span(2)
            resolved_tag = tag[:start] + resolved + tag[end:]
            href = "elvandar-image:" + quote(decoded, safe="")
            return f'<a href="{href}">{resolved_tag}</a>'

        return _IMAGE_TAG.sub(replace_tag, rendered)

    def _document(self, body: str, *, raw: bool = False) -> str:
        body_class = "raw" if raw else "rendered"
        palette = (
            {
                "scheme": "dark",
                "text": "#D8DBE2",
                "heading": "#F2F3F5",
                "link": "#8FB5E6",
                "link_decoration": "#536D8F",
                "quote": "#AFB5C0",
                "quote_border": "#B58A43",
                "rule": "#555C67",
                "table_border": "#414650",
                "table_heading": "#AEB5C0",
                "code": "#282C33",
                "pre": "#22262C",
                "footnote": "#A0A7B3",
            }
            if self.night_mode
            else {
                "scheme": "light",
                "text": "#252932",
                "heading": "#171B24",
                "link": "#315D9B",
                "link_decoration": "#A8BBD5",
                "quote": "#525968",
                "quote_border": "#B58A43",
                "rule": "#AEB4BF",
                "table_border": "#D9DCE2",
                "table_heading": "#555E6D",
                "code": "#EDEFF3",
                "pre": "#F0F2F5",
                "footnote": "#626A78",
            }
        )
        palette.update(
            {
                "body": body,
                "body_class": body_class,
                "font_size": str(self.font_size),
                "raw_font_size": str(max(11, self.font_size - 5)),
            }
        )
        return """<!doctype html>
<html><head><meta charset="utf-8"><style>
:root { color-scheme: %(scheme)s; }
* { box-sizing: border-box; }
body {
  margin: 0 auto; padding: 58px 68px 96px; max-width: 820px;
  color: %(text)s; background: transparent;
  font-family: "Iowan Old Style", "Palatino Linotype", Palatino, serif;
  font-size: %(font_size)spx; line-height: 1.72; text-rendering: optimizeLegibility;
}
h1, h2, h3, h4 { color: %(heading)s; line-height: 1.2; margin: 2.1em 0 .7em; }
h1 { font-size: 2.25em; font-weight: 600; letter-spacing: -.025em; margin-top: 0; }
h2 { font-size: 1.5em; font-weight: 600; }
h3 { font-size: 1.16em; font-weight: 650; }
p { margin: 0 0 1.15em; }
a { color: %(link)s; text-decoration-color: %(link_decoration)s; text-underline-offset: 3px; }
blockquote { margin: 1.8em 0; padding: .15em 0 .15em 1.25em; border-left: 2px solid %(quote_border)s; color: %(quote)s; }
hr { border: 0; width: 48px; margin: 3em auto; border-top: 1px solid %(rule)s; }
img { display: block; max-width: 100%%; max-height: 72vh; margin: 2em auto; border-radius: 7px; }
table { border-collapse: collapse; width: 100%%; margin: 1.5em 0 2em; font-family: -apple-system, BlinkMacSystemFont, sans-serif; font-size: .82em; }
th, td { border-bottom: 1px solid %(table_border)s; padding: .7em .75em; text-align: left; vertical-align: top; }
th { color: %(table_heading)s; font-size: .84em; letter-spacing: .035em; text-transform: uppercase; }
code { border-radius: 4px; background: %(code)s; padding: .12em .32em; font-family: "SFMono-Regular", Menlo, monospace; font-size: .82em; }
pre { overflow-x: auto; padding: 1.25em; border: 1px solid %(table_border)s; border-radius: 7px; background: %(pre)s; line-height: 1.55; }
pre code { padding: 0; background: transparent; }
.task-list-item { list-style: none; }
.footnotes { color: %(footnote)s; font-size: .82em; }
.raw-markdown { white-space: pre-wrap; word-break: normal; font-size: %(raw_font_size)spx; }
</style></head><body class="%(body_class)s">%(body)s</body></html>""" % palette
