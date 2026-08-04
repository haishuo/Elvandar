from __future__ import annotations

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

