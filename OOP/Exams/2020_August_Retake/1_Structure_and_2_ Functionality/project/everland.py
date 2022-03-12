from project.rooms.room import Room


class Everland:

    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        if not any(r.family_name == room.family_name for r in self.rooms):
            self.rooms.append(room)

    def get_monthly_consumptions(self):
        monthly_consumption = sum([room.monthly_cost for room in self.rooms])
        return f"Monthly consumption: {monthly_consumption:.2f}$."

    def pay(self):
        retval = ''
        for room in self.rooms:
            successful_payment, message = room.pay_expenses()
            retval += message + '\n'
            if not successful_payment:
                self.rooms.remove(room)
        return retval.rstrip()

    def status(self):
        retval = f'Total population: {sum([room.members_count for room in self.rooms])}\n'
        retval += '\n'.join([room.status() for room in self.rooms])
        return retval
