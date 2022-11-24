class Jockey:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
        self._horse = None

    def get_name(self):
        return self._horse

    def set_name(self, value: str):
        if len(value) == 0 or value == " ":
            raise ValueError("Name should contain at least one character!")
        self._name = value

    def get_age(self):
        return self._age

    def set_age(self, value: int):
        if value < 18:
            raise ValueError(
                "Jockeys must be at least 18 to participate in the race!"
            )
        self._age = value

    def get_horse(self):
        return self._horse

    def set_horse(self, value):
        self._horse = value
