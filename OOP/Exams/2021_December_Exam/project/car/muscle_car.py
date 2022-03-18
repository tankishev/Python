from project.car.car import Car


class MuscleCar(Car):

    __MIN_SPEED_LIMIT = 250
    __MAX_SPEED_LIMIT = 400

    def __init__(self, model: str, speed_limit: int):
        super().__init__(model, speed_limit)
