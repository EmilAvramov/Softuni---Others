animals = str(input())

animal_list = animals.split(", ")
sheep_number = 0

for index, value in enumerate(animal_list):
    if animal_list[-1] == "wolf":
        print(f'Please go away and stop eating my sheep')
        break
    if value == "wolf" and index != len(animal_list):
        print(f'Oi! Sheep number {(abs(index + 1 - len(animal_list)))}! You are about to be eaten by a wolf!')
        break
