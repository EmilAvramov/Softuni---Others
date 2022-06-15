from collections import deque

names = deque(input().split(" "))
number = int(input())
counter = 0

while len(names) > 1:
    counter += 1
    if counter == number:
        current = names.popleft()
        counter = 0
        print(f"Removed {current}")
    else:
        current = names.popleft()
        names.append(current)

print(f"Last is {names[0]}")
