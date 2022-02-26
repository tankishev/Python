from .animal import Animal


class Dog(Animal):

    def __init__(self) -> None:
        super().__init__()

    def bark(self) -> str:
        return 'barking...'
