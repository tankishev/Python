from .car import Car


class FamilyCar(Car):

    def __init__(self, *args) -> None:
        super().__init__(*args)
