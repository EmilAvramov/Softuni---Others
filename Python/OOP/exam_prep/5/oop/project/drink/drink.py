from abc import ABC


class Drink(ABC):
    def __init__(
        self, name: str, portion: float, price: float, brand: str
    ) -> None:
        self.__name = name
        self.__portion = portion
        self.price = price
        self.__brand = brand

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value: float):
        if value <= 0:
            raise ValueError("Portion cannot be less than or equal to zero!")
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value: str):
        if value.strip() == "":
            raise ValueError("Brand cannot be empty string or white space!")
        self.__brand = value

    def __repr__(self) -> str:
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"
