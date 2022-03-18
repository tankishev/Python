from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):

    __CAPACITY = 50

    def __init__(self, name: str) -> None:
        super().__init__(name, self.__class__.__CAPACITY)
