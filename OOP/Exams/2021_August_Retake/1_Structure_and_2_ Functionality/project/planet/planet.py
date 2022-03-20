class Planet:

    def __init__(self) -> None:
        self.name = 'None'
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.isspace() or value == '':
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value

    @classmethod
    def from_name_items(cls, name: str, items: str):
        new_planet = cls()
        new_planet.name = name
        new_planet.items = [el for el in items.split(', ')]
        return new_planet

    @property
    def info(self):
        items_info = '\n - '.join(self.items)
        retval = f'Planet name: {self.name}' \
                 f'\nItems:' \
                 f'\n - {items_info}'
        return retval
