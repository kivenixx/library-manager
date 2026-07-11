class Book:
    def __init__(self, author, title, year, length, font_size, weight, school_required):
        self.author = author
        self.title = title
        self.year = year
        self.length = length
        self.font_size = font_size
        self.weight = weight
        self.school_required = school_required


    def display(self):
        print(
            "\n"
            f"Autor: {self.author}\n"
            f"Tytuł: {self.title}\n"
            f"Rok wydania: {self.year}\n"
            f"Długość: {self.length} stron\n"
            f"Wielkość czcionki: {self.font_size} pt\n"
            f"Waga: {self.weight} kg\n"
            f"Lektura szkolna: {"Tak" if self.school_required else "Nie"}"
        )
