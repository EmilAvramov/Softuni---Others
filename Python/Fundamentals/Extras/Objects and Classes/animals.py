class Dog:
    def __init__(self, _name: str, _age: int, legs: int):
        self._name = _name
        self._age = _age
        self.legs = legs

    @staticmethod
    def produce_sound():
        return "I'm a Distinguishedog, and I will now " \
               "produce a distinguished sound! Bau Bau."

    def unpack_self(self):
        return ["Dog", [self._name, [self._age, self.legs]]]


class Cat:
    def __init__(self, _name: str, _age: int, iq: int):
        self._name = _name
        self._age = _age
        self.iq = iq

    @staticmethod
    def produce_sound():
        return "I'm an Aristocat, and I will now " \
               "produce an aristocratic sound! Myau Myau."

    def unpack_self(self):
        return ["Cat", [self._name, [self._age, self.iq]]]


class Snake:
    def __init__(self, _name: str, _age: int, cruelty: int):
        self._name = _name
        self._age = _age
        self.cruelty = cruelty

    @staticmethod
    def produce_sound():
        return "I'm a Sophistisnake, and I will now " \
               "produce a sophisticated sound! Honey, I'm home."

    def unpack_self(self):
        return ["Snake", [self._name, [self._age, self.cruelty]]]


data = input()
animal_dict = {}

while data != "I'm your Huckleberry":
    if "talk" in data:
        name = data.split()[1]
        for key, value in animal_dict.items():
            if name in value:
                if key == "Dog":
                    print(Dog.produce_sound())
                elif key == "Cat":
                    print(Cat.produce_sound())
                else:
                    print(Snake.produce_sound())
    else:
        call = data.split()[0]
        name = data.split()[1]
        age = int(data.split()[2])
        parameter = int(data.split()[3])
        if call not in animal_dict.keys():
            if call == "Dog":
                anml = Dog(name, age, parameter).unpack_self()
            elif call == "Cat":
                anml = Cat(name, age, parameter).unpack_self()
            else:
                anml = Snake(name, age, parameter).unpack_self()
            animal_dict[anml[0]] = {anml[1][0]: anml[1][1]}
        else:
            if call == "Dog":
                anml = Dog(name, age, parameter).unpack_self()
            elif call == "Cat":
                anml = Cat(name, age, parameter).unpack_self()
            else:
                anml = Snake(name, age, parameter).unpack_self()
            animal_dict[anml[0]].update({anml[1][0]: anml[1][1]})
    data = input()

for key, value in animal_dict.items():
    if key == "Dog":
        for sub_key, sub_value in value.items():
            print(f"Dog: {sub_key}, Age: {sub_value[0]}, "
                  f"Number Of Legs: {sub_value[1]}")

for key, value in sorted(animal_dict.items(), key=lambda x: x[0]):
    if key == "Cat":
        for sub_key, sub_value in value.items():
            print(f"Cat: {sub_key}, Age: {sub_value[0]}, "
                  f"IQ: {sub_value[1]}")
    elif key == "Snake":
        for sub_key, sub_value in value.items():
            print(f"Snake: {sub_key}, Age: {sub_value[0]}, "
                  f"Cruelty: {sub_value[1]}")