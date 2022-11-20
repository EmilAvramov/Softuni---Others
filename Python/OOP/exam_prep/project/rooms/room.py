class Room:
    def __init__(self, family_name: str, budget: float, members_count: float) -> None:
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children: list = []
        self.expenses: int = 0

    def set_expenses(self, value: int): 
        if value < 0:
            raise ValueError("Expenses cannot be negative")           
        self.expenses = value
    
    def calculate_expenses(self, *args):
        total = 0
        for arg in args:
            total += arg.cost
        self.expenses = total