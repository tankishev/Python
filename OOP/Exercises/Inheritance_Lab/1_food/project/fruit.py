from .food import Food


class Fruit(Food):

    def __init__(self, expiration_date: str) -> None:
        super().__init__(expiration_date)
