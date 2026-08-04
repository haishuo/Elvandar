from __future__ import annotations

import html
from dataclasses import dataclass
from difflib import SequenceMatcher
from pathlib import Path

from .markdown import ImageResolver, MarkdownRenderer


@dataclass(frozen=True, slots=True)
class DiffVersions:
    before: str
    after: str
    before_label: str
    after_label: str


@dataclass(frozen=True, slots=True)
class DiffRow:
    kind: str
    before: str = ""
    after: str = ""
    before_number: str = ""
    after_number: str = ""
    collapsed_count: int = 0


def split_markdown_blocks(source: str) -> list[str]:
    """Split Markdown into semantic blocks while preserving fenced code."""

    blocks: list[str] = []
    current: list[str] = []
    fence: str | None = None

    def flush() -> None:
        if current:
            block = "".join(current).strip()
            if block:
                blocks.append(block)
            current.clear()

    for line in source.splitlines(keepends=True):
        stripped = line.lstrip()
        if fence is not None:
            current.append(line)
            if stripped.startswith(fence):
                fence = None
                flush()
            continue

        marker = next((candidate for candidate in ("```", "~~~") if stripped.startswith(candidate)), None)
        if marker:
            flush()
            fence = marker
            current.append(line)
            continue

        if not line.strip():
            flush()
            continue

        if current and (stripped.startswith("#") or stripped.strip() == "---"):
            flush()
        current.append(line)
        if stripped.strip() == "---":
            flush()

    flush()
    return blocks


def build_diff_rows(before: str, after: str, context: int = 2) -> list[DiffRow]:
    old_blocks = split_markdown_blocks(before)
    new_blocks = split_markdown_blocks(after)
    matcher = SequenceMatcher(a=old_blocks, b=new_blocks, autojunk=False)
    rows: list[DiffRow] = []

    for operation, old_start, old_end, new_start, new_end in matcher.get_opcodes():
        old_slice = old_blocks[old_start:old_end]
        new_slice = new_blocks[new_start:new_end]
        if operation == "equal":
            if len(old_slice) > context * 2 + 1:
                for offset in range(context):
                    rows.append(
                        DiffRow(
                            "equal",
                            old_slice[offset],
                            new_slice[offset],
                            str(old_start + offset + 1),
                            str(new_start + offset + 1),
                        )
                    )
                rows.append(DiffRow("collapsed", collapsed_count=len(old_slice) - context * 2))
                for offset in range(len(old_slice) - context, len(old_slice)):
                    rows.append(
                        DiffRow(
                            "equal",
                            old_slice[offset],
                            new_slice[offset],
                            str(old_start + offset + 1),
                            str(new_start + offset + 1),
                        )
                    )
            else:
                for offset, block in enumerate(old_slice):
                    rows.append(
                        DiffRow(
                            "equal",
                            block,
                            new_slice[offset],
                            str(old_start + offset + 1),
                            str(new_start + offset + 1),
                        )
                    )
            continue

        before_number = _number_range(old_start, old_end)
        after_number = _number_range(new_start, new_end)
        rows.append(
            DiffRow(
                operation,
                "\n\n".join(old_slice),
                "\n\n".join(new_slice),
                before_number,
                after_number,
            )
        )
    return rows


class DiffRenderer:
    def __init__(self, markdown: MarkdownRenderer) -> None:
        self.markdown = markdown

    def render(
        self,
        versions: DiffVersions,
        document_path: Path,
        image_resolver: ImageResolver | None = None,
    ) -> str:
        rows = build_diff_rows(versions.before, versions.after)
        changed = any(row.kind not in {"equal", "collapsed"} for row in rows)
        before_label = html.escape(versions.before_label)
        after_label = html.escape(versions.after_label)

        if not changed:
            body = (
                '<div class="no-changes"><div class="check">✓</div>'
                "<h1>No differences</h1><p>This document is identical in both views.</p></div>"
            )
            return self._document(body, before_label, after_label)

        rendered_rows: list[str] = []
        for row in rows:
            if row.kind == "collapsed":
                rendered_rows.append(
                    f'<tr class="collapsed"><td colspan="2">{row.collapsed_count} unchanged paragraphs</td></tr>'
                )
                continue
            old_class = "removed" if row.kind in {"replace", "delete"} else "equal"
            new_class = "added" if row.kind in {"replace", "insert"} else "equal"
            before = self._cell(row.before, row.before_number, old_class, document_path, image_resolver)
            after = self._cell(row.after, row.after_number, new_class, document_path, image_resolver)
            rendered_rows.append(f'<tr class="diff-row">{before}{after}</tr>')

        body = '<table class="diff-table">' + "".join(rendered_rows) + "</table>"
        return self._document(body, before_label, after_label)

    def _cell(
        self,
        source: str,
        number: str,
        kind: str,
        document_path: Path,
        image_resolver: ImageResolver | None,
    ) -> str:
        if source:
            content = self.markdown.render_fragment(source, document_path, image_resolver)
        else:
            content = '<span class="empty">No text</span>'
        return (
            f'<td class="{kind}"><div class="block-number">{html.escape(number)}</div>'
            f'<div class="block-content">{content}</div></td>'
        )

    def _document(self, body: str, before_label: str, after_label: str) -> str:
        diff_font_size = max(13, self.markdown.font_size - 2)
        night_styles = ""
        if self.markdown.night_mode:
            night_styles = """
body { color: #D8DBE2; background: #1B1E23; }
.diff-header { background: #252A31; border-color: #3A404A; color: #A4ACB8; }
.diff-header td + td, .diff-table td + td { border-color: #3A404A; }
.diff-table td { border-bottom-color: #343A43; }
.block-number { color: #7E8795; }
.block-content h1, .block-content h2, .block-content h3 { color: #F0F2F5; }
.block-content th, .block-content td { border-bottom-color: #444B56; }
.block-content code { color: #DDE1E7; background: #30353D; }
.block-content pre { background: #24282F; border: 1px solid #414752; }
td.removed { background: #39282B; border-left-color: #B56870; }
td.added { background: #26372D; border-left-color: #609176; }
td.equal { background: #1D2025; }
.empty { color: #858E9B; }
.collapsed td { background: #262B32; color: #8F98A5; border-bottom-color: #3A404A; }
.no-changes { color: #A4ABB7; }
.no-changes .check { color: #82AF90; background: #263A2D; }
.no-changes h1 { color: #EEF0F3; }
"""
        return f"""<!doctype html><html><head><meta charset="utf-8"><style>
* {{ box-sizing: border-box; }}
body {{ margin: 0; padding: 0 0 80px; color: #252932; background: #F7F8FA;
  font-family: -apple-system, BlinkMacSystemFont, sans-serif; }}
.diff-header {{ width: 100%; border-collapse: collapse; table-layout: fixed; background: #F0F2F5;
  border-bottom: 1px solid #D7DAE0; color: #5D6572; font-size: 11px; font-weight: 650; }}
.diff-header td {{ width: 50%; padding: 12px 20px; letter-spacing: .055em; text-transform: uppercase; }}
.diff-header td + td {{ border-left: 1px solid #D7DAE0; }}
.diff-table {{ width: 100%; min-width: 680px; border-collapse: collapse; table-layout: fixed; }}
.diff-table td {{ width: 50%; vertical-align: top; border-bottom: 1px solid #E0E2E6; }}
.diff-table td + td {{ border-left: 1px solid #D7DAE0; }}
.block-number {{ padding: 8px 14px 0; color: #8A919D; font-size: 10px; font-family: Menlo, monospace; }}
.block-content {{ padding: 7px 18px 16px; font-family: "Iowan Old Style", Palatino, serif;
  font-size: {diff_font_size}px; line-height: 1.55; }}
.block-content p {{ margin: 0 0 .8em; }} .block-content p:last-child {{ margin-bottom: 0; }}
.block-content h1, .block-content h2, .block-content h3 {{ margin: 0 0 .6em; line-height: 1.25; }}
.block-content h1 {{ font-size: 1.55em; }} .block-content h2 {{ font-size: 1.3em; }}
.block-content img {{ max-width: 100%; }}
.block-content table {{ border-collapse: collapse; width: 100%; font-family: -apple-system, sans-serif; font-size: .8em; }}
.block-content th, .block-content td {{ border: 0; border-bottom: 1px solid #CCD1D8; padding: 5px; }}
.block-content th, .block-content td {{ width: auto; }}
.block-content pre {{ white-space: pre-wrap; font-family: Menlo, monospace; font-size: .76em; }}
td.removed {{ background: #FAECEC; border-left: 3px solid #C97878; }}
td.added {{ background: #EAF4ED; border-left: 3px solid #6E9B7B; }}
td.equal {{ background: #FCFCFD; }}
.empty {{ color: #A1A6AF; font-family: -apple-system, sans-serif; font-size: 12px; font-style: italic; }}
.collapsed td {{ width: 100%; padding: 9px; text-align: center; background: #EDF0F4; color: #7B8390;
  border-bottom: 1px solid #D7DAE0; font-size: 10px; letter-spacing: .04em; text-transform: uppercase; }}
.no-changes {{ max-width: 420px; margin: 120px auto; text-align: center; color: #68717F; }}
.no-changes .check {{ margin: 0 auto 18px; width: 38px; height: 38px; padding-top: 7px; border-radius: 19px;
  color: #477056; background: #E5EFE8; font-size: 18px; }}
.no-changes h1 {{ margin: 0 0 8px; color: #252932; font: 600 22px "Iowan Old Style", Palatino, serif; }}
.no-changes p {{ margin: 0; font-size: 13px; }}
{night_styles}
</style></head><body><table class="diff-header"><tr><td>{before_label}</td><td>{after_label}</td></tr></table>{body}</body></html>"""


def _number_range(start: int, end: int) -> str:
    if start == end:
        return ""
    if end - start == 1:
        return str(start + 1)
    return f"{start + 1}–{end}"
