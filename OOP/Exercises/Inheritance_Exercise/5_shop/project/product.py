class Product:

    def __init__(self, name: str, quantity: int) -> None:
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity: int) -> None:
        if self.quantity >= quantity:
            self.quantity -= quantity

    def increase(self, quantity: int) -> None:
        self.quantity += quantity
