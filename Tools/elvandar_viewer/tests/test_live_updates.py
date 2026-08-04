from elvandar_viewer.live_updates import changed_block_indices


def test_changed_blocks_include_insertions_and_replacements() -> None:
    before = ["First", "The old paragraph", "Last"]
    after = ["First", "A new paragraph", "Another paragraph", "Last"]

    assert changed_block_indices(before, after) == [1, 2]


def test_deletion_marks_nearest_surviving_block() -> None:
    before = ["First", "Removed", "Last"]
    after = ["First", "Last"]

    assert changed_block_indices(before, after) == [1]
