from __future__ import annotations

from pathlib import Path, PurePosixPath

from .diff import DiffVersions
from .git import GitClient
from .repository import IMAGE_SUFFIXES, IGNORED_NAMES, SUPPORTED_SUFFIXES, VISIBLE_SUFFIXES, Repository


class RepositoryView:
    """A filesystem working tree or an immutable branch snapshot."""

    def __init__(self, working_tree: Repository, git: GitClient) -> None:
        self.working_tree = working_tree
        self.git = git
        self.root = working_tree.root
        self.revision: str | None = None
        self._files: set[PurePosixPath] = set()
        self._directories: set[PurePosixPath] = set()

    @property
    def is_working_tree(self) -> bool:
        return self.revision is None

    def show_working_tree(self) -> None:
        self.revision = None
        self._files.clear()
        self._directories.clear()

    def show_revision(self, revision: str) -> None:
        files = {path for path in self.git.list_files(revision) if self._visible(path)}
        directories: set[PurePosixPath] = {PurePosixPath(".")}
        for path in files:
            directories.update(path.parents)
        self.revision = revision
        self._files = files
        self._directories = directories

    def resolve(self, path: str | Path) -> Path:
        return self.working_tree.resolve(path)

    def relative(self, path: str | Path) -> Path:
        return self.working_tree.relative(path)

    def is_directory(self, path: str | Path) -> bool:
        if self.is_working_tree:
            return self.resolve(path).is_dir()
        return PurePosixPath(self.relative(path).as_posix()) in self._directories

    def is_file(self, path: str | Path) -> bool:
        if self.is_working_tree:
            return self.resolve(path).is_file()
        return PurePosixPath(self.relative(path).as_posix()) in self._files

    def is_image(self, path: str | Path) -> bool:
        return self.is_file(path) and self.resolve(path).suffix.casefold() in IMAGE_SUFFIXES

    def directories(self, parent: str | Path | None = None) -> list[Path]:
        if self.is_working_tree:
            return self.working_tree.directories(parent)
        relative_parent = PurePosixPath(self.relative(parent or self.root).as_posix())
        children = {
            directory
            for directory in self._directories
            if directory != relative_parent and directory.parent == relative_parent
        }
        return [self.root / Path(child.as_posix()) for child in sorted(children, key=lambda item: item.name.casefold())]

    def contents(self, folder: str | Path) -> list[Path]:
        if self.is_working_tree:
            return self.working_tree.contents(folder)
        relative_folder = PurePosixPath(self.relative(folder).as_posix())
        directories = [
            self.root / Path(item.as_posix())
            for item in self._directories
            if item != relative_folder and item.parent == relative_folder
        ]
        documents = [
            self.root / Path(item.as_posix())
            for item in self._files
            if item.parent == relative_folder and item.suffix.casefold() in VISIBLE_SUFFIXES
        ]
        return sorted(directories, key=lambda item: item.name.casefold()) + sorted(
            documents, key=lambda item: item.name.casefold()
        )

    def read_text(self, path: str | Path) -> str:
        if self.is_working_tree:
            return self.working_tree.read_text(path)
        relative = PurePosixPath(self.relative(path).as_posix())
        if relative.suffix.casefold() not in SUPPORTED_SUFFIXES:
            raise ValueError(f"Unsupported document type: {relative.suffix}")
        assert self.revision is not None
        return self.git.show_file(self.revision, relative)

    def read_binary(self, path: str | Path) -> bytes:
        if self.is_working_tree:
            return self.working_tree.read_binary(path)
        relative = PurePosixPath(self.relative(path).as_posix())
        if relative.suffix.casefold() not in IMAGE_SUFFIXES:
            raise ValueError(f"Unsupported image type: {relative.suffix}")
        assert self.revision is not None
        return self.git.show_file_bytes(self.revision, relative)

    def diff_versions(self, path: str | Path) -> DiffVersions:
        relative = PurePosixPath(self.relative(path).as_posix())
        if self.is_working_tree:
            before = self.git.show_file_optional("HEAD", relative) or ""
            after = self.working_tree.read_text(path) if self.working_tree.resolve(path).is_file() else ""
            return DiffVersions(before, after, f"HEAD · {self.git.current_branch()}", "Working tree")

        assert self.revision is not None
        parent = self.git.parent_revision(self.revision)
        before = self.git.show_file_optional(parent, relative) if parent else ""
        after = self.git.show_file_optional(self.revision, relative) or ""
        return DiffVersions(
            before or "",
            after,
            f"Parent · {self.revision}^" if parent else "Before first commit",
            f"Committed · {self.revision}",
        )

    def all_documents(self) -> list[Path]:
        if self.is_working_tree:
            return self.working_tree.walk_documents()
        return sorted(
            (
                self.root / Path(path.as_posix())
                for path in self._files
                if path.suffix.casefold() in SUPPORTED_SUFFIXES
            ),
            key=lambda path: str(path).casefold(),
        )

    def read_documents(self) -> dict[Path, str]:
        documents = self.all_documents()
        if self.is_working_tree:
            contents: dict[Path, str] = {}
            for path in documents:
                try:
                    contents[path] = self.working_tree.read_text(path)
                except OSError:
                    # An AI save can briefly replace or remove a file while an
                    # index build is in flight. Its next filesystem event will
                    # add the stable version back.
                    continue
            return contents
        assert self.revision is not None
        relative_paths = [PurePosixPath(self.relative(path).as_posix()) for path in documents]
        contents = self.git.show_files(self.revision, relative_paths)
        return {self.root / Path(path.as_posix()): source for path, source in contents.items()}

    @staticmethod
    def _visible(path: PurePosixPath) -> bool:
        return not any(part in IGNORED_NAMES or part.startswith(".") for part in path.parts)
