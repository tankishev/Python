from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self) -> None:
        self.astronauts = []

    def add(self, astronaut: Astronaut) -> None:
        """Adds an astronaut."""
        pass

    def remove(self, astronaut: Astronaut) -> None:
        """Removes an astronaut from the collection."""
        pass

    def find_by_name(self, name: str) -> Astronaut:
        """Returns an astronaut with that name if he/ she exists."""
        pass
