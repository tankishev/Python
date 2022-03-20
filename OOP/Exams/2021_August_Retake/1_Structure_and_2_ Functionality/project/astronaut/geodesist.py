from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    """The geodesist is a type of astronaut.
    Each geodesist has 50 initial units of oxygen."""

    def __init__(self, name: str) -> None:
        super().__init__(name, 50)
