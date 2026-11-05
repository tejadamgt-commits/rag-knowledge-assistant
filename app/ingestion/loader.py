from pathlib import Path

from app.core.exceptions import (
    DocumentLoadError,
    UnsupportedFileTypeError,
)
from app.models.document import Document

SUPPORTED_EXTENSIONS = {".txt", ".md"}


def load_document(file_path: Path) -> Document:
    """Load a TXT or Markdown document."""

    if file_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
        raise UnsupportedFileTypeError(f"Unsupported file type: {file_path.suffix}")

    try:
        content = file_path.read_text(encoding="utf-8")

    except (OSError, UnicodeDecodeError) as exc:
        raise DocumentLoadError(f"Could not load document: {file_path}") from exc

    if not content.strip():
        raise DocumentLoadError(f"Document is empty: {file_path}")

    return Document(
        content=content.strip(),
        source=str(file_path),
        metadata={
            "filename": file_path.name,
            "extension": file_path.suffix.lower(),
        },
    )


def load_directory(directory: Path) -> list[Document]:
    """Load all supported documents in a directory recursively."""

    if not directory.is_dir():
        raise DocumentLoadError(f"Directory does not exist: {directory}")

    documents = []

    for file_path in sorted(directory.rglob("*")):
        if file_path.is_file() and (file_path.suffix.lower() in SUPPORTED_EXTENSIONS):
            documents.append(load_document(file_path))

    return documents
