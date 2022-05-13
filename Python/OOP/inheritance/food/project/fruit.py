from project.food import Food


class Fruit(Food):
    def __init__(self, _name: str, _date: str) -> None:
        self.name = _name
        self.expiration_date = _date
