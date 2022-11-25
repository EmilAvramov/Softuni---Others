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
            self.__horse_races.append(new_race)
            return f"Race {race_type} is created."
        except Exception:
            pass

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        pass
        # jockey_found = False
        # horse_found = False
        # horse_available = False
        # jockey_has_horse = False
        # horse_set = False
        # for jockey in self._jockeys:
        #     if jockey_name == jockey.name:
        #         jockey_found = True
        #         for horse in self._horses:
        #             if (
        #                 horse.__class__.__name__ == horse_type
        #                 and horse.is_taken is False
        #                 and jockey.horse is None
        #             ):
        #                 horse_set = True
        #                 jockey.horse = horse
        #                 horse.is_taken = True
        #                 return f"Jockey {jockey_name} will ride the horse {horse.name}."
        #         if horse_set is False:
        #             for horse in self._horses:
        #                 if horse.__class__.__name__ == horse_type:
        #                     horse_found = True
        #                     for horse in self._horses:
        #                         if (
        #                             horse.__class__.__name__ == horse_type
        #                             and horse.is_taken is False
        #                         ):
        #                             horse_available = True
        #                             jockey_has_horse = True
        #                             break
        # if jockey_found is False:
        #     raise Exception(f"Jockey {jockey_name} could not be found!")
        # if horse_found is False or horse_available is False:
        #     raise Exception(f"Horse breed {horse_type} could not be found!")
        # if jockey_has_horse:
        #     raise Exception(f"Jockey {jockey_name} already has a horse.")

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        pass

    def start_horse_race(self, race_type: str):
        if self.check_race(race_type):
            selected = self.return_race(race_type)
            self.check_participants(selected)
            self.choose_winner(selected)

    def return_race(self, race_type: str):
        for race in self.horse_races:
            if race_type == race.race_type:
                return race

    def check_jockey_exists(self, jockey_name: str):
        if jockey_name in self.jockeys:
            return True
        raise Exception(f"Jockey {jockey_name} could not be found!")

    def check_jockey_horse(self, jockey_name: str):
        if self.jockeys[jockey_name].horse == None:
            raise Exception(
                f"Jockey {jockey_name} cannot race without a horse!"
            )
        return True

    def check_jockey_in_rade(self, jockey_name: str, race: HorseRace):
        for jockey in race.jockeys:
            if jockey_name == jockey.name:
                return True
        return False

    def check_race(self, race_type: str):
        if race_type in self.horse_races:
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
