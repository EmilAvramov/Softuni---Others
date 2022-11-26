from project.horse_specification.horse import Horse
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.horse_race import HorseRace


class HorseRaceApp:
    def __init__(self) -> None:
        self.__horses: list = []
        self.__jockeys: list = []
        self.__horse_races: list = []

    @property
    def horses(self):
        return self.__horses

    @horses.setter
    def horses(self, value: Horse):
        for horse in self.__horses:
            if horse.name == value.name:
                raise Exception(f"Horse {value.name} has been already added!")
        self.__horses.append(value)

    @property
    def jockeys(self):
        return self.__jockeys

    @jockeys.setter
    def jockeys(self, value: Jockey):
        for jockey in self.__jockeys:
            if jockey.name == value.name:
                raise Exception(f"Jockey {value.name} has been already added!")
        self.__jockeys.append(value)

    @property
    def horse_races(self):
        return self.__horse_races

    @horse_races.setter
    def horse_races(self, value: HorseRace):
        for race in self.__horse_races:
            if race.race_type == value.race_type:
                raise Exception(
                    f"Race {value.race_type} has been already created!"
                )
        self.__horse_races.append(value)

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type == "Appaloosa":
            new_horse = Appaloosa(horse_name, horse_speed)
            try:
                self.horses.append(new_horse)
                return f"Appaloosa horse {horse_name} is added."
            except Exception:
                pass
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
            try:
                self.horses.append(new_horse)
                return f"Thoroughbred horse {horse_name} is added."
            except Exception:
                pass

    def add_jockey(self, jockey_name: str, age: int):
        new_jockey = Jockey(jockey_name, age)
        try:
            self.__jockeys.append(new_jockey)
            return f"Jockey {jockey_name} is added."
        except Exception:
            pass

    def create_horse_race(self, race_type: str):
        new_race = HorseRace(race_type)
        try:
            self.horse_races.append(new_race)
            return f"Race {race_type} is created."
        except Exception:
            pass

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self.return_jockey(jockey_name)
        if self.check_jockey(jockey_name):
            if isinstance(self.jockey_needs_horse(jockey_name), bool):
                horse = self.return_horse(horse_type)
                if self.check_horse(horse_type):
                    jockey.horse = horse
                    horse.is_taken = True
                    index_jockey = self.jockeys.index(jockey)
                    index_horse = self.horses.index(horse)
                    self.horses[index_horse] = horse
                    self.jockeys[index_jockey] = jockey
                    return f"Jockey {jockey_name} will ride the horse {horse.name}."
            else:
                return self.jockey_needs_horse(jockey_name)

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.return_race(race_type)
        if self.check_race(race_type):
            if self.check_jockey(jockey_name):
                if self.jockey_has_horse(jockey_name):
                    if isinstance(
                        self.jockey_in_race(jockey_name, race), bool
                    ):
                        jockey = self.return_jockey(jockey_name)
                        race.jockeys.append(jockey)
                        race_index = self.horse_races.index(race)
                        self.horse_races[race_index] = race
                        return f"Jockey {jockey_name} added to the {race_type} race."
                    else:
                        return self.jockey_in_race(jockey_name, race)

    def start_horse_race(self, race_type: str):
        if self.check_race(race_type):
            selected = self.return_race(race_type)
            self.check_participants(selected)
            return self.choose_winner(selected)

    # Objects
    def return_race(self, race_type: str):
        for race in self.horse_races:
            if race_type == race.race_type:
                return race

    def return_jockey(self, jockey_name: str):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def return_horse(self, horse_type: str):
        for horse in self.horses:
            if horse.__class__.__name__ == horse_type:
                return horse

    # Existence
    def check_race(self, race_type: str):
        for race in self.horse_races:
            if race_type == race.race_type:
                return True
        raise Exception(f"Race {race_type} could not be found!")

    def check_jockey(self, jockey_name: str):
        for jockey in self.jockeys:
            if jockey_name == jockey.name:
                return True
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def check_horse(self, horse_type: str):
        for horse in reversed(self.horses):
            if horse.__class__.__name__ == horse_type:
                if horse.is_taken is False:
                    return True
                raise Exception(
                    f"Horse breed {horse_type} could not be found!"
                )
        raise Exception(f"Horse breed {horse_type} could not be found!")

    # Race Validation
    def check_participants(self, race: HorseRace):
        if len(race.jockeys) < 2:
            raise Exception(
                f"Horse race {race.race_type} needs at least two participants!"
            )

    def choose_winner(self, race: HorseRace):
        top_speed = 0
        jockey_name = ""
        horse_name = ""
        for jockey in race.jockeys:
            if jockey.horse.speed > top_speed:
                top_speed = jockey.horse.speed
                jockey_name = jockey.name
                horse_name = jockey.horse.name
        return f"The winner of the {race.race_type} race, with a speed of {top_speed}km/h is {jockey_name}! Winner's horse: {horse_name}."

    def jockey_in_race(self, jockey_name: str, race: HorseRace):
        for jockey in race.jockeys:
            if jockey_name == jockey.name:
                return f"Jockey {jockey_name} has been already added to the {race.race_type} race."
        return False

    # Jockey horse validation
    def jockey_has_horse(self, jockey_name: str):
        jockey = self.return_jockey(jockey_name)
        if jockey.horse != None:
            return True
        return Exception(f"Jockey {jockey_name} cannot race without a horse!")

    def jockey_needs_horse(self, jockey_name: str):
        jockey = self.return_jockey(jockey_name)
        if jockey.horse == None:
            return True
        return f"Jockey {jockey_name} already has a horse."
