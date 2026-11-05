import pytest

from app.utils.data import (
    create_document,
    validate_document,
)


def test_create_document():
    document = create_document(
        "doc-001",
        "  AI engineering fundamentals  ",
    )

    assert document == {
        "id": "doc-001",
        "content": "AI engineering fundamentals",
    }


def test_validate_document():
    document = {
        "id": "doc-001",
        "content": "Sample content",
    }

    assert validate_document(document) is True


def test_invalid_document():
    assert validate_document({}) is False


def test_empty_document_id():
    with pytest.raises(ValueError):
        create_document("", "Sample content")
