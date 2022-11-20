from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove

class OldCouple(Room):
    def __init__(self, family_name: str, pension_one: float, pension_two: float) -> None:
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove(), Stove()]
        self.expenses = 1.5 + 1.2 + 0.7 + 0.7