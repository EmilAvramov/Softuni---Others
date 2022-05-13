class School:
    def __init__(self, _name: str, _level: str, _numberOfStudents: int):
        self.name = _name
        self.level = _level
        self.number_of_students = _numberOfStudents

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_students(self):
        return self.number_of_students

    def set_students(self, _new_value):
        self.number_of_students = _new_value

    def __repr__(self):
        return f"A {self.level} school named {self.name} with {self.number_of_students} students"


class PrimarySchool(School):
    def __init__(self, _pickup_policy: str):
        super().__init__("a new name", "primary", 50)
        self.pickup_policy = _pickup_policy

    def __repr__(self):
        return super().__repr__() + f" and {self.pickup_policy} pickup policy"


class HighSchool(School):
    def __init__(self, _sports_teams: list):
        super().__init__("an even newer name", "high school", 100)
        self.sports_teams = _sports_teams

    def get_teams(self):
        return self.sports_teams

    def __repr__(self):
        return super().__repr__() + f" with {self.sports_teams} teams"


new_school = School("a name", "primary", 10)
new_school.set_students(20)
print(new_school)

new_primary = PrimarySchool("After 3 pm")
print(new_primary)

new_high = HighSchool(["team A", "team B", "team C"])
print(new_high.get_teams())
print(new_high)
