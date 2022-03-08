from .dough import Dough
from .topping import Topping
from .data_descriptors import PositiveNum, NonEmptyString


class Pizza:

    name = NonEmptyString('The name cannot be an empty string')
    toppings_capacity = PositiveNum("The topping's capacity cannot be less or equal to zero")

    def __init__(self, name: str, dough: Dough, toppings_capacity: int) -> None:
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = {}

    def add_topping(self, topping: Topping) -> None:
        if len(self.toppings.keys()) == self.toppings_capacity:
            raise ValueError('Not enough space for another topping')

        if topping.topping_type not in self.toppings.keys():
            self.toppings[topping.topping_type] = 0
        self.toppings[topping.topping_type] += topping.weight

    def calculate_total_weight(self) -> int:
        return self.dough.weight + sum(self.toppings.values())

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError('You should add dough to the pizza')
        self.__dough = value
