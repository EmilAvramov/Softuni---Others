from collections import deque

green_light = int(input())
free_window = int(input())
time_left = 0
passed = 0
end = False

command = input()
queue = deque()
sub_queue = deque()

while command != "END":
    queue.append(command)
    command = input()

while queue:
    while queue[0] != "green":
        sub_queue.append(queue.popleft())
    queue.popleft()
    time_left = green_light
    while sub_queue:
        passed += 1
        car = sub_queue.popleft()
        if len(car) <= time_left:
            time_left -= len(car)
        else:
            if time_left + free_window >= len(car):
                break
            else:
                index = (time_left + free_window) - len(car)
                end = True
                print("A crash happened!")
                print(f"{car} was hit at {car[index]}.")
                break
    if end:
        break

if end is False:
    print(f"Everyone is safe.\n{passed} total cars passed the crossroads.")
