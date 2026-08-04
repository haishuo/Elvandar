from pathlib import PurePosixPath

from elvandar_viewer.change_awareness import ChangeState, ChangeTracker


def test_changed_versions_move_from_unseen_to_viewed_and_back() -> None:
    chapter = PurePosixPath("Book 3/Chapters/Chapter 3.md")
    signatures = {chapter: "first-change"}
    tracker = ChangeTracker()

    tracker.refresh([chapter], signatures.get)
    assert tracker.state_for(chapter) == ChangeState.UNSEEN

    assert tracker.mark_viewed(chapter, "first-change")
    assert tracker.state_for(chapter) == ChangeState.VIEWED

    signatures[chapter] = "second-change"
    tracker.refresh([chapter], signatures.get)
    assert tracker.state_for(chapter) == ChangeState.UNSEEN


def test_folders_roll_up_the_strongest_descendant_state() -> None:
    first = PurePosixPath("Book 3/Chapters/Chapter 1.md")
    third = PurePosixPath("Book 3/Chapters/Chapter 3.md")
    tracker = ChangeTracker({first.as_posix(): "read"})
    tracker.refresh([first, third], {first: "read", third: "new"}.get)

    assert tracker.state_for(PurePosixPath("Book 3"), directory=True) == ChangeState.UNSEEN
    assert tracker.counts_for(PurePosixPath("Book 3/Chapters")) == (1, 1)


def test_seen_signatures_round_trip_through_settings_json() -> None:
    tracker = ChangeTracker(
        {"Book 3/Chapters/Chapter 2.md": "seen"},
        {"Book 3/Chapters/Chapter 3.md": "pending"},
    )

    restored = ChangeTracker.from_json(tracker.to_json())

    assert restored.seen_signatures == tracker.seen_signatures
    assert restored.pending_signatures == tracker.pending_signatures


def test_unseen_change_survives_when_it_moves_out_of_the_current_git_window() -> None:
    chapter = PurePosixPath("Book 3/Chapters/Chapter 3.md")
    signatures = {chapter: "unread-version"}
    tracker = ChangeTracker()

    tracker.refresh([chapter], signatures.get)
    tracker.refresh([], signatures.get)

    assert tracker.state_for(chapter) == ChangeState.UNSEEN
