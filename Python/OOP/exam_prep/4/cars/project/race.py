class Race:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.drivers: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if value == "":
            raise ValueError("Name cannot be an empty string!")
        self.__name = value
