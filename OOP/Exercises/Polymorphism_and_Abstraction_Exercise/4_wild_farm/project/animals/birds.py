from project.animals.animal import Animal
from abc import ABC, abstractmethod


class Bird(Animal, ABC):

    @abstractmethod
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten=0):
        super().__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"


class Owl(Bird):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_foods(self):
        return ['Meat']

    @property
    def weight_gain(self):
        return 0.25

    @staticmethod
    def make_sound():
        return 'Hoot Hoot'


class Hen(Bird):

    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def allowed_foods(self):
        return None

    @property
    def weight_gain(self):
        return 0.35

    @staticmethod
    def make_sound():
        return 'Cluck'
