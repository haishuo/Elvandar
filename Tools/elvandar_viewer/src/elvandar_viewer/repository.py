from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re


IGNORED_NAMES = {
    ".git",
    ".claude",
    ".codex",
    ".agents",
    ".DS_Store",
    "TGMS - OLD",
    "__pycache__",
}

SUPPORTED_SUFFIXES = {".md", ".markdown", ".txt"}
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".tif", ".tiff", ".svg"}
VISIBLE_SUFFIXES = SUPPORTED_SUFFIXES | IMAGE_SUFFIXES
_NATURAL_PART = re.compile(r"(\d+)")


def natural_sort_key(value: str) -> tuple[tuple[int, str | int, int], ...]:
    """Sort human-numbered names in reading order: Chapter 2 before Chapter 10."""

    return tuple(
        (1, int(part), len(part)) if part.isdigit() else (0, part.casefold(), 0)
        for part in _NATURAL_PART.split(value)
        if part
    )


class RepositoryBoundaryError(ValueError):
    """Raised when navigation tries to leave the repository root."""


@dataclass(frozen=True, slots=True)
class Repository:
    root: Path

    @classmethod
    def open(cls, path: str | Path) -> "Repository":
        root = Path(path).expanduser().resolve(strict=True)
        if not root.is_dir():
            raise NotADirectoryError(root)
        return cls(root=root)

    def resolve(self, path: str | Path) -> Path:
        candidate = Path(path)
        if not candidate.is_absolute():
            candidate = self.root / candidate
        candidate = candidate.resolve(strict=False)
        if not candidate.is_relative_to(self.root):
            raise RepositoryBoundaryError(candidate)
        return candidate

    def relative(self, path: str | Path) -> Path:
        return self.resolve(path).relative_to(self.root)

    def directories(self, parent: str | Path | None = None) -> list[Path]:
        folder = self.resolve(parent or self.root)
        if not folder.is_dir():
            return []
        return sorted(
            (
                item
                for item in folder.iterdir()
                if item.is_dir()
                and item.name not in IGNORED_NAMES
                and not item.name.startswith(".")
            ),
            key=lambda item: natural_sort_key(item.name),
        )

    def contents(self, folder: str | Path) -> list[Path]:
        parent = self.resolve(folder)
        if not parent.is_dir():
            return []
        return sorted(
            (
                item
                for item in parent.iterdir()
                if item.name not in IGNORED_NAMES
                and not item.name.startswith(".")
                and (item.is_dir() or item.suffix.casefold() in VISIBLE_SUFFIXES)
            ),
            key=lambda item: (not item.is_dir(), natural_sort_key(item.name)),
        )

    def walk_directories(self) -> list[Path]:
        discovered: list[Path] = []
        pending = [self.root]
        while pending:
            folder = pending.pop()
            discovered.append(folder)
            pending.extend(reversed(self.directories(folder)))
        return discovered

    def walk_documents(self) -> list[Path]:
        return [
            item
            for folder in self.walk_directories()
            for item in self.contents(folder)
            if item.is_file() and item.suffix.casefold() in SUPPORTED_SUFFIXES
        ]

    def walk_visible_files(self) -> list[Path]:
        return [
            item
            for folder in self.walk_directories()
            for item in self.contents(folder)
            if item.is_file()
        ]

    def structure_snapshot(self) -> tuple[tuple[str, str], ...]:
        """Describe visible folders and readable documents, excluding mtimes."""

        entries: list[tuple[str, str]] = []
        for folder in self.walk_directories():
            entries.append((str(self.relative(folder)), "directory"))
            for item in self.contents(folder):
                if item.is_file():
                    kind = "image" if item.suffix.casefold() in IMAGE_SUFFIXES else "document"
                    entries.append((str(self.relative(item)), kind))
        return tuple(sorted(entries))

    def read_text(self, path: str | Path) -> str:
        document = self.resolve(path)
        if document.suffix.casefold() not in SUPPORTED_SUFFIXES:
            raise ValueError(f"Unsupported document type: {document.suffix}")
        return document.read_text(encoding="utf-8", errors="replace")

    def read_binary(self, path: str | Path) -> bytes:
        asset = self.resolve(path)
        if asset.suffix.casefold() not in IMAGE_SUFFIXES:
            raise ValueError(f"Unsupported image type: {asset.suffix}")
        return asset.read_bytes()


def discover_repository(start: str | Path) -> Path:
    current = Path(start).expanduser().resolve(strict=True)
    if current.is_file():
        current = current.parent
    for candidate in (current, *current.parents):
        if (candidate / ".git").exists():
            return candidate
    raise FileNotFoundError("No Git repository found in this folder or its parents")
