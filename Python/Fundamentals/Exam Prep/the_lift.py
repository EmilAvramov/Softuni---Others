people = int(input())
wagons = [int(i) for i in input().split(" ")]
no_space = False


for i in range(len(wagons)):
    if wagons[i] < 4:
        if people > 4 - wagons[i]:
            people -= 4 - wagons[i]
            wagons[i] = 4
        else:
            wagons[i] += people
            people = 0
            no_space = True
            break

if people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*wagons, sep=" ")
elif no_space:
    print("The lift has empty spots!")
    print(*wagons, sep=" ")
else:
    print(*wagons, sep=" ")
