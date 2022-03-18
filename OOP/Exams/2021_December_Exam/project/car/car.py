from abc import ABC, abstractmethod


class Car(ABC):

    __MIN_SPEED_LIMIT = 0
    __MAX_SPEED_LIMIT = 0

    @abstractmethod
    def __init__(self, model: str, speed_limit: int) -> None:
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value
        
    @property
    def speed_limit(self):
        return self.__speed_limit
    
    @speed_limit.setter
    def speed_limit(self, value):
        min_limit = self.__class__.__MIN_SPEED_LIMIT
        max_limit = self.__class__.__MIN_SPEED_LIMIT
        if value < min_limit or value > max_limit:
            raise ValueError(f"Invalid speed limit! Must be between {min_limit} and {max_limit}!")
        self.__speed_limit = value
