class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        Zoo.__animals += 1
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f'Mammals in {self.zoo_name}: {", ".join(self.mammals)}\n'
        elif species == "fish":
            result += f'Fishes in {self.zoo_name}: {", ".join(self.fishes)}\n'
        elif species == "bird":
            result += f'Birds in {self.zoo_name}: {", ".join(self.birds)}\n'
        result += f'Total animals: {Zoo.__animals}'
        return result


zoo_inst = Zoo(input())
num_animals = int(input())

for animal in range(num_animals):
    command = input().split()
    zoo_inst.add_animal(command[0], command[1])

print(zoo_inst.get_info(input()))
