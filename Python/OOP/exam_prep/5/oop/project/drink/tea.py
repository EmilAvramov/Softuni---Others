from project.drink.drink import Drink

class Tea(Drink):
    def __init__(self, name: str, portion: float, brand: str) -> None:
        super().__init__(name, portion, 2.5, brand)