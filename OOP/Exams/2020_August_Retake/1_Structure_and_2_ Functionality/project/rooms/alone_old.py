from project.rooms.room import Room


class AloneOld(Room):

    _ROOM_COST = 10
    _MEMBERS_COUNT = 1

    def __init__(self, family_name: str, pension: float) -> None:
        super().__init__(family_name, pension, self.__class__._MEMBERS_COUNT)
        self.room_cost = self.__class__._ROOM_COST
        self.appliances = self.__class__._APPLIANCES * self.members_count
