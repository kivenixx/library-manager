from models.book import Book


def test_book_creation():
    book = Book("Orwell", "1984", 1949, 328, 12.0, 0.3, True)
    assert book.author == "Orwell"
    assert book.title == "1984"
    assert book.year == 1949
    assert book.length == 328
    assert book.font_size == 12.0
    assert book.weight == 0.3
    assert book.school_required == True
    
def test_book_school_required_false():
    book = Book("Kowalski", "Coś tam", 2020, 100, 10.0, 0.4, False)

    assert book.school_required is False
