from abc import ABC, abstractmethod


class Delicacy(ABC):
    def __init__(self, name: str, portion: int, price: float):
        if not name.strip():
            raise ValueError("Name cannot be null or whitespace!")
        if price <= 0:
            raise ValueError("Price cannot be less or equal to zero!")

        self.name = name
        self.portion = portion
        self.price = price

    @abstractmethod
    def details(self):
        pass
