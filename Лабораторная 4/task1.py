class Conifer:
    """
    Базовый класс, описывающий хвойное дерево.

    Attributes:
        name (str): Название дерева.
        age (int): Возраст дерева в годах.
        height (float): Высота дерева в метрах.

    Непубличный атрибут:
        _health_status (str): Текущее состояние здоровья дерева.
        Делаем этот атрибут непубличным, чтобы избежать прямого доступа
        и некорректного изменения состояния здоровья извне.
    """

    def __init__(self, name: str, age: int, height: float) -> None:
        """
        Инициализирует объект хвойного дерева.

        Args:
            name (str): Название дерева.
            age (int): Возраст дерева.
            height (float): Высота дерева.
        """
        self.name: str = name
        self.age: int = age
        self.height: float = height
        self._health_status: str = "Healthy"

    def __str__(self) -> str:
        """
        Магический метод, отвечающий за строковое представление объекта.
        Возвращает читабельное описание дерева.
        """
        return f"Conifer(name={self.name}, age={self.age}, height={self.height})"

    def __repr__(self) -> str:
        """
        Магический метод, отвечающий за формальное строковое представление объекта.
        Возвращает подробное описание для отладочных целей.
        """
        return (f"Conifer(name={self.name!r}, age={self.age!r}, "
                f"height={self.height!r}, health_status={self._health_status!r})")

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст и высоту дерева, имитируя рост за указанное количество лет.

        Args:
            years (int): Количество лет, на которое дерево "стареет".
        """
        self.age += years
        self.height += 0.5 * years

    def photosynthesize(self) -> str:
        """
        Имитирует процесс фотосинтеза у хвойного дерева.

        Returns:
            str: Сообщение о фотосинтезе.
        """
        return f"{self.name} is photosynthesizing under the sun!"
    

class Spruce(Conifer):
    """
    Дочерний класс, описывающий ель как конкретное хвойное дерево.

    Наследует все атрибуты и методы от класса Conifer, 
    но переопределяет некоторые из них под особенности ели.
    """

    def __init__(self, name: str, age: int, height: float, cone_count: int) -> None:
        """
        Инициализирует объект ели.

        Args:
            name (str): Название дерева (ель).
            age (int): Возраст дерева.
            height (float): Высота дерева.
            cone_count (int): Количество шишек на ели.
        """
        super().__init__(name, age, height)
        self.cone_count: int = cone_count

    def __str__(self) -> str:
        """
        Переопределённый магический метод для строкового представления объекта.
        Возвращает читабельное описание ели.
        """
        return f"Spruce(name={self.name}, age={self.age}, height={self.height}, cones={self.cone_count})"

    def __repr__(self) -> str:
        """
        Переопределённый магический метод для формального строкового представления объекта.
        """
        return (f"Spruce(name={self.name!r}, age={self.age!r}, "
                f"height={self.height!r}, cone_count={self.cone_count!r}, "
                f"health_status={self._health_status!r})")

    def photosynthesize(self) -> str:
        """
        Переопределённый метод фотосинтеза под особенности ели.

        Returns:
            str: Сообщение о фотосинтезе ели.
        
        Причина переопределения:
            У ели могут быть отличия в интенсивности и особенностях фотосинтеза 
            по сравнению с обобщённым хвойным деревом.
        """
        return f"{self.name} (Spruce) is photosynthesizing in a cool, shaded forest!"

    def produce_cones(self, new_cones: int) -> None:
        """
        Увеличивает количество шишек у ели.

        Args:
            new_cones (int): Количество новых шишек.
        """
        self.cone_count += new_cones


if __name__ == "__main__":
    conifer_tree = Conifer("Generic Conifer", 10, 2.5)
    print(conifer_tree)
    print(repr(conifer_tree))
    print(conifer_tree.photosynthesize())

    spruce_tree = Spruce("Blue Spruce", 5, 1.2, 10)
    print(spruce_tree)
    print(repr(spruce_tree))
    print(spruce_tree.photosynthesize())
    spruce_tree.grow(3)
    spruce_tree.produce_cones(5)
    print(spruce_tree)