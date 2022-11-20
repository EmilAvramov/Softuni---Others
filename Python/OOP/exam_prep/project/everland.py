from project.rooms.room import Room


class Everland:
    def __init__(self) -> None:
        self.rooms: list = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses
            total_consumption += room.room_cost
        return f"Monthly consumption: {total_consumption}$."

    def pay(self):
        string = []
        new_line = "\n"
        for room in self.rooms:
            totals = room.room_cost + room.expenses
            if room.budget >= totals:
                room.budget -= totals
                string.append(
                    f"{room.family_name} paid {totals}$ and have {room.budget}$ left."
                )
            else:
                string.append(
                    f"{room.family_name} does not have enough budget and must leave the hotel."
                )
                self.rooms.remove(room)
        return new_line.join(string)

    def status(self):
        pass
