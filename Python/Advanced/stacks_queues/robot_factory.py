from collections import deque

# Setup data
queue = deque()
robots = [i.split("-") for i in input().split(";")]
time = [int(i) for i in input().split(":")]
sec = time[0] * 3600 + time[1] * 60 + time[2]

# Create queue
product = input()
while product != "End":
    queue.append(product)
    product = input()

# Prepare robots
for robot in robots:
    robot[1] = int(robot[1])
    robot.append(True)
    robot.append(robot[1])

# Process orders
while len(queue) > 0:
    sec += 1
    c_product = queue[0]
    for robot in robots:
        if robot[3] == 0:
            robot[2] = True
            robot.pop()
            robot.append(robot[1])
        if robot[2]:
            robot[2] = False
            current_time = "{:02}:{:02}:{:02}".format(
                sec // 3600, sec % 3600 // 60, sec % 60
            )
            print(f"{robot[0]} - {queue.popleft()} [{current_time}]")
            break
    for robot in robots:
        if robot[2] is False and robot[3] > 0:
            robot[3] -= 1
    if len(queue) > 0:
        if c_product == queue[0]:
            queue.append(queue.popleft())
