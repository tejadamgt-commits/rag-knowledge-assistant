from app.ingestion.loader import load_document


def test_load_text_document(tmp_path):
    file_path = tmp_path / "sample.txt"
    file_path.write_text("Hello AI engineering", encoding="utf-8")

    document = load_document(file_path)

    assert document.content == "Hello AI engineering"
    assert document.metadata["filename"] == "sample.txt"
