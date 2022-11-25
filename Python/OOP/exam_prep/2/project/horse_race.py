class HorseRace:
    def __init__(self, race_type: str) -> None:
        self.__race_type: str = race_type
        self.jockeys: list = []

    @property
    def race_type(self):
        return self.__race_type

    @race_type.setter
    def race_type(self, value: str):
        valid_races = ["Winter", "Spring", "Autumn", "Summer"]
        if value not in valid_races:
            raise ValueError("Race type does not exist!")
        self.__race_type = value
