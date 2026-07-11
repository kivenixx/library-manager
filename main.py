from models.book import Book
book_list = []
while True:
    print(
        "\n1. Dodaj książkę\n"
        "2. Wyświetl książki\n"
        "3. Zapisz do JSON\n"
        "4. Wczytaj JSON"
    )

    resp = input()

    if resp == "1":
        b1 = Book()
        book_list.append(b1)
    elif resp == "2":
        if book_list:
            for book in book_list:
                book.display()
        else:
            print("Lista książek jest pusta.")
    elif resp == "3":
        pass
        #zapisz
    elif resp == "4":
        pass
        #wczytaj
    else:
        print("Wprowadź liczbę od 1 do 4.")
