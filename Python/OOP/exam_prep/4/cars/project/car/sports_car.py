from project.car.car import Car


class SportsCar(Car):
    min_speed_limit: int = 400
    max_speed_limit: int = 600

    def __init__(self, model: str, speed_limit: int) -> None:
        super().__init__(model, speed_limit)
