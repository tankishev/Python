from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self) -> None:
        self.astronauts = []

    def add(self, astronaut: Astronaut) -> None:
        """Adds an astronaut."""
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut) -> None:
        """Removes an astronaut from the collection."""
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Astronaut:
        """Returns an astronaut with that name if he/ she exists."""
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut

    def find_top_five(self, filter_type: str) -> list:

        if filter_type == 'oxygen':
            results = list(filter(lambda x: x.oxygen >= 30, sorted(self.astronauts, key=lambda x: -x.oxygen)))
            return results[:5]
        elif filter_type == 'breaths_left':
            results = list(filter(lambda x: x.oxygen >= 30, sorted(self.astronauts, key=lambda x: -x.breaths_left)))
            return results[:5]
