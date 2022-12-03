from project.car.car import Car


class MuscleCar(Car):
    min_speed_limit: int = 250
    max_speed_limit: int = 400

    def __init__(self, model: str, speed_limit: int) -> None:
        super().__init__(model, speed_limit)
