from project.animals.animal import Animal
from abc import ABC, abstractmethod


class Mammal(Animal, ABC):

    @abstractmethod
    def __init__(self, name: str, weight: float, living_region: str, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"


class Mouse(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Vegetable', 'Fruit']

    @property
    def weight_gain(self):
        return 0.10

    @staticmethod
    def make_sound():
        return "Squeak"


class Dog(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @staticmethod
    def make_sound():
        return "Woof!"

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_gain(self):
        return 0.40


class Cat(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Meat', 'Vegetable']

    @property
    def weight_gain(self):
        return 0.30

    @staticmethod
    def make_sound():
        return "Meow"


class Tiger(Mammal):

    def __init__(self, name: str, weight: float, living_region: str):
        super().__init__(name, weight, living_region)

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_gain(self):
        return 1

    @staticmethod
    def make_sound():
        return "ROAR!!!"
