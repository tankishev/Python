from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):

    __INITIAL_SIZE = 3
    __ALLOWED_HABITAT = 'FreshwaterAquarium'

    def __init__(self, name: str, species: str, price: float) -> None:
        super().__init__(name, species, self.__class__.__INITIAL_SIZE, price)

    @property
    def allowed_habitat(self):
        return self.__class__.__ALLOWED_HABITAT

    def eat(self) -> None:
        self.size += 3
