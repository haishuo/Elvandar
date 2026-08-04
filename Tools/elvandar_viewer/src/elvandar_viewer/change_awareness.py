from __future__ import annotations

import json
from collections.abc import Callable, Iterable
from enum import Enum
from pathlib import PurePosixPath


class ChangeState(str, Enum):
    UNSEEN = "unseen"
    VIEWED = "viewed"


SignatureLookup = Callable[[PurePosixPath], str | None]


class ChangeTracker:
    """Remember which exact changed file versions the reader has opened."""

    def __init__(
        self,
        seen_signatures: dict[str, str] | None = None,
        pending_signatures: dict[str, str] | None = None,
    ) -> None:
        self.seen_signatures = dict(seen_signatures or {})
        self.pending_signatures = dict(pending_signatures or {})
        self.active_paths: set[PurePosixPath] = set()
        self.states: dict[PurePosixPath, ChangeState] = {}

    @classmethod
    def from_json(cls, value: str) -> "ChangeTracker":
        try:
            decoded = json.loads(value) if value else {}
        except (TypeError, ValueError):
            decoded = {}
        if not isinstance(decoded, dict):
            return cls()
        seen = decoded.get("seen")
        pending = decoded.get("pending")
        if not isinstance(seen, dict):
            # Version 1 stored the seen-signature mapping directly.
            seen = decoded
        if not isinstance(pending, dict):
            pending = {}
        return cls(
            seen_signatures={
                str(path): str(signature)
                for path, signature in seen.items()
                if isinstance(path, str) and isinstance(signature, str)
            },
            pending_signatures={
                str(path): str(signature)
                for path, signature in pending.items()
                if isinstance(path, str) and isinstance(signature, str)
            },
        )

    def to_json(self) -> str:
        return json.dumps(
            {"pending": self.pending_signatures, "seen": self.seen_signatures},
            sort_keys=True,
            separators=(",", ":"),
        )

    def refresh(self, changed_paths: Iterable[PurePosixPath], signature: SignatureLookup) -> None:
        states: dict[PurePosixPath, ChangeState] = {}
        active_paths: set[PurePosixPath] = set()
        for path in changed_paths:
            if path.is_absolute() or ".." in path.parts:
                continue
            current = signature(path)
            if current is None:
                continue
            active_paths.add(path)
            key = path.as_posix()
            if self.seen_signatures.get(key) == current:
                self.pending_signatures.pop(key, None)
                states[path] = ChangeState.VIEWED
            else:
                self.pending_signatures[key] = current
                states[path] = ChangeState.UNSEEN

        for key, pending_signature in tuple(self.pending_signatures.items()):
            path = PurePosixPath(key)
            if path in active_paths:
                continue
            current = signature(path)
            if current == pending_signature and self.seen_signatures.get(key) != current:
                states[path] = ChangeState.UNSEEN
            else:
                self.pending_signatures.pop(key, None)
        self.active_paths = active_paths
        self.states = states

    def mark_viewed(self, path: PurePosixPath, signature: str | None) -> bool:
        if path not in self.states or signature is None:
            return False
        key = path.as_posix()
        changed = self.seen_signatures.get(key) != signature
        self.seen_signatures[key] = signature
        self.pending_signatures.pop(key, None)
        if path in self.active_paths:
            self.states[path] = ChangeState.VIEWED
        else:
            self.states.pop(path, None)
        return changed

    def state_for(self, path: PurePosixPath, *, directory: bool = False) -> ChangeState | None:
        if not directory:
            return self.states.get(path)
        descendant_states = [
            state for changed_path, state in self.states.items() if changed_path.is_relative_to(path)
        ]
        if ChangeState.UNSEEN in descendant_states:
            return ChangeState.UNSEEN
        if ChangeState.VIEWED in descendant_states:
            return ChangeState.VIEWED
        return None

    def counts_for(self, path: PurePosixPath) -> tuple[int, int]:
        states = [
            state for changed_path, state in self.states.items() if changed_path.is_relative_to(path)
        ]
        return states.count(ChangeState.UNSEEN), states.count(ChangeState.VIEWED)
