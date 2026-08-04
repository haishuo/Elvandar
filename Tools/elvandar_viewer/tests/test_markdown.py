from pathlib import Path

from PySide6.QtGui import QTextDocument
from PySide6.QtWidgets import QApplication

from elvandar_viewer.markdown import MarkdownRenderer


def test_renders_gfm_table_task_and_footnote(tmp_path: Path) -> None:
    source = "| Name | Role |\n| --- | --- |\n| Xion | Healer |\n\n- [x] Read\n\nNote[^1]\n\n[^1]: Detail"

    rendered = MarkdownRenderer().render(source, tmp_path / "page.md")

    assert "<table>" in rendered
    assert 'type="checkbox"' in rendered
    assert 'class="footnotes"' in rendered


def test_local_image_is_resolved_from_document_folder(tmp_path: Path) -> None:
    rendered = MarkdownRenderer().render("![Map](<images/map one.png>)", tmp_path / "page.md")

    assert "file://" in rendered
    assert "map%20one.png" in rendered


def test_night_mode_uses_a_dark_reading_palette(tmp_path: Path) -> None:
    rendered = MarkdownRenderer(night_mode=True).render("# Night reading", tmp_path / "page.md")

    assert "color-scheme: dark" in rendered
    assert "color: #D8DBE2" in rendered
    assert "color: #F2F3F5" in rendered


def test_custom_text_size_applies_to_rendered_and_raw_markdown(tmp_path: Path) -> None:
    renderer = MarkdownRenderer(font_size=24)

    rendered = renderer.render("Larger prose", tmp_path / "page.md")
    raw = renderer.raw("Larger source")

    assert "font-size: 24px" in rendered
    assert "font-size: 19px" in raw


def test_document_roles_scale_proportionally_with_text_size(tmp_path: Path) -> None:
    _application = QApplication.instance() or QApplication([])
    source = """## Section Heading

### Detail Heading

Body copy with `inline code`.

> Quoted copy.

- List item

| Column |
| --- |
| Cell |

Note[^1]

[^1]: Footnote copy
"""
    document = QTextDocument()
    document.setHtml(MarkdownRenderer(font_size=30).render(source, tmp_path / "page.md"))

    expected_pixel_sizes = {
        "Section Heading": 45,
        "Detail Heading": 35,
        "Body copy": 30,
        "inline code": 25,
        "Quoted copy": 30,
        "List item": 30,
        "Column": 21,
        "Cell": 25,
        "Footnote copy": 25,
    }
    for text, expected in expected_pixel_sizes.items():
        assert document.find(text).charFormat().font().pixelSize() == expected
