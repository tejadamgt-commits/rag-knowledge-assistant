from datetime import UTC, datetime
from uuid import uuid4

from pydantic import BaseModel, Field


class Document(BaseModel):
    """Represents a source document used by the RAG pipeline."""

    id: str = Field(default_factory=lambda: str(uuid4()))
    content: str = Field(min_length=1)
    source: str
    metadata: dict[str, str] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
