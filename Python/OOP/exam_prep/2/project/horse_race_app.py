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
                self.__horses.append(new_horse)
                return f"Appaloosa horse {horse_name} is added."
            except Exception:
                pass
        elif horse_type == "Thoroughbred":
            new_horse = Thoroughbred(horse_name, horse_speed)
            try:
                self.__horses.append(new_horse)
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
        pass

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        race = self.return_race(race_type)
        jockey = self.return_jockey(jockey_name)
        if self.check_race(race_type):
            if self.check_jockey_exists(jockey_name):
                if self.check_jockey_horse(jockey_name):
                    if self.check_jockey_in_race(jockey_name, race) is False:
                        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        if self.check_race(race_type):
            selected = self.return_race(race_type)
            self.check_participants(selected)
            self.choose_winner(selected)

    def return_race(self, race_type: str):
        for race in self.horse_races:
            if race_type == race.race_type:
                return race

    def return_jockey(self, jockey_name: str):
        for jockey in self.jockeys:
            if jockey.name == jockey_name:
                return jockey

    def return_horse(self, horse_name: str):
        for horse in self.horses:
            if horse.name == horse_name:
                return horse

    def check_horse(self, horse_name: str):
        horse = self.return_horse(horse_name)
        if horse.is_taken:
            return True
        return False

    def check_breed(self, breed: str):
        if breed == "Thoroughbred" or breed == "Appaloosa":
            return True
        raise Exception(f"Horse breed {breed} could not be found!")

    def check_jockey_exists(self, jockey_name: str):
        for jockey in self.jockeys:
            if jockey_name == jockey.name:
                return True
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def check_jockey_horse(self, jockey_name: str):
        jockey = self.return_jockey(jockey_name)
        if jockey.horse != None:
            return True
        raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

    def check_jockey_in_race(self, jockey_name: str, race: HorseRace):
        for jockey in race.jockeys:
            if jockey_name == jockey.name:
                return "Jockey {jockey_name} has been already added to the {race_type} race."
        return False

    def check_race(self, race_type: str):
        for race in self.horse_races:
            if race_type == race.race_type:
                return True
        raise Exception(f"Race {race_type} could not be found!")

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
