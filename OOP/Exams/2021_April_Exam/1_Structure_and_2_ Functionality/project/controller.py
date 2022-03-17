from project import *


class Controller:

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str) -> str:
        if aquarium_type in ("FreshwaterAquarium", "SaltwaterAquarium"):
            new_aquarium = eval(f'{aquarium_type}("{aquarium_name}")')
            self.aquariums.append(new_aquarium)
            return f'Successfully added {aquarium_type}.'
        return 'Invalid aquarium type.'

    def add_decoration(self, decoration_type: str) -> str:
        if decoration_type in ("Ornament", "Plant"):
            eval_str = f'{decoration_type}()'
            new_decoration = eval(eval_str)
            self.decorations_repository.add(new_decoration)
            return f"Successfully added {decoration_type}."
        return f"Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        """
        Finds an existing decoration object from the repository and adds it to the aquarium.
        Returns string indicating if operation is successful.
        """
        found_aquarium = self.__find_aquarium_by_name(aquarium_name)
        if found_aquarium:
            found_decoration = self.decorations_repository.find_by_type(decoration_type)
            if found_decoration != 'None':
                found_aquarium.decorations.append(found_decoration)
                return f"Successfully added {decoration_type} to {aquarium_name}."
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        """
        Create add fish of the given type to an aquarium with the given name if such exists
        """
        if fish_type in ("FreshwaterFish", "SaltwaterFish"):
            new_fish = eval(f'{fish_type}("{fish_name}", "{fish_species}", {price})')
            found_aquarium = self.__find_aquarium_by_name(aquarium_name)
            if found_aquarium:
                if found_aquarium.aquarium_type != new_fish.allowed_habitat:
                    return f"Water not suitable."
                return found_aquarium.add_fish(new_fish)
        return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name: str) -> str:
        found_aquarium = self.__find_aquarium_by_name(aquarium_name)
        if found_aquarium:
            found_aquarium.feed()
            return f"Fish fed: {len(found_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str) -> str:
        found_aquarium = self.__find_aquarium_by_name(aquarium_name)
        if found_aquarium:
            retval = found_aquarium.aquarium_value
            return f"The value of Aquarium {aquarium_name} is {retval:.2f}."

    def report(self) -> str:
        retval = '\n'.join([str(el) for el in self.aquariums])
        return retval

    def __find_aquarium_by_name(self, aquarium_name: str) -> BaseAquarium:
        """
        Finds and returns an aquarium object with the given name from the aquariums list.
        Returns None if no matches found.
        """
        if aquarium_name in [a.name for a in self.aquariums]:
            return next(el for el in self.aquariums if el.name == aquarium_name)
