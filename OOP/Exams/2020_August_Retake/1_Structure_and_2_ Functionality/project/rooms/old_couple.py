from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.stove import Stove
from project.appliances.fridge import Fridge


class OldCouple(Room):

    _ROOM_COST = 15
    _APPLIANCES = [TV(), Fridge(), Stove()]
    _MEMBERS_COUNT = 2

    def __init__(self, family_name: str, pension_one: float, pension_two: float) -> None:
        super().__init__(family_name, pension_one + pension_two, self.__class__._MEMBERS_COUNT)
        self.room_cost = self.__class__._ROOM_COST
        self.appliances = self.__class__._APPLIANCES * self.members_count
        self.calculate_expenses(self.appliances)
