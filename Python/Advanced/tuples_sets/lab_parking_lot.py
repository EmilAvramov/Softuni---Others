entries = int(input())
parking_lot = set()

for i in range(entries):
    data = input().split(", ")
    direction = data[0]
    car = data[1]
    if direction == "IN":
        parking_lot.add(car)
    else:
        parking_lot.discard(car)

if len(parking_lot) == 0:
    print(f"Parking Lot is Empty")
else:
    for car in parking_lot:
        print(f"{car}", end="\n")
