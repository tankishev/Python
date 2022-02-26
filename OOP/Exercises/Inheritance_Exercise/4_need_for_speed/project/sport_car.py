from .car import Car


class SportCar(Car):

    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, *args) -> None:
        super().__init__(*args)
