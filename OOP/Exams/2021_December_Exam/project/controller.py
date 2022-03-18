from project.car.car import Car
from project.race import Race
from project.driver import Driver


class Controller:

    def __init__(self) -> None:
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        pass

    def create_driver(self, driver_name: str):
        pass

    def create_race(self, race_name: str):
        pass

    def add_car_to_driver(self, driver_name: str, car_type: str):
        pass

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name: str):
        pass
