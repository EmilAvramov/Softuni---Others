from collections import deque

pumps = int(input())
road_queue = deque()
start = False
total_fuel = 0
stops = 0
index = 0
start_point = 0

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
            start_point = 0
    else:
        if fuel >= distance:
            start = True
            total_fuel += fuel - distance
            stops += 1
            start_point = index
    road_queue.append(road_queue.popleft())
    index += 1
    if index == len(road_queue):
        index = 0


print(start_point)
