class Race:

    def __init__(self, name: str) -> None:
        self.name = name
        self.drivers = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value
