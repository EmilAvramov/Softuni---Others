from datetime import datetime, timedelta
from collections import deque

# Setup data
queue = deque()
robots = [i.split("-") for i in input().split(";")]
time = datetime.strptime(input(), "%H:%M:%S")

# Create queue
product = input()
while product != "End":
    queue.append(product)
    product = input()

# Prepare robots
for robot in robots:
    robot[1] = int(robot[1])
    robot.append(0)

# Process orders
while len(queue) > 0:
    is_free = True
    time += timedelta(seconds=1)
    product = queue.popleft()
    for robot in robots:
        if robot[2] == 0:
            robot.pop()
            robot.append(robot[1])
            print(f"{robot[0]} - {product} [{time.strftime('%H:%M:%S')}]")
            is_free = False
            break
    for robot in robots:
        if robot[2] > 0:
            robot[2] -= 1
    if is_free:
        queue.append(product)
