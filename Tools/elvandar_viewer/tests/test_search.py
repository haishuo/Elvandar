from pathlib import Path

from elvandar_viewer.git import GitClient
from elvandar_viewer.repository import Repository
from elvandar_viewer.repository_view import RepositoryView
from elvandar_viewer.search import SearchIndex


def _view(tmp_path: Path) -> RepositoryView:
    import subprocess

    subprocess.run(
        ["git", "-C", str(tmp_path), "init", "-b", "main"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return RepositoryView(Repository.open(tmp_path), GitClient(tmp_path))


def test_search_ranks_titles_and_requires_every_term(tmp_path: Path) -> None:
    people = tmp_path / "People"
    people.mkdir()
    (people / "Xion Kemvimore.md").write_text("A healer carrying Mira's wound.", encoding="utf-8")
    chapters = tmp_path / "Chapters"
    chapters.mkdir()
    (chapters / "Opening.md").write_text("Xion enters the room.", encoding="utf-8")
    view = _view(tmp_path)
    index = SearchIndex()
    index.rebuild(view)

    xion_results = index.search("Xion")
    specific_results = index.search("Mira wound")

    assert xion_results[0].title == "Xion Kemvimore"
    assert [result.title for result in specific_results] == ["Xion Kemvimore"]
    assert "Mira's wound" in specific_results[0].excerpt


def test_search_index_updates_one_changed_document(tmp_path: Path) -> None:
    document = tmp_path / "Places.md"
    document.write_text("Kaha'an", encoding="utf-8")
    view = _view(tmp_path)
    index = SearchIndex()
    index.rebuild(view)
    assert index.search("Lathion") == []

    document.write_text("Kaha'an and Lathion", encoding="utf-8")
    index.update(view, document)

    assert index.search("Lathion")[0].title == "Places"
