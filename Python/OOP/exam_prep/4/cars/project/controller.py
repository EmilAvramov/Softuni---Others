from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self) -> None:
        self.cars: list = []
        self.drivers: list = []
        self.races: list = []

    def model_exists(self, model: str):
        for car in self.cars:
            if car.model == model:
                return True
        return False

    def driver_exists(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                return True
        return False

    def race_exists(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return True
        return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        valid_cars = ["MuscleCar", "SportsCar"]
        if car_type in valid_cars:
            if self.model_exists(model) is False:
                if car_type == "MuscleCar":
                    car = MuscleCar(model, speed_limit)
                    self.cars.append(car)
                elif car_type == "SportsCar":
                    car = SportsCar(model, speed_limit)
                    self.cars.append(car)
                return f"{car_type} {model} is created."
            else:
                raise Exception(f"Car {model} is already created!")

    def create_driver(self, driver_name: str):
        if self.driver_exists(driver_name) is False:
            driver = Driver(driver_name)
            self.drivers.append(driver)
            return f"Driver {driver_name} is created."
        else:
            raise Exception(f"Driver {driver_name} is already created!")

    def create_race(self, race_name: str):
        if self.race_exists(race_name) is False:
            race = Race(race_name)
            self.races.append(race)
            return f"Race {race_name} is created."
        else:
            raise Exception(f"Race {race_name} is already created!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        pass

    def add_driver_to_race(self, race_name: str, driver_name: str):
        pass

    def start_race(self, race_name: str):
        pass
