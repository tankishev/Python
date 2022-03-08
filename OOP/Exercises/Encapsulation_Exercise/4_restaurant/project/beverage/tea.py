from .hot_beverage import HotBeverage


class Tea(HotBeverage):

    def __init__(self, name: str, price: float, milliliters: float) -> None:
        super().__init__(name, price, milliliters)
