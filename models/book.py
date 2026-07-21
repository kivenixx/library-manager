class Book:
    author: str
    title: str
    year: int
    length: int
    font_size: float
    weight: float
    school_required: bool
    
    def __init__(self, author: str, title: str, year: int, length: int, font_size: float, weight: float, school_required: bool) -> None:
        self.author = author
        self.title = title
        self.year = year
        self.length = length
        self.font_size = font_size
        self.weight = weight
        self.school_required = school_required


    def display(self) -> None:
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
