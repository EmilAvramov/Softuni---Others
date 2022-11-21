from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCouple(Room):
    def __init__(
        self, family_name: str, salary_one: float, salary_two: float
    ) -> None:
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost: int = 20
        self.appliances: list = [
            TV(),
            Fridge(),
            Laptop(),
            TV(),
            Fridge(),
            Laptop(),
        ]
        self.expenses: float = self.calculate_expenses(
            [x.cost for x in self.appliances]
        )
