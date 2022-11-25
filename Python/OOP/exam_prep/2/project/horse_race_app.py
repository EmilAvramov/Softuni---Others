from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self) -> None:
        self._horses: list = []
        self._jockeys: list = []
        self._horse_races: list = []

    def get_horses(self):
        return self._horses

    def set_horses(self, value: Horse):
        for horse in self._horses:
            if horse.name == value.name:
                raise Exception(f"Horse {value.name} has been already added!")
        self._horses.append(value)
        print(f"{value.__class__.__name__} horse {value.name} is added.")

    def get_jockeys(self):
        return self._jockeys

    def set_jockeys(self, value: Jockey):
        for jockey in self._jockeys:
            if jockey.name == value.name:
                raise Exception(f"Jockey {value.name} has been already added!")
        self._jockeys.append(value)
        print(f"Jockey {value.name} is added.")

    def get_horse_races(self):
        return self._horse_races

    def set_horse_races(self, value: HorseRace):
        for race in self._horse_races:
            if race.race_type == value.race_type:
                raise Exception(
                    f"Race {value.race_type} has been already created!"
                )
        self._horse_races.append(value)
        print(f"Race {value.race_type} is created.")

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
            self._horses.append(new_horse)
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
            self._horses.append(new_horse)

    def add_jockey(self, jockey_name: str, age: int):
        new_jockey = Jockey(jockey_name, age)
        self._jockeys.append(new_jockey)

    def create_horse_race(self, race_type: str):
        new_race = HorseRace(race_type)
        self._horse_races.append(new_race)

    def add_horse_to_jocket(self, jockey_name: str, horse_type: str):
        jockey_found = False
        horse_found = False
        horse_available = False
        jockey_has_horse = False
        horse_set = False
        for jockey in self._jockeys:
            if jockey_name == jockey.name:
                jockey_found = True
                for horse in self._horses:
                    if (
                        horse.__class__.__name__ == horse_type
                        and horse.is_taken is False
                        and jockey.horse is None
                    ):
                        horse_set = True
                        jockey.horse = horse
                        horse.is_taken = True
                        return f"Jockey {jockey_name} will ride the horse {horse.name}."
                if horse_set is False:
                    for horse in self._horses:
                        if horse.__class__.__name__ == horse_type:
                            horse_found = True
                            for horse in self._horses:
                                if (
                                    horse.__class__.__name__ == horse_type
                                    and horse.is_taken is False
                                ):
                                    horse_available = True
                                    jockey_has_horse = True
                                    break
        if jockey_found is False:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if horse_found is False or horse_available is False:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if jockey_has_horse:
            raise Exception(f"Jockey {jockey_name} already has a horse.")

    def add_jockey_to_horse_race(self):
        pass

    def start_horse_race(self):
        pass
