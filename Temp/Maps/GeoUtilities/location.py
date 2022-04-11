from abc import ABC, abstractmethod


class Location(ABC):

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass
