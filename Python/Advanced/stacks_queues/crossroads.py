from collections import deque

green_light = int(input())
free_window = int(input())
passed = 0
crash = False

command = input()
queue = deque()

while command != "END":
    if command == "green":
        if queue:
            time_left = green_light
            while time_left > 0:
                if queue:
                    if len(queue[0]) <= time_left:
                        passed += 1
                        time_left -= len(queue[0])
                        queue.popleft()
                    else:
                        if time_left + free_window >= len(queue[0]):
                            queue.popleft()
                            passed += 1
                            break
                        else:
                            hit_car = queue.popleft()
                            index = (time_left + free_window) - len(hit_car)
                            crash = True
                            print("A crash happened!")
                            print(f"{hit_car} was hit at {hit_car[index]}.")
                            break
                else:
                    break
    else:
        queue.append(command)
    command = input()

if crash is False:
    print(f"Everyone is safe.\n{passed} total cars passed the crossroads.")
