class Horse:
    def __init__(self, name: str, speed: int) -> None:
        self._name = name
        self._speed = speed
        self._is_taken = False
        self.max_speed = 0

    def get_name(self):
        return self._name

    def set_name(self, value: str):
        if len(value) < 4:
            raise ValueError("Horse name {value} is less than 4 symbols!")

    def get_speed(self):
        return self._speed

    def set_speed(self, value: int):
        if value > self.max_speed:
            raise ValueError("Horse speed is too high!")
        self._speed = value

    def train(self):
        pass
