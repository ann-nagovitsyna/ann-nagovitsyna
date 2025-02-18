class Book:
    def __init__(self, name: str, author: str):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    def __str__(self):
        return f"Книга '{self.name}'. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Количество страниц должно быть целым числом.")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.__pages = value

    def __str__(self):
        return f"{super().__str__()}, Страниц: {self.pages}"

    def __repr__(self):
        return f"PaperBook(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Продолжительность должна быть числом.")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом.")
        self.__duration = value

    def __str__(self):
        return f"{super().__str__()}, Продолжительность: {self.duration} ч."

    def __repr__(self):
        return f"AudioBook(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
