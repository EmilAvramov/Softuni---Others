class HorseRace:
    def __init__(self, race_type: str) -> None:
        self._race_type: str = race_type
        self.jockeys: list = []

    def get_race_type(self):
        return self._race_type

    def set_race_type(self, value: str):
        valid_races = ["Winter", "Spring", "Autumn", "Summer"]
        if value not in valid_races:
            raise ValueError("Race type does not exist!")
        self._race_type = value
