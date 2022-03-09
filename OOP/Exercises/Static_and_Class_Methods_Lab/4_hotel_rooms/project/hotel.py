from .room import Room


class Hotel:

    def __init__(self, name: str) -> None:
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room) -> None:
        if all([r.number != room.number for r in self.rooms]):
            self.rooms.append(room)

    def take_room(self, room_number: int, people: int) -> None:
        try:
            room = next(room for room in self.rooms if room.number == room_number)
            return room.take_room(people)
        except StopIteration:
            pass

    def free_room(self, room_number: int) -> None:
        try:
            room = next(room for room in self.rooms if room.number == room_number)
            return room.free_room()
        except StopIteration:
            pass

    def status(self) -> str:
        retval = f'Hotel {self.name} has {self.guests} total guests' \
                 f'\nFree rooms: {self.__find_rooms(is_taken=False)}' \
                 f'\nTaken rooms: {self.__find_rooms(is_taken=True)}'
        return retval

    def __find_rooms(self, is_taken: bool) -> str:
        return ', '.join([str(room.number) for room in self.rooms if room.is_taken == is_taken])
