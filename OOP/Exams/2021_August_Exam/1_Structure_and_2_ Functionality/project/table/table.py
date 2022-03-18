from abc import ABC, abstractmethod
from project.drink.drink import Drink
from project.baked_food.baked_food import BakedFood


class Table(ABC):

    @abstractmethod
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people: int):
        if not self.is_reserved:
            self.number_of_people = number_of_people
            self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        retval = sum(el.price for el in self.food_orders)
        retval += sum(el.price for el in self.drink_orders)
        return retval

    def clear(self):
        self.number_of_people = 0
        self.drink_orders.clear()
        self.food_orders.clear()
        self.is_reserved = False

    def free_table_info(self):
        if not self.is_reserved:
            retval = f"Table: {self.table_number}" \
                     f"\nType: {self.__class__.__name__}" \
                     f"\nCapacity: {self.capacity}"
            return retval
