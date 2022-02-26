from .animal import Animal


class Mammal(Animal):

    def __init__(self, name: str) -> None:
        super().__init__(name)
