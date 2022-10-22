from collections import deque


caffeine = deque([int(i) for i in input().split(", ")])
drinks = deque([int(i) for i in input().split(", ")])

initial = 0
MAX = 300

while True:
    caff = caffeine.pop()
    drink = drinks.popleft()
    product = caff * drink
    if initial + product <= 300:
        initial += product
    else:
        drinks.append(drink)
        if initial >= 30:
            initial -= 30
        else:
            initial = 0
    if len(caffeine) == 0 or len(drinks) == 0:
        break

if len(drinks) > 0:
    print(f"Drinks left: {', '.join(str(x) for x in drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial} mg caffeine.")
