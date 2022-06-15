from collections import deque

pumps = int(input())
road_queue = deque()
start = False
total_fuel = 0
stops = 0
start_index = 0

for i in range(pumps):
    tokens = [int(i) for i in input().split(" ")]
    road_queue.append(tokens)

while True:
    current = road_queue[0]
    fuel = current[0]
    distance = current[1]
    if start:
        if total_fuel + fuel >= distance:
            total_fuel += fuel - distance
            stops += 1
            if stops == len(road_queue):
                break
        elif total_fuel + fuel < distance:
            stops = 0
            total_fuel = 0
            start = False
            start_index += 1
    else:
        if fuel >= distance:
            start = True
            total_fuel += fuel - distance
            stops += 1
        elif fuel < distance:
            start_index += 1
    road_queue.append(road_queue.popleft())


print(start_index)
