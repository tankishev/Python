from .main_dish import MainDish


class Salmon(MainDish):

    GRAMS = 22

    #  def __init__(self, name: str, price: float, grams: float) -> None:
    def __init__(self, name: str, price: float) -> None:
        super().__init__(name, price, Salmon.GRAMS)
