from .animal import Animal


class Cheetah(Animal):

    _MONEY_FOR_CARE = 60

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, Cheetah._MONEY_FOR_CARE)
