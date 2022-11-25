from project.horse_specification.horse import Horse

class Appaloosa(Horse):
    def __init__(self, name: str, speed: int) -> None:
        super().__init__(name, speed)
        self.max_speed = 120
        self.increase = 2

    def train(self):
        return super().train()