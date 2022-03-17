from abc import ABC, abstractmethod
from project.fish.base_fish import BaseFish
from project.decoration.base_decoration import BaseDecoration


class BaseAquarium(ABC):

    @abstractmethod
    def __init__(self, name: str, capacity: int) -> None:
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self) -> int:
        return sum(decoration.comfort for decoration in self.decorations)

    def add_fish(self, fish: BaseFish) -> str:
        if self.capacity <= len(self.fish):
            return "Not enough capacity."
        self.fish.append(fish)
        return f"Successfully added {fish.fish_type} to {self.name}."

    def remove_fish(self, fish: BaseFish) -> None:
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def feed(self) -> None:
        for fish in self.fish:
            fish.eat()

    def __str__(self) -> str:
        fish_list = [self.fish[i].name if i < len(self.fish) else 'none' for i in range(self.capacity)]
        retval = f'{self.name}:' \
                 f'\nFish: {" ".join(fish_list)}' \
                 f'\nDecorations: {len(self.decorations)}' \
                 f'\nComfort: {self.calculate_comfort()}'
        return retval

    @property
    def aquarium_value(self):
        retval = sum(decoration.price for decoration in self.decorations)
        retval += sum(fish.price for fish in self.fish)
        return retval

    @property
    def aquarium_type(self):
        return self.__class__.__name__
