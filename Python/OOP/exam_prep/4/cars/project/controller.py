from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver


class Controller:
    def __init__(self) -> None:
        self.cars: list = []
        self.drivers: list = []
        self.races: list = []
