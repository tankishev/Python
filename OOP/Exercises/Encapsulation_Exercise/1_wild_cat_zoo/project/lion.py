from .animal import Animal


class Lion(Animal):

    _MONEY_FOR_CARE = 50

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, Lion._MONEY_FOR_CARE)
