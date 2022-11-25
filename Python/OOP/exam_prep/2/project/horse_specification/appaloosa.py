from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    def __init__(self, name: str, speed: int) -> None:
        super().__init__(name, speed)
        self.max_speed: int = 120
        self.increase: int = 2

    def train(self):
        return super().train()
