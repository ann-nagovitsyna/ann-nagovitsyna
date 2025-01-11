import doctest

class Tree:
    def __init__(self, species: str, height: float, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param species: Вид дерева
        :param height: Высота дерева в метрах
        :param age: Возраст дерева в годах

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если значения аргументов не допустимы (например, отрицательные значения)

        Примеры:
        >>> tree = Tree("Береза", 5.5, 10)
        """
        if not isinstance(species, str):
            raise TypeError("Вид дерева должен быть строкой")
        if not isinstance(height, (int, float)):
            raise TypeError("Высота дерева должна быть числом")
        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть целым числом")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительным числом")
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")

        self.species = species
        self.height = height
        self.age = age

    def grow(self, meters: float) -> None:
        """
        Увеличивает высоту дерева.

        :param meters: Количество метров для добавления к текущей высоте

        :raise TypeError: Если meters не число
        :raise ValueError: Если meters отрицательно

        Примеры:
        >>> tree = Tree("Сосна", 3.0, 5)
        >>> tree.grow(0.5)
        """
        if not isinstance(meters, (int, float)):
            raise TypeError("Количество метров должно быть числом")
        if meters < 0:
            raise ValueError("Количество метров не может быть отрицательным")
        ...

    def age_one_year(self) -> None:
        """
        Увеличивает возраст дерева на один год.

        Примеры:
        >>> tree = Tree("Ель", 4.0, 20)
        >>> tree.age_one_year()
        """
        ...


class Stack:
    def __init__(self, max_size: int = 100):
        """
        Создание и подготовка к работе объекта "Стек"

        :param max_size: Максимальный размер стека

        :raise TypeError: Если max_size не целое число
        :raise ValueError: Если max_size не положительное

        Примеры:
        >>> stack = Stack(50)
        """
        if not isinstance(max_size, int):
            raise TypeError("Максимальный размер стека должен быть целым числом")
        if max_size <= 0:
            raise ValueError("Максимальный размер стека должен быть положительным")
        self.max_size = max_size
        self.items = []

    def push(self, item: any) -> None:
        """
        Добавляет элемент в стек.

        :param item: Элемент для добавления

        :raise OverflowError: Если стек уже полон

        Примеры:
        >>> stack = Stack(2)
        >>> stack.push(1)
        >>> stack.push(2)
        """
        if len(self.items) >= self.max_size:
            raise OverflowError("Стек переполнен")
        self.items.append(item)
        ...

    def pop(self) -> any:
        """
        Удаляет и возвращает верхний элемент стека.

        :return: Верхний элемент стека

        :raise IndexError: Если стек пуст

        Примеры:
        >>> stack = Stack(2)
        >>> stack.push('a')
        >>> stack.pop()
        'a'
        """
        if not self.items:
            raise IndexError("Стек пуст")
        return self.items.pop()
        ...


class SocialMediaPlatform:
    def __init__(self, name: str, users_count: int = 0, is_active: bool = True):
        """
        Создание и подготовка к работе объекта "Социальная Платформа"

        :param name: Название платформы
        :param users_count: Количество пользователей
        :param is_active: Статус активности платформы

        :raise TypeError: Если типы аргументов не соответствуют ожидаемым
        :raise ValueError: Если users_count отрицательно

        Примеры:
        >>> platform = SocialMediaPlatform("MySocial")
        """
        if not isinstance(name, str):
            raise TypeError("Название платформы должно быть строкой")
        if not isinstance(users_count, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        if not isinstance(is_active, bool):
            raise TypeError("Статус активности должен быть булевым значением")

        self.name = name
        self.users_count = users_count
        self.is_active = is_active

    def add_user(self, number: int = 1) -> None:
        """
        Добавляет указанное количество пользователей к платформе.

        :param number: Количество пользователей для добавления

        :raise TypeError: Если number не целое число
        :raise ValueError: Если number отрицательно

        Примеры:
        >>> platform = SocialMediaPlatform("ChatSpace", 100)
        >>> platform.add_user(50)
        """
        if not isinstance(number, int):
            raise TypeError("Количество пользователей должно быть целым числом")
        if number < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")
        self.users_count += number
        ...

    def deactivate_platform(self) -> None:
        """
        Деактивирует платформу.

        Примеры:
        >>> platform = SocialMediaPlatform("QuietNet")
        >>> platform.deactivate_platform()
        """
        self.is_active = False
        ...


if __name__ == "__main__":
    doctest.testmod()