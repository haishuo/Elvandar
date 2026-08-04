from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass(frozen=True, slots=True)
class NavigationEntry:
    """A document location that can be revisited without touching the repository."""

    relative_path: PurePosixPath
    mode: str
    scroll_ratio: float


class NavigationHistory:
    """Small browser-style back/forward history for the active repository view."""

    def __init__(self, limit: int = 100) -> None:
        self.limit = max(1, limit)
        self._back: list[NavigationEntry] = []
        self._forward: list[NavigationEntry] = []

    @property
    def can_go_back(self) -> bool:
        return bool(self._back)

    @property
    def can_go_forward(self) -> bool:
        return bool(self._forward)

    def remember(self, entry: NavigationEntry) -> None:
        self._back.append(entry)
        if len(self._back) > self.limit:
            del self._back[: len(self._back) - self.limit]
        self._forward.clear()

    def peek_back(self) -> NavigationEntry | None:
        return self._back[-1] if self._back else None

    def peek_forward(self) -> NavigationEntry | None:
        return self._forward[-1] if self._forward else None

    def discard_back(self) -> None:
        if self._back:
            self._back.pop()

    def discard_forward(self) -> None:
        if self._forward:
            self._forward.pop()

    def go_back(self, current: NavigationEntry) -> NavigationEntry | None:
        if not self._back:
            return None
        target = self._back.pop()
        self._forward.append(current)
        return target

    def go_forward(self, current: NavigationEntry) -> NavigationEntry | None:
        if not self._forward:
            return None
        target = self._forward.pop()
        self._back.append(current)
        return target

    def clear(self) -> None:
        self._back.clear()
        self._forward.clear()


def normalized_scroll(value: int, maximum: int) -> float:
    if maximum <= 0:
        return 0.0
    return min(1.0, max(0.0, value / maximum))


def restored_scroll(ratio: float, maximum: int) -> int:
    return round(min(1.0, max(0.0, ratio)) * max(0, maximum))
