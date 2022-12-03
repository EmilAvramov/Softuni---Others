class Player:
    names = []

    def __init__(self, name: str, age: int, stamina: int = 100) -> None:
        self.__name = name
        self.__age = age
        self.__stamina = stamina

    @property
    def need_sustenance(self):
        return self.__stamina < 100

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name not valid!")
        if value in self.names:
            raise Exception(f"Name {value} is already used!")
        self.names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 12:
            raise ValueError("The player cannot be under 12 years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    def __str__(self) -> str:
        return f"Player: {self.__name}, {self.__age}, {self.__stamina}, {self.need_sustenance}"

    def increase_stamina(self, value: int):
        if self.stamina + value >= 100:
            self.stamina = 100
        else:
            self.stamina += value
