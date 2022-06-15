from collections import deque

data = input()
customers = deque()

while data != "End":
    if data == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(data)
    data = input()

print(f"{len(customers)} people remaining.")
