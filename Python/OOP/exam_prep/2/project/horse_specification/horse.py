class Horse:
    def __init__(self, name: str, speed: int) -> None:
        self._name: str = name
        self._speed: int = speed
        self.is_taken: bool = False
        self.max_speed: None | int = None
        self.increase: None | int = None

    def get_name(self):
        return self._name

    def set_name(self, value: str):
        if len(value) < 4:
            raise ValueError("Horse name {value} is less than 4 symbols!")
        self._name = value

    def get_speed(self):
        return self._speed

    def set_speed(self, value: int):
        if value > self.max_speed:
            raise ValueError("Horse speed is too high!")
        self._speed = value

    def train(self):
        if self.increase + self._speed >= self.max_speed:
            self._speed = self.max_speed
        else:
            self._speed += self.increase
