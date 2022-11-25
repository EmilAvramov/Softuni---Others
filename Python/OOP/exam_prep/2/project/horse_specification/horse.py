from abc import ABC, abstractmethod


class Horse(ABC):
    MAX_HORSE_SPEED: None | int = None

    def __init__(self, name: str, speed: int) -> None:
        self.__name: str = name
        self.__speed: int = speed
        self.is_taken: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value: str):
        if len(value) < 4:
            raise ValueError("Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value: int):
        if value > self.MAX_HORSE_SPEED:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        ...
