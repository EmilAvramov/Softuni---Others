from collections import deque

lines = int(input())
stack = deque()

for i in range(lines):
    data = input()
    if "1" in data:
        stack.append(int(data.split(" ")[1]))
    elif "2" in data:
        if stack:
            stack.pop()
    elif "3" in data:
        if stack:
            print(stack[stack.index(max(stack))])
    else:
        if stack:
            print(stack[stack.index(min(stack))])

if stack:
    stack.reverse()
    print(*stack, sep=", ")
