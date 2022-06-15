from collections import deque

queue = deque()

water_qty = int(input())
name = input()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    tokens = command.split(" ")
    if len(tokens) > 1:
        water_qty += int(tokens[1])
    else:
        if water_qty >= int(tokens[0]) and queue:
            water_qty -= int(tokens[0])
            print(f"{queue.popleft()} got water")
        else:
            print(f"{queue.popleft()} must wait")
    command = input()

print(f"{water_qty} liters left")
