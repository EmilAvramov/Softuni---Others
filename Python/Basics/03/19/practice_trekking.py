num_groups = int(input())

musala = 0
monblan = 0
kilimanjdaro = 0
k2 = 0
everest = 0
total_climbers = 0

for i in range(1, num_groups + 1):
    num_people = int(input())
    total_climbers += num_people
    if num_people <= 5:
        musala += num_people
    elif 6 <= num_people <= 12:
        monblan += num_people
    elif 13 <= num_people <= 25:
        kilimanjdaro += num_people
    elif 26 <= num_people <= 40:
        k2 += num_people
    else:
        everest += num_people

print(f'{(musala / total_climbers) * 100:.2f}%', end='\n')
print(f'{(monblan / total_climbers) * 100:.2f}%', end='\n')
print(f'{(kilimanjdaro / total_climbers) * 100:.2f}%', end='\n')
print(f'{(k2 / total_climbers) * 100:.2f}%', end='\n')
print(f'{(everest / total_climbers) * 100:.2f}%')
