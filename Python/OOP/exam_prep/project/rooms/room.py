class Room:
    def __init__(self, name: str, budget: float, members_count: int) -> None:
        self.family_name: str = name
        self.budget: float = budget
        self.members_count: int = members_count
        self.children: list = []
        self._expenses: float = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value: float):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self._expenses = value

    def calculate_expenses(self, *args):
        total = 0
        for arg in args:
            for item in arg:
                total += item * 30
        self._expenses = total
