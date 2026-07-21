from models.book import Book
from services.storage import File


book_list: list[Book] = []

def validate_int(message: str) -> int:
    while True:
        resp_value = input(message)
        try:
            return int(resp_value)
        except ValueError:
            print("Podana wartość nie jest liczbą całkowitą.")

def validate_float(message: str) -> float:
    while True:
        resp_value = input(message)
        try:
            return float(resp_value)
        except ValueError:
            print("Podana wartość nie jest liczbą.")


while True:
    print(
        "1. Dodaj książkę\n"
        "2. Wyświetl książki\n"
        "3. Zapisz do JSON\n"
        "4. Wczytaj JSON"
    )

    resp_menu = input()

    if resp_menu == "1":
        author = input("Podaj autora: ")
        title = input("Podaj tytuł: ")

        year: int = validate_int("Podaj rok wydania: ")
        length = validate_int("Podaj ilość stron: ")
        font_size = validate_float("Podaj wielkość czcionki: ")
        weight = validate_float("Podaj wagę: ")

        while True:
            resp_school_required = input("Czy jest lekturą szkolną (t/n): ").lower()

            if resp_school_required in ("t","n"): break

        school_required = resp_school_required == "t"

        book_obj = Book(author, title, year, length, font_size, weight, school_required)
        book_list.append(book_obj)

    elif resp_menu == "2":
        if book_list:
            for book in book_list:
                book.display()
        else:
            print("Lista książek jest pusta.")

    elif resp_menu == "3":
        if book_list:
            File.save(book_list)
        else:
            print("Brak danych do zapisania.")

    elif resp_menu == "4":
        try:
            book_list = File.load()
        except FileNotFoundError:
            print("Nie znaleziono pliku z książkami.")
    else:
        print("Wprowadź liczbę od 1 do 4.")
