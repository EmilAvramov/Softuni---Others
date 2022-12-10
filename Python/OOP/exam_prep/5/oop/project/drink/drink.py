from abc import ABC


class Drink(ABC):
    def __init__(self, name: str, portion: float, price: float, brand: str):
        if name.isspace() or name == "":
            raise ValueError("Name cannot be empty string or white space!")
        if portion <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        if brand.isspace() or brand == "":
            raise ValueError("Brand cannot be empty string or white space!")
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
