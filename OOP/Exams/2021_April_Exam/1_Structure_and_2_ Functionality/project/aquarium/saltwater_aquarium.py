from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):

    __CAPACITY = 25

    def __init__(self, name: str) -> None:
        super().__init__(name, self.__class__.__CAPACITY)
