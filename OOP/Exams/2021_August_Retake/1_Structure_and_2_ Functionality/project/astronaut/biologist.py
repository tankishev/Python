from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    """Each biologist has 70 initial units of oxygen, and
    each time they take a breath, their oxygen is decreased by 5 units."""

    _BREATHE_UNITS = 5

    def __init__(self, name: str) -> None:
        super().__init__(name, 70)
