from .animal import Animal


class Tiger(Animal):

    _MONEY_FOR_CARE = 45

    def __init__(self, name: str, gender: str, age: int) -> None:
        super().__init__(name, gender, age, Tiger._MONEY_FOR_CARE)
