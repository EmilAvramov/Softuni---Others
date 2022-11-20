class Room:
    def __init__(self, name: str, budget: float, members_count: int) -> None:
        self.family_name: str = name
        self.budget: float = budget
        self.members_count: int = members_count
        self.children: list = []
        self.expenses: int = 0

    def set_expenses(self, value: int):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.expenses = value

    def calculate_expenses(self, *args):
        total = 0
        for arg in args:
            for item in arg:
                total += item.cost
        self.expenses = total * 30
