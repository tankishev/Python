from .product import Product


class Food(Product):

    def __init__(self, name: str, quantity=15) -> None:
        super().__init__(name, quantity)
