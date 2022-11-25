from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAX_HORSE_SPEED: None | int = 120

    def __init__(self, name: str, speed: int) -> None:
        super().__init__(name, speed)

    def train(self):
        if self.speed <= 118:
            self.speed += 2
        else:
            self.speed = self.MAX_HORSE_SPEED
