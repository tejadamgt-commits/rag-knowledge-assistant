import pytest

from app.utils.text import chunk_text, normalize_text


def test_normalize_text():
    text = "AI   engineering\n is important"

    assert normalize_text(text) == "AI engineering is important"


def test_chunk_text():
    text = "one two three four five"

    result = chunk_text(
        text,
        chunk_size=3,
        overlap=1,
    )

    assert result == [
        "one two three",
        "three four five",
        "five",
    ]


def test_empty_text():
    assert chunk_text("") == []


def test_invalid_chunk_size():
    with pytest.raises(ValueError):
        chunk_text("hello world", chunk_size=0)


def test_invalid_overlap():
    with pytest.raises(ValueError):
        chunk_text("hello world", chunk_size=5, overlap=5)
