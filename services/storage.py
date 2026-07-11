import json
from models.book import Book


book_list_new = []

class File:
    @staticmethod
    def save(book_list):
        book_list_dict = []
        for book in book_list:
            book_list_dict.append(book.__dict__)
        with open("books.json", "w") as f:
            json.dump(book_list_dict, f, indent=4)

    @staticmethod
    def load():
        try:
            with open("books.json") as f:
                book_list_dict = json.load(f)
                for book in book_list_dict:
                    book_obj = Book(
                        book["author"],
                        book["title"],
                        book["year"],
                        book["length"],
                        book["font_size"],
                        book["weight"],
                        book["school_required"]
                    )
                    book_list_new.append(book_obj)
            return book_list_new
        except FileNotFoundError:
            print("Nie znaleziono pliku z książkami.")
