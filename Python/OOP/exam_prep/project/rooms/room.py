class Room:
    def __init__(self, name: str, budget: float, members_count: int) -> None:
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: list = []
        self.expenses: int = 0

    @property.setter
    def expenses(self, value: int):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.expenses = value

    def calculate_expenses(self, *args):
        total = 0
        for arg in args:
            total += arg.cost
        self.expenses = total * 30
