class DocumentError(Exception):
    """Base exception for document processing errors."""


class UnsupportedFileTypeError(DocumentError):
    """Raised when a document format is unsupported."""


class DocumentLoadError(DocumentError):
    """Raised when a document cannot be loaded."""
