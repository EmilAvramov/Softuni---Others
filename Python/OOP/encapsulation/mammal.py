class Mammal:
    __kingdom = "animals"

    def __init__(self, _name: str, _type: str, _sound: str) -> None:
        self.name = _name
        self.type = _type
        self.sound = _sound

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return Mammal.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"
