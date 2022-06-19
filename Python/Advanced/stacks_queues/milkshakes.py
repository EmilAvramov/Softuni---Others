from collections import deque

chocolates_stack = deque([int(i) for i in input().split(", ")])
cups_queue = deque([int(i) for i in input().split(", ")])
num_shakes = 0
break_flag = False

while num_shakes < 5:
    if break_flag:
        break
    try:
        while chocolates_stack[-1] <= 0:
            chocolates_stack.pop()
    except IndexError:
        break_flag = True
    try:
        while cups_queue[0] <= 0:
            cups_queue.popleft()
    except IndexError:
        break_flag = True
    if break_flag is False:
        if chocolates_stack[-1] == cups_queue[0]:
            num_shakes += 1
            chocolates_stack.pop()
            cups_queue.popleft()
        else:
            cups_queue.append(cups_queue.popleft())
            chocolates_stack[-1] -= 5

if num_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates_stack:
    print(f"Chocolate: {', '.join([str(i) for i in chocolates_stack])}")
else:
    print("Chocolate: empty")
if cups_queue:
    print(f"Milk: {', '.join([str(i) for i in cups_queue])}")
else:
    print("Milk: empty")
