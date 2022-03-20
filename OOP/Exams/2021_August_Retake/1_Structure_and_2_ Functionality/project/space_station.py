from project.planet.planet_repository import PlanetRepository, Planet
from project.astronaut.astronaut_repository import AstronautRepository, Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from collections import deque

class ObjectFactory:

    @staticmethod
    def create_astronaut(astronaut_type, name) -> Astronaut:
        if astronaut_type == "Biologist":
            return Biologist(name)
        elif astronaut_type == "Geodesist":
            return Geodesist(name)
        elif astronaut_type == "Meteorologist":
            return Meteorologist(name)


class SpaceStation:

    def __init__(self) -> None:
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.missions = {'successful': 0, 'failed': 0}

    def add_astronaut(self, astronaut_type: str, name: str) -> str:

        if astronaut_type in ("Biologist", "Geodesist", "Meteorologist"):
            if self.astronaut_repository.find_by_name(name):
                return f"{name} is already added."
            new_astronaut = ObjectFactory.create_astronaut(astronaut_type, name)
            self.astronaut_repository.add(new_astronaut)
            return f"Successfully added {astronaut_type}: {name}."
        raise Exception("Astronaut type is not valid!")

    def add_planet(self, name: str, items: str) -> str:

        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."
        new_planet = Planet.from_name_items(name, items)
        self.planet_repository.add(new_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str) -> str:

        found_astronaut = self.astronaut_repository.find_by_name(name)
        if found_astronaut:
            self.astronaut_repository.remove(found_astronaut)
            return f"Astronaut {name} was retired!"
        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self) -> None:
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str) -> str:
        """
        •	You should start by choosing the astronauts that are most suitable for the mission:
        o	You should pick up to 5 astronauts with the highest amount of oxygen among the ones with oxygen above 30 units.
        o	If you don't have any suitable astronauts, raise an Exception with the following message:
                "You need at least one astronaut to explore the planet!"
        •	The astronauts start going out in open space one by one, sorted in descending order by the amount of oxygen they have:
        o	An astronaut lands on a planet and starts collecting its items one by one starting from the last one in the collection.
            Each time he/she finds an item he/she takes a breath.
        o	If an astronaut runs out of oxygen, he/ she should return to the space station, and the next astronaut starts exploring.
        •	A mission is successful when all the items from the planet are collected:
        o	If it is successful, return the following message, with the name of the explored planet and the number of
        the astronauts that had gone out in open space: "Planet: {planet_name} was explored. {astronauts} astronauts participated in collecting items."
        o	Otherwise, return: "Mission is not completed."
        """
        selected_planet = self.planet_repository.find_by_name(planet_name)
        if selected_planet:
            astronauts = deque(self.astronaut_repository.find_top_five('oxygen'))
            if len(astronauts) > 0:
                items = selected_planet.items
                sent_to_explore = 0
                while astronauts and items:
                    astronaut = astronauts.popleft()
                    sent_to_explore += 1
                    while astronaut.breaths_left > 0 and items:
                        item = items.pop()
                        astronaut.get_item(item)

                if items:
                    self.missions['failed'] += 1
                    return "Mission is not completed."

                self.missions['successful'] += 1
                return f"Planet: {planet_name} was explored. " \
                       f"{sent_to_explore} astronauts participated in collecting items."

            raise Exception("You need at least one astronaut to explore the planet!")
        raise Exception("Invalid planet name!")

    def report(self) -> str:
        retval = f"{self.missions.get('successful', 0)} successful missions!" \
                 f"\n{self.missions.get('failed', 0)} missions were not completed!" \
                 f"\nAstronauts' info:"
        retval += '\n' + '\n'.join([astronaut.info for astronaut in self.astronaut_repository.astronauts])
        return retval


if __name__ == '__main__':
    s = SpaceStation()
    s.add_planet('Earth', 'mouse, cat, dog, shit_like_that')
    s.add_planet('Mars', 'dust, rock, alien')
    s.add_planet('Uranus', 'blue rock, red rock, green rock, yellow rock, orange rock, lemon rock, pink rock, black rock, white rock, purple rock, crazy rock, new rock')
    s.add_planet('Uranus2', 'blue rock, red rock, green rock, yellow rock, orange rock, lemon rock, pink rock, black rock, white rock, purple rock, crazy rock, new rock')
    s.add_astronaut('Biologist', 'Marina')
    s.add_astronaut('Geodesist', 'Boryana')
    s.add_astronaut('Meteorologist', 'Bobi')

    a = 5