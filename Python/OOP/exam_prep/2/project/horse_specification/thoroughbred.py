from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    def __init__(self, name: str, speed: int) -> None:
        super().__init__(name, speed)
        self.max_speed: int = 140
        self.increase: int = 3

    def train(self):
        return super().train()
