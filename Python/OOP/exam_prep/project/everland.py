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

    def pay():
        pass

    def status():
        pass
