class Child:
    def __init__(self, food_cost: int, *toys_cost) -> None:
        self.cost = food_cost + sum(toys_cost)
