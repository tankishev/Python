# Create separate file for each class as shown below and submit a zip file containing all files
# (zip the whole project folder/module) - it is important to include all files in project module
# to be able to make proper imports.
# Create a class called Player. Upon initialization, it should receive:
# •	Private attribute name: string
# •	Private attribute sprint: int
# •	Private attribute dribble: int
# •	Private attribute passing: int
# •	Private attribute shooting: int
# You should create property only for the name of the player. The class should also have one additional method:
# Override the __str__() method of the class, so it returns:
# "Player: {name}
# Sprint: {sprint}
# Dribble: {dribble}
# Passing: {passing}
# Shooting: {shooting}"


class Player:

    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int) -> None:
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    def __str__(self) -> str:
        return f"Player: {self.__name}" \
               f"\nSprint: {self.__sprint}" \
               f"\nDribble: {self.__dribble}" \
               f"\nPassing: {self.__passing}" \
               f"\nShooting: {self.__shooting}"
