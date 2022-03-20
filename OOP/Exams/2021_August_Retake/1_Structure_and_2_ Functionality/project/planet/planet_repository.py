from project.planet.planet import Planet


class PlanetRepository:

    def __init__(self) -> None:
        self.planets = []

    def add(self, planet: Planet) -> None:
        """Adds a planet for exploration."""
        self.planets.append(planet)

    def remove(self, planet: Planet) -> None:
        """Removes a planet from the collection."""
        self.planets.remove(planet)

    def find_by_name(self, name: str) -> Planet:
        """Returns a planet with that name if it exists."""
        for planet in self.planets:
            if planet.name == name:
                return planet
