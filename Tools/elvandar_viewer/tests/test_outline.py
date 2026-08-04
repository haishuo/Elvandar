from elvandar_viewer.outline import add_outline_anchors, document_outline


def test_document_outline_collects_headings_and_scene_breaks_in_order() -> None:
    source = """# Opening **Movement**

## The First Question

---

Second movement
---------------

```markdown
# Not a real heading
---
```
"""

    entries = document_outline(source)

    assert [(entry.kind, entry.title, entry.level, entry.line) for entry in entries] == [
        ("heading", "Opening Movement", 1, 0),
        ("heading", "The First Question", 2, 2),
        ("scene", "Scene 1", 0, 4),
        ("heading", "Second movement", 2, 6),
    ]
    assert [entry.anchor for entry in entries] == [
        "elvandar-section-0",
        "elvandar-section-1",
        "elvandar-section-2",
        "elvandar-section-3",
    ]


def test_rendered_outline_targets_receive_matching_named_anchors() -> None:
    rendered = "<h1>Opening</h1>\n<p>Text</p>\n<hr>\n<h3>Return</h3>\n"

    anchored = add_outline_anchors(rendered)

    assert anchored.index('name="elvandar-section-0"') < anchored.index("<h1>")
    assert anchored.index('name="elvandar-section-1"') < anchored.index("<hr>")
    assert anchored.index('name="elvandar-section-2"') < anchored.index("<h3>")
