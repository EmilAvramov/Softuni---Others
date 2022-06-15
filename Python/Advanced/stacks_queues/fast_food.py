from collections import deque

food_qty = int(input())
orders = deque([int(i) for i in input().split(" ")])

print(orders[orders.index(max(orders))])

while True:
    if orders:
        current = orders[0]
        if food_qty >= current:
            food_qty -= orders.popleft()
        else:
            break
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left: {' '.join([str(i) for i in orders])}")
