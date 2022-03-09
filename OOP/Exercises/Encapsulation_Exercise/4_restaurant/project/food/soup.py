from .starter import Starter


class Soup(Starter):

    def __init__(self, name: str, price: float, grams: float) -> None:
        super().__init__(name, price, grams)
