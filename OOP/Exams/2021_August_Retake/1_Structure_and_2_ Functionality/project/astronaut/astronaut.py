from abc import ABC, abstractmethod


class Astronaut(ABC):

    _BREATHE_UNITS = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int) -> None:
        """The __init__ method should have a name, a given amount of oxygen, and a backpack."""
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    def breathe(self) -> None:
        """Each time an astronaut takes a breath, their oxygen decreases by 10 units.
        Note: some types of astronauts need more oxygen units while breathing."""
        self.oxygen -= self.__class__._BREATHE_UNITS

    def increase_oxygen(self, amount: int) -> None:
        """Increases the oxygen with the given amount."""
        self.oxygen += amount

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isspace() or value == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @property
    def breaths_left(self) -> int:
        return self.oxygen // self.__class__._BREATHE_UNITS

    def get_item(self, item) -> None:
        self.backpack.append(item)
        self.breathe()

    @property
    def info(self):
        bag_items = '"none"'
        if len(self.backpack) > 0:
            bag_items = ', '.join(self.backpack)

        retval = f'Name: {self.name}' \
                 f'\nOxygen: {self.oxygen}' \
                 f'\nBackpack items: {bag_items}'

        return retval
