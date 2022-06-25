people = int(input())
wagons = [int(i) for i in input().split(" ")]
no_people = False


for i in range(len(wagons)):
    if wagons[i] < 4:
        if people > 4 - wagons[i]:
            people -= 4 - wagons[i]
            wagons[i] = 4
        else:
            wagons[i] += people
            people = 0
            no_people = True
            break


if no_people and (sum(wagons) / 4) != len(wagons):
    print("The lift has empty spots!")
    print(*wagons, sep=" ")
elif people > 0 and (sum(wagons) / 4) == len(wagons):
    print(f"There isn't enough space! {people} people in a queue!")
    print(*wagons, sep=" ")
else:
    print(*wagons, sep=" ")
