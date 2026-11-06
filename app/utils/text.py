def normalize_text(text: str) -> str:
    """Normalize whitespace in text."""
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

    step = chunk_size - overlap
    chunks = []

    for start in range(0, len(words), step):
        chunk_words = words[start : start + chunk_size]

        if chunk_words:
            chunks.append(" ".join(chunk_words))

        if start + chunk_size >= len(words):
            break

    return chunks
