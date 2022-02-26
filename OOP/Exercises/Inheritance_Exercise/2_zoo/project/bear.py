from .mammal import Mammal


class Bear(Mammal):

    def __init__(self, name: str) -> None:
        super().__init__(name)
