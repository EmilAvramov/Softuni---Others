from project.rooms.room import Room
from project.appliances.tv import TV


class AlongYoung(Room):
    def __init__(self, family_name: str, salary: float) -> None:
        super().__init__(family_name, salary, 1)
        self.room_cost:int  = 10
        self.appliances: list = [TV()]
        self.expenses: float = 1.5
