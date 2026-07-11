from models.book import Book
from services.storage import File


book_list = []

def validation(message, var_type):
    while True:
        resp_value = input(message)

        try:
            if var_type == "i":
                attribute = int(resp_value)
            elif var_type == "f":
                attribute = float(resp_value)
            else:
                raise SystemExit("Error: Variable type not allowed.")
            return attribute
        except ValueError:
            print("Podana wartość nie jest liczbą całkowitą.")

while True:
    print(
        "\n"
        "1. Dodaj książkę\n"
        "2. Wyświetl książki\n"
        "3. Zapisz do JSON\n"
        "4. Wczytaj JSON"
    )

    resp_menu = input()

    if resp_menu == "1":
        author = input("Podaj autora: ")
        title = input("Podaj tytuł: ")

        year = validation("Podaj rok wydania: ", "i")
        length = validation("Podaj ilość stron: ", "i")
        font_size = validation("Podaj wielkość czcionki: ", "f")
        weight = validation("Podaj wagę: ", "f")

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
        File.save(book_list)
    elif resp_menu == "4":
        book_list = File.load()
    else:
        print("Wprowadź liczbę od 1 do 4.")
