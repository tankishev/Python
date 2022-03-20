from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    """The meteorologist is a type of astronaut. Each meteorologist has 90 initial units of oxygen, and
    each time they take a breath, their oxygen is decreased by 15 units."""

    _BREATHE_UNITS = 15

    def __init__(self, name: str) -> None:
        super().__init__(name, 90)
