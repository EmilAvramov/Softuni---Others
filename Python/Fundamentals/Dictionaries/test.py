data_input = input()

talk_info = {}


class Dog:
    dogs_collection = []

    def __init__(self, name, age, legs):
        self.name = name
        self.age = int(age)
        self.legs = int(legs)

    @staticmethod
    def produce_sound():
        return f"I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau."


class Cat:
    cats_collection = []

    def __init__(self, name, age, intelligence):
        self.name = name
        self.age = int(age)
        self.intelligence = int(intelligence)

    @staticmethod
    def produce_sound():
        return f"I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau."


class Snake:
    snake_collection = []

    def __init__(self, name, age, cruelty):
        self.name = name
        self.age = int(age)
        self.cruelty = int(cruelty)

    @staticmethod
    def produce_sound():
        return f"I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home."


while data_input != "I'm your Huckleberry":
    name, *info = data_input.split()
    if "Dog" == name:
        Dog.dogs_collection.append(Dog(*info))
        talk_info[info[0]] = Dog.produce_sound()
    elif "Cat" == name:
        Cat.cats_collection.append(Cat(*info))
        talk_info[info[0]] = Cat.produce_sound()
    elif "Snake" == name:
        Snake.snake_collection.append(Snake(*info))
        talk_info[info[0]] = Snake.produce_sound()
    if name == "talk":
        print(talk_info[info[0]])
    data_input = input()

for show in Dog.dogs_collection:
    print(f"Dog: {show.name}, Age: {show.age}, Number Of Legs: {show.legs}")
for show in Cat.cats_collection:
    print(f"Cat: {show.name}, Age: {show.age}, IQ: {show.intelligence}")
for show in Snake.snake_collection:
    print(f"Snake: {show.name}, Age: {show.age}, Cruelty: {show.cruelty}")