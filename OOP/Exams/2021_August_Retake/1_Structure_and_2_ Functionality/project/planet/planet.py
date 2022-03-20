class Planet:

    def __init__(self) -> None:
        self.name = None
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isspace() or value == '':
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value
