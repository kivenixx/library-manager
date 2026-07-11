class Book:
    def __init__(self):
        self.author = str(input("Podaj autora: "))
        self.title = str(input("Podaj tytuł: "))
        self.year = int(input("Podaj rok wydania: "))
        self.length = int(input("Podaj ilość stron: "))
        self.font_size = float(input("Podaj wielkość czcionki: "))
        self.weight = float(input("Podaj wagę: "))

        while True:
            resp = input("Czy jest lekturą szkolną (t/n): ").lower()

            if resp in(["t","n"]): break

        self.school_required = resp
        print(self.school_required)

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

