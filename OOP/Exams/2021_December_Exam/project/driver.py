from project.car.car import Car


class Driver:

    def __init__(self, name: str) -> None:
        self.name = name
        self.car = None
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def car(self):
        return self.__car

    @car.setter
    def car(self, value: Car):
        self.__car = value
