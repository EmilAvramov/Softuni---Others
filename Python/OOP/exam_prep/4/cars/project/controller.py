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
                return driver
        return False

    def race_exists(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return race
        return False

    def get_last_free_car(self, car_type: str):
        indexes = [
            i
            for i, v in enumerate(self.cars[::-1])
            if car_type == v.__class__.__name__ and v.is_taken == False
        ]
        if len(indexes) > 1:
            return indexes[-1], self.cars[indexes[-1]]
        elif len(indexes) == 1:
            return indexes[0], self.cars[indexes[0]]
        else:
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
        driver = self.driver_exists(driver_name)
        if driver is not False:
            if car_type == "MuscleCar" or car_type == "SportsCar":
                if self.get_last_free_car(car_type) is not False:
                    index, car = self.get_last_free_car(car_type)
                    if driver.car:
                        old_model = driver.car.model
                        driver.car.is_taken = False
                        driver.car = car
                        self.cars[index].is_taken = True
                        return f"Driver {driver_name} changed his car from {old_model} to {driver.car.model}."
                    else:
                        driver.car = car
                        self.cars[index].is_taken = True
                        return f"Driver {driver_name} chose the car {driver.car.model}."
                else:
                    raise Exception(f"Car {car_type} could not be found!")
            else:
                raise Exception(f"Car {car_type} could not be found!")
        else:
            raise Exception(f"Driver {driver_name} could not be found!")

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.race_exists(race_name)
        if race is not False:
            driver = self.driver_exists(driver_name)
            if driver is not False:
                if driver.car:
                    if driver not in race.drivers:
                        race.drivers.append(driver)
                        return (
                            f"Driver {driver_name} added in {race_name} race."
                        )
                    else:
                        return f"Driver {driver_name} is already added in {race_name} race."
                else:
                    raise Exception(
                        f"Driver {driver_name} could not participate in the race!"
                    )
            else:
                raise Exception(f"Driver {driver_name} could not be found!")
        else:
            raise Exception(f"Race {race_name} could not be found!")

    def start_race(self, race_name: str):
        race = self.race_exists(race_name)
        if race is not False:
            if len(race.drivers) >= 3:
                fastest = {}
                for driver in race.drivers:
                    fastest[driver.name] = driver.car.speed_limit
                fastest = sorted(fastest.items(), key=lambda x: x[0])
                print(fastest)
            else:
                raise Exception(
                    f"Race {race_name} cannot start with less than 3 participants!"
                )
        else:
            raise Exception(f"Race {race_name} could not be found!")
