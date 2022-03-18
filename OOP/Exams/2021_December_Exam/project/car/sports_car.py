from project.car.car import Car


class SportsCar(Car):

    _MIN_SPEED_LIMIT = 400
    _MAX_SPEED_LIMIT = 600

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)

