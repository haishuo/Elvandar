from pathlib import Path

import pytest

from elvandar_viewer.repository import Repository, RepositoryBoundaryError, natural_sort_key


def test_repository_lists_supported_documents_and_folders(tmp_path: Path) -> None:
    (tmp_path / "Book 1").mkdir()
    (tmp_path / "Chapter.md").write_text("# Chapter", encoding="utf-8")
    (tmp_path / "cover.png").write_bytes(b"not an image")
    (tmp_path / ".git").mkdir()

    repository = Repository.open(tmp_path)

    assert [item.name for item in repository.contents(tmp_path)] == ["Book 1", "Chapter.md", "cover.png"]
    assert repository.read_binary(tmp_path / "cover.png") == b"not an image"


def test_repository_refuses_paths_outside_root(tmp_path: Path) -> None:
    root = tmp_path / "repository"
    root.mkdir()
    repository = Repository.open(root)

    with pytest.raises(RepositoryBoundaryError):
        repository.resolve(tmp_path / "elsewhere.md")


def test_read_text_replaces_incomplete_utf8(tmp_path: Path) -> None:
    document = tmp_path / "draft.md"
    document.write_bytes(b"A draft in progress: \xe2\x80")
    repository = Repository.open(tmp_path)

    assert repository.read_text(document).startswith("A draft in progress:")


def test_natural_sort_key_uses_reading_order_for_numbered_names() -> None:
    names = ["Chapter 20.md", "Chapter 3.md", "Chapter 10.md", "Chapter 2.md"]

    assert sorted(names, key=natural_sort_key) == [
        "Chapter 2.md",
        "Chapter 3.md",
        "Chapter 10.md",
        "Chapter 20.md",
    ]


def test_repository_contents_use_natural_reading_order(tmp_path: Path) -> None:
    for name in ("Chapter 10.md", "Chapter 2.md", "Chapter 1.md"):
        (tmp_path / name).write_text(name)

    repository = Repository.open(tmp_path)

    assert [path.name for path in repository.contents(tmp_path)] == [
        "Chapter 1.md",
        "Chapter 2.md",
        "Chapter 10.md",
    ]
