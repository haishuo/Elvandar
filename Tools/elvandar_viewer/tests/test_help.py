from PySide6.QtWidgets import QApplication

from elvandar_viewer.help_window import (
    HELP_TOPIC_BY_KEY,
    HELP_TOPICS,
    HelpDialog,
    help_topic_document,
)


def test_help_covers_the_promised_reader_topics() -> None:
    assert {topic.key for topic in HELP_TOPICS} == {
        "welcome",
        "navigate",
        "views",
        "live",
        "git",
        "safety",
        "shortcuts",
    }
    assert "never edits repository files" in HELP_TOPIC_BY_KEY["welcome"].body
    assert "● WAITING" in HELP_TOPIC_BY_KEY["live"].body
    assert "will never" in HELP_TOPIC_BY_KEY["safety"].body
    assert "⌘?" in HELP_TOPIC_BY_KEY["shortcuts"].body
    assert "⌘⇧O" in HELP_TOPIC_BY_KEY["navigate"].body
    assert "document outline" in HELP_TOPIC_BY_KEY["shortcuts"].body
    assert "Chapter 2 appears before Chapter 10" in HELP_TOPIC_BY_KEY["navigate"].body
    assert "solid coral" in HELP_TOPIC_BY_KEY["navigate"].body
    assert "N CHANGES" in HELP_TOPIC_BY_KEY["live"].body
    assert "⌘⌥↓" in HELP_TOPIC_BY_KEY["shortcuts"].body


def test_help_articles_follow_day_and_night_appearance() -> None:
    topic = HELP_TOPIC_BY_KEY["welcome"]

    day = help_topic_document(topic, False)
    night = help_topic_document(topic, True)

    assert "#FCFCFD" in day
    assert "#191C21" in night
    assert topic.title in day
    assert topic.summary in night


def test_help_dialog_can_open_a_deep_linked_topic() -> None:
    _application = QApplication.instance() or QApplication([])
    dialog = HelpDialog(False)

    dialog.open_topic("shortcuts")

    assert dialog.current_topic_key == "shortcuts"
    assert "Keyboard shortcuts" in dialog.content.toPlainText()
    assert dialog.topic_list.count() == len(HELP_TOPICS)

    dialog.set_night_mode(True)
    assert dialog.night_mode
    assert dialog.current_topic_key == "shortcuts"
