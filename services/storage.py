import json
from models.book import Book


class File:
    @staticmethod
    def save(book_list, path: str = "books.json") -> None:
        book_list_dict = [book.__dict__ for book in book_list]
        with open(path, "w") as f:
            json.dump(book_list_dict, f, indent=4)

    @staticmethod
    def load(path: str = "books.json") -> list[Book]:
        book_list_new = []
        with open(path) as f:
            book_list_dict = json.load(f)
            for book in book_list_dict:
                book_list_new.append(Book(
                    book["author"],
                    book["title"],
                    book["year"],
                    book["length"],
                    book["font_size"],
                    book["weight"],
                    book["school_required"]
                ))
        return book_list_new
