from __future__ import annotations

import base64
import os
import subprocess
from pathlib import Path

from PySide6.QtGui import QImage

from elvandar_viewer.git import GitClient
from elvandar_viewer.markdown import MarkdownRenderer
from elvandar_viewer.repository import Repository
from elvandar_viewer.repository_view import RepositoryView


PNG = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNk+A8AAQUBAScY42YAAAAASUVORK5CYII="
)


def _git(root: Path, *arguments: str) -> None:
    environment = os.environ.copy()
    environment.update(
        {
            "GIT_AUTHOR_NAME": "Elvandar Test",
            "GIT_AUTHOR_EMAIL": "test@elvandar.invalid",
            "GIT_COMMITTER_NAME": "Elvandar Test",
            "GIT_COMMITTER_EMAIL": "test@elvandar.invalid",
        }
    )
    subprocess.run(
        ["git", "-C", str(root), *arguments],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=environment,
    )


def test_inline_images_are_resolved_and_clickable(tmp_path: Path) -> None:
    data_url = "data:image/png;base64," + base64.b64encode(PNG).decode("ascii")

    rendered = MarkdownRenderer().render(
        "![Map](maps/elvandar.png)",
        tmp_path / "page.md",
        lambda _source, _parent: data_url,
    )

    assert data_url in rendered
    assert 'href="elvandar-image:maps%2Felvandar.png"' in rendered


def test_branch_snapshot_reads_image_blob_without_extraction(tmp_path: Path) -> None:
    _git(tmp_path, "init", "-b", "main")
    image_path = tmp_path / "Maps" / "Elvandar.png"
    image_path.parent.mkdir()
    image_path.write_bytes(PNG)
    _git(tmp_path, "add", ".")
    _git(tmp_path, "commit", "-m", "Add map")
    image_path.unlink()

    view = RepositoryView(Repository.open(tmp_path), GitClient(tmp_path))
    view.show_revision("main")

    assert view.is_image(image_path)
    assert view.read_binary(image_path) == PNG
    assert not QImage.fromData(view.read_binary(image_path)).isNull()
