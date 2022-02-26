from .vehicle import Vehicle


class Car(Vehicle):

    DEFAULT_FUEL_CONSUMPTION = 3

    def __init__(self, *args) -> None:
        super().__init__(*args)
