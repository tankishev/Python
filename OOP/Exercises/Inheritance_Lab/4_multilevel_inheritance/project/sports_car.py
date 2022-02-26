from .car import Car


class SportsCar(Car):

    def __init__(self) -> None:
        super().__init__()

    def race(self) -> str:
        return 'racing...'
