class Appliance:
    def __init__(self, cost: float) -> None:
        self.cost: float = cost

    def get_monetary_expense(self):
        return self.cost * 30
