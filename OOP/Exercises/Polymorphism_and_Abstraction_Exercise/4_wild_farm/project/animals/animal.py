from abc import ABC, abstractmethod
from project.food import Food


class Animal(ABC):

    def __init__(self, name: str, weight: float, food_eaten=0):
        self.name = name
        self.weight = weight
        self.food_eaten = food_eaten

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

    @property
    @abstractmethod
    def allowed_foods(self):
        pass

    @property
    @abstractmethod
    def weight_gain(self):
        pass

    def feed(self, food: Food):
        food_name = food.__class__.__name__
        if food_name not in self.allowed_foods:
            return f"{self.__class__.__name__} does not eat {food_name}!"
        self.weight += self.weight_gain * food.quantity
        self.food_eaten += food.quantity

    @abstractmethod
    def __repr__(self):
        pass
