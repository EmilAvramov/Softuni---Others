from abc import ABC


class BakedFood(ABC):
    def __init__(self, name: str, portion: float, price: float) -> None:
        self.__name = name
        self.portion = portion
        self.__price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Price cannot be less than or equal to zero!")
        self.__price = value

    def __repr__(self) -> str:
        return f" - {self.name}: {self.portion:.2f}g - {self.price:.2f}lv"
