from .dessert import Dessert


class Cake(Dessert):

    GRAMS = 250 
    CALORIES = 1000 
    PRICE = 5 

    # def __init__(self, name: str, price: float, grams: float, calories: float) -> None:
    def __init__(self, name: str) -> None:
        super().__init__(name, Cake.PRICE, Cake.GRAMS, Cake.CALORIES)
