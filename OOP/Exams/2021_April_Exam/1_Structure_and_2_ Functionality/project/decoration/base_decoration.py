from abc import ABC, abstractmethod


class BaseDecoration(ABC):

    @abstractmethod
    def __init__(self, comfort: int, price: float) -> None:
        self.comfort = comfort
        self.price = price

    @property
    def decoration_type(self):
        return self.__class__.__name__
