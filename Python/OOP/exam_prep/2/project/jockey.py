class Jockey:
    def __init__(self, name: str, age: int) -> None:
        self.__name: str = name
        self.__age: int = age
        self.__horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) == 0 or value.strip() == "":
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: int):
        if value < 18:
            raise ValueError(
                "Jockeys must be at least 18 to participate in the race!"
            )
        self.__age = value

    @property
    def horse(self):
        return self.__horse

    @horse.setter
    def horse(self, value):
        if self.__horse == None:
            self.__horse = value
