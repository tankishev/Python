from project.car.car import Car
from project.race import Race
from project.driver import Driver
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class ObjectFactory:

    @staticmethod
    def create_car(car_type: str, model: str, speed_limit: int):
        if car_type == 'MuscleCar':
            return MuscleCar(model, speed_limit)
        elif car_type == 'SportsCar':
            return SportsCar(model, speed_limit)

    @staticmethod
    def create_driver(driver_name: str):
        return Driver(driver_name)

    @staticmethod
    def create_race(race_name: str):
        return Race(race_name)


class Controller:

    def __init__(self) -> None:
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if any(car.model == model for car in self.cars):
            raise Exception(f"Car {model} is already created!")
        new_car = ObjectFactory.create_car(car_type, model, speed_limit)
        self.cars.append(new_car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        if self.__find_driver_by_name(driver_name):
            raise Exception(f"Driver {driver_name} is already created!")
        new_driver = ObjectFactory.create_driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        if self.__find_race_by_name(race_name):
            raise Exception(f"Race {race_name} is already created!")
        new_race = ObjectFactory.create_race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        found_driver = self.__find_driver_by_name(driver_name)
        if found_driver:
            old_car = found_driver.car
            available_car = self.__find_available_car_by_type(car_type)
            if available_car:
                found_driver.car = available_car
                available_car.is_taken = True
                if old_car:
                    old_car.is_taken = False
                    return f"Driver {driver_name} changed his car from {old_car.model} to {available_car.model}."
                return f"Driver {driver_name} chose the car {available_car.model}."
            raise Exception(f"Car {car_type} could not be found!")
        raise Exception(f"Driver {driver_name} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        found_race = self.__find_race_by_name(race_name)
        if found_race:
            found_driver = self.__find_driver_by_name(driver_name)
            if found_driver:
                if found_driver.car is None:
                    raise Exception(f"Driver {driver_name} could not participate in the race!")
                if any(driver.name == driver_name for driver in found_race.drivers):
                    return f"Driver {driver_name} is already added in {race_name} race."
                found_race.drivers.append(found_driver)
                return f"Driver {driver_name} added in {race_name} race."
            raise Exception(f"Driver {driver_name} could not be found!")
        raise Exception(f"Race {race_name} could not be found!")

    def start_race(self, race_name: str):
        found_race = self.__find_race_by_name(race_name)
        if found_race:
            if len(found_race.drivers) >= 3:
                retval = ''
                race_results = sorted(found_race.drivers, key=lambda driver: -driver.car.speed_limit)[:3]
                for driver in race_results:
                    driver.add_win()
                    retval += f"Driver {driver.name} " \
                              f"wins the {race_name} race " \
                              f"with a speed of {driver.car.speed_limit}.\n"
                return retval.strip()
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        raise Exception(f"Race {race_name} could not be found!")

    def __find_driver_by_name(self, driver_name) -> Driver:
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __find_available_car_by_type(self, car_type) -> Car:
        for car in self.cars[::-1]:
            if car.car_type == car_type and not car.is_taken:
                return car

    def __find_race_by_name(self, race_name: str) -> Race:
        for race in self.races:
            if race.name == race_name:
                return race
