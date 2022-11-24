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
        people = 0
        string = []
        new_line = "\n"
        for room in self.rooms:
            people += room.member_count
        string.append(f"Total population: {people}")
        for room in self.rooms:
            result = f"{room.__class__.__name__} with {room.member_count}. Budget: {room.budget}$, Expenses: {room.expenses}$"
            string.append(result)
            if len(room.children) > 0:
                for i in range(len(room.children)):
                    string.append(
                        f"--- Child {i} monthly cost: {room.children[i].cost * 30}$"
                    )
            if len(room.appliances) > 0:
                total = 0
                for appliance in room.appliances:
                    total += appliance.get_monthly_expense()
                string.append(f"Appliances monthly cost: {total}$")
        return new_line.join(string)
