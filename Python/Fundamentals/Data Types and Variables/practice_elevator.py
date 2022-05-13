from math import ceil

num_people = int(input())
cap_people = int(input())

if num_people <= cap_people:
    print("1")
else:
    if num_people % cap_people == 0:
        print(f'{num_people/cap_people:.0f}')
    else:
        print(f'{ceil(num_people/cap_people):.0f}')
