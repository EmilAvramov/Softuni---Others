from collections import deque

stack = deque([int(i) for i in input().split(" ")])
capacity = int(input())
volume = 0
num_racks = 1

while True:
    if stack:
        if volume + stack[-1] <= capacity:
            volume += stack.pop()
        else:
            volume = stack.pop()
            num_racks += 1
    else:
        break

print(num_racks)
