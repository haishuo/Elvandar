from elvandar_viewer.live_updates import adjacent_change_index, changed_block_indices


def test_changed_blocks_include_insertions_and_replacements() -> None:
    before = ["First", "The old paragraph", "Last"]
    after = ["First", "A new paragraph", "Another paragraph", "Last"]

    assert changed_block_indices(before, after) == [1, 2]


def test_deletion_marks_nearest_surviving_block() -> None:
    before = ["First", "Removed", "Last"]
    after = ["First", "Last"]

    assert changed_block_indices(before, after) == [1]


def test_change_navigation_starts_near_the_reader_and_wraps() -> None:
    blocks = [2, 8, 15]

    assert adjacent_change_index(
        blocks, current_block=7, active_index=None, step=1
    ) == 1
    assert adjacent_change_index(
        blocks, current_block=7, active_index=None, step=-1
    ) == 0
    assert adjacent_change_index(
        blocks, current_block=15, active_index=2, step=1
    ) == 0
    assert adjacent_change_index(
        blocks, current_block=2, active_index=0, step=-1
    ) == 2


def test_change_navigation_has_no_target_without_changes() -> None:
    assert adjacent_change_index(
        [], current_block=0, active_index=None, step=1
    ) is None
