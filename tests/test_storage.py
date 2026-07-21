import pytest

from models.book import Book
from services.storage import File


def test_save_and_load(tmp_path):
    path = tmp_path / "books.json"

    books = [Book("Orwell", "1984", 1949, 328, 12.0, 0.3, True)]

    File.save(books, str(path))
    assert path.exists()

    loaded = File.load(str(path))
    assert len(loaded) == 1
    assert loaded[0].author == "Orwell"
    assert loaded[0].school_required == True


def test_file_missing(tmp_path):
    path = tmp_path / "nonexistent.json"

    with pytest.raises(FileNotFoundError):
        File.load(str(path))
