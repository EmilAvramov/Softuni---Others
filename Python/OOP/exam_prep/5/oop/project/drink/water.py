from project.drink.drink import Drink


class Water(Drink):
    def __init__(self, name: str, portion: float, brand: str) -> None:
        super().__init__(name, portion, 1.5, brand)
