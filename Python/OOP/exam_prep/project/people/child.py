class Child:
    def __init__(self, food_cost: int, *toys_cost) -> None:
        self.cost: float = food_cost + sum(x for x in toys_cost)
