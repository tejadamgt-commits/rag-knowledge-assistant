from typing import Any


def validate_document(document: dict[str, Any]) -> bool:
    """Validate a basic document record."""

    required_fields = {"id", "content"}

    if not required_fields.issubset(document):
        return False

    if not isinstance(document["id"], str):
        return False

    if not isinstance(document["content"], str):
        return False

    return bool(document["id"].strip() and document["content"].strip())


def create_document(
    document_id: str,
    content: str,
) -> dict[str, str]:
    """Create a normalized document record."""

    if not document_id.strip():
        raise ValueError("document_id cannot be empty")

    if not content.strip():
        raise ValueError("content cannot be empty")

    return {
        "id": document_id,
        "content": content.strip(),
    }
