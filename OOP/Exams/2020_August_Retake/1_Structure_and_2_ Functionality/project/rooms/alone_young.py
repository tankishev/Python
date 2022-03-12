from project.rooms.room import Room
from project.appliances.tv import TV


class AloneYoung(Room):

    _ROOM_COST = 10
    _APPLIANCES = [TV()]
    _MEMBERS_COUNT = 1

    def __init__(self, family_name: str, salary: float) -> None:
        super().__init__(family_name, salary, self.__class__._MEMBERS_COUNT)
        self.room_cost = self.__class__._ROOM_COST
        self.appliances = self.__class__._APPLIANCES * self.members_count
        self.calculate_expenses(self.appliances)
