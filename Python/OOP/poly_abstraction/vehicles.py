from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    def __init__(self, _fuel_quantity: int, _fuel_consumption: int) -> None:
        self.fuel_quantity = _fuel_quantity
        self.fuel_consumption = _fuel_consumption

    def drive(self, _distance):
        if _distance * (self.fuel_consumption + 0.9) <= self.fuel_quantity:
            self.fuel_quantity -= _distance * (self.fuel_consumption + 0.9)

    def refuel(self, _fuel):
        self.fuel_quantity += _fuel


class Truck(Vehicle):
    def __init__(self, _fuel_quantity: int, _fuel_consumption: int) -> None:
        self.fuel_quantity = _fuel_quantity
        self.fuel_consumption = _fuel_consumption

    def drive(self, _distance):
        if _distance * (self.fuel_consumption + 1.6) <= self.fuel_quantity:
            self.fuel_quantity -= _distance * (self.fuel_consumption + 1.6)

    def refuel(self, _fuel):
        self.fuel_quantity += _fuel * 0.95
