class Animals:
    dogs = {}
    cats = {}
    snakes = {}

    @staticmethod
    def produce_sound(_name: str):
        if _name in Animals.dogs.keys():
            return "I'm a Distinguishedog, and I will now " \
                   "produce a distinguished sound! Bau Bau."
        elif _name in Animals.cats.keys():
            return "I'm an Aristocat, and I will now " \
                   "produce an aristocratic sound! Myau Myau."
        else:
            return "I'm a Sophistisnake, and I will now " \
                   "produce a sophisticated sound! Honey, I'm home."

    @staticmethod
    def add_animal(_type: str, _name: str, _age: int, _param: int):
        if _type == "Dog":
            Animals.dogs[_name] = [_age, _param]
        elif _type == "Cat":
            Animals.cats[_name] = [_age, _param]
        else:
            Animals.snakes[_name] = [_age, _param]


data = input()

while data != "I'm your Huckleberry":
    if "talk" in data:
        name = data.split()[1]
        print(Animals.produce_sound(name))
    else:
        a_type = data.split()[0]
        name = data.split()[1]
        age = int(data.split()[2])
        param = int(data.split()[3])
        Animals.add_animal(a_type, name, age, param)
    data = input()

for key, value in Animals.dogs.items():
    print(f"Dog: {key}, Age: {value[0]}, Number Of Legs: {value[1]}")
for key, value in Animals.cats.items():
    print(f"Cat: {key}, Age: {value[0]}, IQ: {value[1]}")
for key, value in Animals.snakes.items():
    print(f"Snake: {key}, Age: {value[0]}, Cruelty: {value[1]}")
