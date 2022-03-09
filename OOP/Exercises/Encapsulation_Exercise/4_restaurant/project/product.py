class Product:

    def __init__(self, name: str, price: float) -> None:
        self.__name = name
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price
