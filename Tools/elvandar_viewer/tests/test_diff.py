from pathlib import Path

from elvandar_viewer.diff import DiffRenderer, DiffVersions, build_diff_rows, split_markdown_blocks
from elvandar_viewer.markdown import MarkdownRenderer


def test_markdown_blocks_keep_fenced_code_together() -> None:
    source = "Before\n\n```python\nfirst = 1\n\nsecond = 2\n```\n\nAfter"

    blocks = split_markdown_blocks(source)

    assert blocks == ["Before", "```python\nfirst = 1\n\nsecond = 2\n```", "After"]


def test_diff_groups_replacement_and_collapses_unchanged_context() -> None:
    before = "\n\n".join(["Zero", "One", "Two", "Three", "Old", "Five", "Six", "Seven", "Eight"])
    after = "\n\n".join(["Zero", "One", "Two", "Three", "New", "Five", "Six", "Seven", "Eight"])

    rows = build_diff_rows(before, after, context=1)

    assert any(row.kind == "replace" and row.before == "Old" and row.after == "New" for row in rows)
    assert sum(row.collapsed_count for row in rows if row.kind == "collapsed") == 4


def test_rendered_diff_has_two_labeled_sides_and_change_colors(tmp_path: Path) -> None:
    versions = DiffVersions("Old paragraph", "New paragraph", "HEAD", "Working tree")

    rendered = DiffRenderer(MarkdownRenderer()).render(versions, tmp_path / "chapter.md")

    assert "HEAD" in rendered
    assert "Working tree" in rendered
    assert 'class="removed"' in rendered
    assert 'class="added"' in rendered


def test_identical_documents_get_clear_empty_state(tmp_path: Path) -> None:
    versions = DiffVersions("Same", "Same", "Before", "After")

    rendered = DiffRenderer(MarkdownRenderer()).render(versions, tmp_path / "chapter.md")

    assert "No differences" in rendered


def test_night_mode_diff_uses_dark_added_and_removed_cells(tmp_path: Path) -> None:
    versions = DiffVersions("Old paragraph", "New paragraph", "HEAD", "Working tree")

    rendered = DiffRenderer(MarkdownRenderer(night_mode=True)).render(
        versions, tmp_path / "chapter.md"
    )

    assert "background: #39282B" in rendered
    assert "background: #26372D" in rendered


def test_diff_respects_the_document_text_size(tmp_path: Path) -> None:
    versions = DiffVersions("Old paragraph", "New paragraph", "HEAD", "Working tree")

    rendered = DiffRenderer(MarkdownRenderer(font_size=24)).render(
        versions, tmp_path / "chapter.md"
    )

    assert "font-size: 22px" in rendered
