from .vehicle import Vehicle


class Motorcycle(Vehicle):

    def __init__(self, *args) -> None:
        super().__init__(*args)
