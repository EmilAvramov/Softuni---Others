import copy


class Person:
    def __init__(self, position):
        self.position = position
        self.is_free = True

    def walk_west(self, distance: int):
        if self.is_free:
            self.position[0] -= distance

    def walk_east(self, distance: int):
        if self.is_free:
            self.position[0] += distance

    def walk_north(self, distance: int):
        if self.is_free:
            self.position[1] += distance

    def walk_south(self, distance: int):
        if self.is_free:
            self.position[1] -= distance


class FreePerson(Person):
    def __init__(self, position):
        super().__init__(position)


class Prisoner(Person):
    PRISON_LOCATION = [3, 3]

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False


# prisoner = Prisoner()

# print("The prisoner trying to walk to north by 10 and east by -3.")

# try:
#     prisoner.walk_north(10)
#     prisoner.walk_east(-3)
# except:
#     pass

# print(f"The location of the prison: {prisoner.PRISON_LOCATION}")
# print(f"The current position of the prisoner: {prisoner.position}")


prisoner = Prisoner()

print("The prisoner trying to walk to north by 10 and east by -3.")

try:
    prisoner.walk_north(10)
    prisoner.walk_east(-3)
except:
    pass

print(f"The location of the prison: {prisoner.PRISON_LOCATION}")

print(f"The current position of the prisoner: {prisoner.position}")
