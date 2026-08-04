from __future__ import annotations

from bisect import bisect_left, bisect_right
from difflib import SequenceMatcher


def changed_block_indices(before: list[str], after: list[str]) -> list[int]:
    """Return the new document blocks affected by an edit.

    A pure deletion marks the nearest surviving block so the reader still gets
    a spatial cue for where text disappeared.
    """

    changed: set[int] = set()
    matcher = SequenceMatcher(a=before, b=after, autojunk=False)
    for operation, _old_start, _old_end, new_start, new_end in matcher.get_opcodes():
        if operation == "equal":
            continue
        if new_start < new_end:
            changed.update(range(new_start, new_end))
        elif after:
            changed.add(min(new_start, len(after) - 1))
    return sorted(changed)


def adjacent_change_index(
    blocks: list[int],
    *,
    current_block: int,
    active_index: int | None,
    step: int,
) -> int | None:
    """Choose the previous or next changed block, wrapping at either end."""

    if not blocks or step == 0:
        return None
    if active_index is not None and 0 <= active_index < len(blocks):
        return (active_index + (1 if step > 0 else -1)) % len(blocks)
    if step > 0:
        candidate = bisect_left(blocks, current_block)
        return candidate if candidate < len(blocks) else 0
    candidate = bisect_right(blocks, current_block) - 1
    return candidate if candidate >= 0 else len(blocks) - 1
