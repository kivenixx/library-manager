class Book:
    def __init__(self):
        self.author = input("Podaj autora: ")
        self.title = input("Podaj tytuł: ")

        self.year = validation("Podaj rok wydania: ", "i")
        self.length = validation("Podaj ilość stron: ", "i")
        self.font_size = validation("Podaj wielkość czcionki: ", "f")
        self.weight = validation("Podaj wagę: ", "f")

        while True:
            resp = input("Czy jest lekturą szkolną (t/n): ").lower()

            if resp in(["t","n"]): break

        self.school_required = True if resp == "t" else False

    def display(self):
        print(
            f"\nAutor: {self.author}\n"
            f"Tytuł: {self.title}\n"
            f"Rok wydania: {self.year}\n"
            f"Długość: {self.length} stron\n"
            f"Wielkość czcionki: {self.font_size} pt\n"
            f"Waga: {self.weight} kg\n"
            f"Lektura szkolna: {"Tak" if self.school_required else "Nie"}"
        )


def validation(message, var_type):
    while True:
        resp = input(message)

        try:
            if var_type == "i":
                attribute = int(resp)
            elif var_type == "f":
                attribute = float(resp)
            else:
                raise SystemExit("Error: Variable type not allowed.")
            return attribute
        except ValueError:
            print("Podana wartość nie jest liczbą całkowitą.")
