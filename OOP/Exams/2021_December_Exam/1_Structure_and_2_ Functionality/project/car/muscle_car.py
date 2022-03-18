from project.car.car import Car


class MuscleCar(Car):

    _MIN_SPEED_LIMIT = 250
    _MAX_SPEED_LIMIT = 450

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)
