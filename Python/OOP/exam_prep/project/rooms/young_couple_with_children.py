from project.rooms.room import Room
from project.appliances.tv import TV
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop


class YoungCoupleWithChildren(Room):
    def __init__(
        self, family_name: str, salary_one: float, salary_two: float, *children
    ) -> None:
        super().__init__(
            family_name, salary_one + salary_two, 2 + len(children)
        )
        self.room_cost: int = 30
        self.children: list = [x for x in children]
        self.appliances: list = [TV(), Fridge(), Laptop(), Laptop()] + [
            Laptop() for _ in range(len(children))
        ]
        self.expenses: float = 3.9 + len(children) + sum(
            x.cost for x in children
        )
