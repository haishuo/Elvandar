from pathlib import PurePosixPath

from elvandar_viewer.navigation import (
    NavigationEntry,
    NavigationHistory,
    normalized_scroll,
    restored_scroll,
)


def _entry(name: str, ratio: float = 0.0) -> NavigationEntry:
    return NavigationEntry(PurePosixPath(name), "Rendered", ratio)


def test_navigation_history_moves_between_back_and_forward_stacks() -> None:
    history = NavigationHistory()
    first = _entry("Book 1/Chapter 1.md", 0.2)
    second = _entry("Book 1/Chapter 2.md", 0.6)
    third = _entry("People/Elara.md", 0.1)

    history.remember(first)
    history.remember(second)

    assert history.go_back(third) == second
    assert history.go_back(second) == first
    assert history.go_forward(first) == second
    assert history.can_go_back
    assert history.can_go_forward


def test_new_navigation_clears_forward_history_and_honors_limit() -> None:
    history = NavigationHistory(limit=2)
    first = _entry("one.md")
    second = _entry("two.md")
    third = _entry("three.md")
    current = _entry("current.md")

    history.remember(first)
    history.remember(second)
    assert history.go_back(current) == second
    history.remember(third)

    assert not history.can_go_forward
    assert history.go_back(current) == third
    assert history.go_back(third) == first
    assert not history.can_go_back


def test_scroll_position_is_saved_as_a_resize_safe_ratio() -> None:
    ratio = normalized_scroll(375, 500)

    assert ratio == 0.75
    assert restored_scroll(ratio, 1200) == 900
    assert normalized_scroll(10, 0) == 0.0
    assert restored_scroll(2.0, 100) == 100
