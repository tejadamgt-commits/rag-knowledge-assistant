def normalize_text(text: str) -> str:
    """Normalize whitespace in a text document."""
    return " ".join(text.split())


def chunk_text(
    text: str,
    chunk_size: int = 500,
    overlap: int = 50,
) -> list[str]:
    """Split text into overlapping word-based chunks."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size")

    words = normalize_text(text).split()

    if not words:
        return []

    chunks = []
    step = chunk_size - overlap

    for start in range(0, len(words), step):
        chunk = words[start : start + chunk_size]
        if chunk:
            chunks.append(" ".join(chunk))

    return chunks
