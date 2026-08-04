from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path, PurePosixPath

from PySide6.QtCore import QFileSystemWatcher, QObject, QTimer, Signal


class GitError(RuntimeError):
    """A read-only Git query failed."""


@dataclass(frozen=True, slots=True)
class Branch:
    name: str
    revision: str
    current: bool = False


@dataclass(frozen=True, slots=True)
class Worktree:
    path: Path
    revision: str
    branch: str | None
    bare: bool = False


@dataclass(frozen=True, slots=True)
class Commit:
    revision: str
    short_revision: str
    author: str
    committed_at: datetime
    subject: str


@dataclass(frozen=True, slots=True)
class Change:
    index_status: str
    worktree_status: str
    path: PurePosixPath

    @property
    def label(self) -> str:
        code = (self.index_status + self.worktree_status).strip() or "?"
        return f"{code:<2}  {self.path}"


class GitClient:
    """Issue only non-mutating Git commands against a working repository."""

    def __init__(self, root: Path) -> None:
        self.root = root.resolve(strict=True)
        if not (self.root / ".git").exists():
            raise GitError(f"Not a Git repository: {self.root}")
        self._run("rev-parse", "--git-dir")

    def current_branch(self) -> str:
        branch = self.current_branch_name()
        if branch is not None:
            return branch
        return f"Detached at {self._run('rev-parse', '--short', 'HEAD').stdout.strip()}"

    def current_branch_name(self) -> str | None:
        result = self._run("symbolic-ref", "--quiet", "--short", "HEAD", check=False)
        return result.stdout.strip() if result.returncode == 0 else None

    def preferred_base_branch(self) -> str | None:
        names = {branch.name for branch in self.branches()}
        for candidate in ("main", "master"):
            if candidate in names:
                return candidate
        return None

    def merge_base(self, first: str, second: str = "HEAD") -> str:
        return self._run("merge-base", first, second).stdout.strip()

    def branches(self) -> list[Branch]:
        output = self._run(
            "for-each-ref",
            "--format=%(refname:short)%09%(objectname:short)%09%(HEAD)",
            "refs/heads",
        ).stdout
        branches: list[Branch] = []
        for line in output.splitlines():
            if not line:
                continue
            name, revision, marker = line.split("\t", 2)
            branches.append(Branch(name=name, revision=revision, current=marker.strip() == "*"))
        return sorted(branches, key=lambda branch: (not branch.current, branch.name.casefold()))

    def worktrees(self) -> list[Worktree]:
        output = self._run("worktree", "list", "--porcelain").stdout
        records: list[Worktree] = []
        current: dict[str, str] = {}
        for line in (*output.splitlines(), ""):
            if not line:
                if current:
                    records.append(
                        Worktree(
                            path=Path(current["worktree"]),
                            revision=current.get("HEAD", "")[:8],
                            branch=self._short_branch(current.get("branch")),
                            bare="bare" in current,
                        )
                    )
                    current = {}
                continue
            key, _, value = line.partition(" ")
            current[key] = value
        return records

    def recent_commits(self, revision: str = "HEAD", limit: int = 8) -> list[Commit]:
        output = self._run(
            "log",
            f"--max-count={limit}",
            "--format=%H%x09%h%x09%an%x09%aI%x09%s",
            revision,
            "--",
        ).stdout
        commits: list[Commit] = []
        for line in output.splitlines():
            if not line:
                continue
            full, short, author, timestamp, subject = line.split("\t", 4)
            commits.append(
                Commit(
                    revision=full,
                    short_revision=short,
                    author=author,
                    committed_at=datetime.fromisoformat(timestamp),
                    subject=subject,
                )
            )
        return commits

    def changes(self) -> list[Change]:
        output = self._run_bytes(
            "-c", "core.quotepath=false", "status", "--porcelain=v1", "-z", "--untracked-files=all"
        )
        changes: list[Change] = []
        records = output.split(b"\0")
        index = 0
        while index < len(records):
            record = records[index]
            index += 1
            if len(record) < 4:
                continue
            index_status = chr(record[0])
            worktree_status = chr(record[1])
            path_text = record[3:].decode("utf-8", errors="replace")
            changes.append(
                Change(
                    index_status=index_status,
                    worktree_status=worktree_status,
                    path=PurePosixPath(path_text),
                )
            )
            if index_status in {"R", "C"} or worktree_status in {"R", "C"}:
                index += 1
        return changes

    def paths_changed_since(self, revision: str) -> set[PurePosixPath]:
        output = self._run_bytes("diff", "--name-only", "-z", revision, "--")
        return {
            PurePosixPath(path.decode("utf-8", errors="replace"))
            for path in output.split(b"\0")
            if path
        }

    def list_files(self, revision: str) -> list[PurePosixPath]:
        output = self._run_bytes("ls-tree", "-r", "-z", "--name-only", revision, "--")
        return [PurePosixPath(path.decode("utf-8", errors="replace")) for path in output.split(b"\0") if path]

    def show_file(self, revision: str, path: PurePosixPath) -> str:
        return self.show_file_bytes(revision, path).decode("utf-8", errors="replace")

    def show_file_bytes(self, revision: str, path: PurePosixPath) -> bytes:
        if path.is_absolute() or ".." in path.parts:
            raise GitError(f"Invalid repository path: {path}")
        return self._run_bytes("show", f"{revision}:{path.as_posix()}")

    def show_file_optional(self, revision: str, path: PurePosixPath) -> str | None:
        try:
            return self.show_file(revision, path)
        except GitError:
            return None

    def show_file_bytes_optional(self, revision: str, path: PurePosixPath) -> bytes | None:
        try:
            return self.show_file_bytes(revision, path)
        except GitError:
            return None

    def show_files(self, revision: str, paths: list[PurePosixPath]) -> dict[PurePosixPath, str]:
        if not paths:
            return {}
        for path in paths:
            if path.is_absolute() or ".." in path.parts or "\n" in path.as_posix():
                raise GitError(f"Invalid repository path: {path}")

        specifications = [f"{revision}:{path.as_posix()}" for path in paths]
        environment = os.environ.copy()
        environment.update({"GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"})
        result = subprocess.run(
            ["git", "-C", str(self.root), "cat-file", "--batch"],
            input=("\n".join(specifications) + "\n").encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=environment,
            check=False,
        )
        if result.returncode != 0:
            raise GitError(result.stderr.decode("utf-8", errors="replace").strip() or "Git query failed")

        documents: dict[PurePosixPath, str] = {}
        cursor = 0
        for path in paths:
            header_end = result.stdout.find(b"\n", cursor)
            if header_end < 0:
                raise GitError("Git returned an incomplete batch response")
            header = result.stdout[cursor:header_end].decode("utf-8", errors="replace")
            cursor = header_end + 1
            if header.endswith(" missing"):
                continue
            fields = header.rsplit(" ", 2)
            if len(fields) != 3 or fields[1] != "blob":
                raise GitError(f"Unexpected Git object response: {header}")
            size = int(fields[2])
            content = result.stdout[cursor : cursor + size]
            cursor += size + 1
            documents[path] = content.decode("utf-8", errors="replace")
        return documents

    def parent_revision(self, revision: str) -> str | None:
        result = self._run("rev-parse", "--verify", f"{revision}^", check=False)
        return result.stdout.strip() if result.returncode == 0 else None

    def metadata_watch_paths(self) -> list[Path]:
        git_directory = Path(self._run("rev-parse", "--absolute-git-dir").stdout.strip())
        common_text = self._run("rev-parse", "--git-common-dir").stdout.strip()
        common_directory = Path(common_text)
        if not common_directory.is_absolute():
            common_directory = (self.root / common_directory).resolve(strict=False)
        candidates = [
            git_directory / "HEAD",
            git_directory / "index",
            git_directory / "logs" / "HEAD",
            common_directory / "packed-refs",
            common_directory / "refs" / "heads",
        ]
        refs = common_directory / "refs" / "heads"
        if refs.is_dir():
            candidates.extend(path for path in refs.rglob("*") if path.is_dir())
        return [path for path in candidates if path.exists()]

    def _run(self, *arguments: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        environment = os.environ.copy()
        environment.update({"GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"})
        result = subprocess.run(
            ["git", "-C", str(self.root), *arguments],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=environment,
            check=False,
        )
        if check and result.returncode != 0:
            message = result.stderr.strip() or "Git query failed"
            raise GitError(message)
        return result

    def _run_bytes(self, *arguments: str) -> bytes:
        environment = os.environ.copy()
        environment.update({"GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"})
        result = subprocess.run(
            ["git", "-C", str(self.root), *arguments],
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=environment,
            check=False,
        )
        if result.returncode != 0:
            raise GitError(result.stderr.decode("utf-8", errors="replace").strip() or "Git query failed")
        return result.stdout

    @staticmethod
    def _short_branch(branch: str | None) -> str | None:
        if branch is None:
            return None
        return branch.removeprefix("refs/heads/")


class GitMetadataWatcher(QObject):
    """Watch Git's metadata files so status and history remain current."""

    changed = Signal()

    def __init__(self, git: GitClient, parent: QObject | None = None) -> None:
        super().__init__(parent)
        self.git = git
        self._watcher = QFileSystemWatcher(self)
        self._watcher.fileChanged.connect(self._queue_refresh)
        self._watcher.directoryChanged.connect(self._queue_refresh)
        self._timer = QTimer(self)
        self._timer.setSingleShot(True)
        self._timer.setInterval(180)
        self._timer.timeout.connect(self._flush)
        self._sync_paths()

    def _queue_refresh(self, _path: str) -> None:
        self._timer.start()

    def _flush(self) -> None:
        self._sync_paths()
        self.changed.emit()

    def _sync_paths(self) -> None:
        desired = {str(path) for path in self.git.metadata_watch_paths()}
        current = set(self._watcher.files()) | set(self._watcher.directories())
        stale = current - desired
        missing = desired - current
        if stale:
            self._watcher.removePaths(sorted(stale))
        if missing:
            self._watcher.addPaths(sorted(missing))
