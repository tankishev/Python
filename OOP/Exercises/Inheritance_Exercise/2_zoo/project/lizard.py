from .reptile import Reptile


class Lizard(Reptile):

    def __init__(self, name: str) -> None:
        super().__init__(name)
