from .motorcycle import Motorcycle


class RaceMotorcycle(Motorcycle):

    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, *args) -> None:
        super().__init__(*args)
