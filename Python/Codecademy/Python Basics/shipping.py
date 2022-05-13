import sys

weight = float(input())

ground_price = 0
flat_price = 125
drone_price = 0
cheapest = -sys.maxsize
method = ""

if weight <= 2:
    ground_price = 1.5 * weight + 20
    if cheapest < ground_price:
        cheapest = ground_price
        method = "Ground"
    drone_price = 4.5 * weight
    if cheapest < drone_price:
        cheapest = drone_price
        method = "Drone"
    flat_price = 125
    if cheapest < flat_price:
        cheapest = flat_price
        method = "Ground Premium"
elif 2 < weight <= 6:
    ground_price = 3 * weight + 20
    if cheapest < ground_price:
        cheapest = ground_price
        method = "Ground"
    drone_price = 9 * weight
    if cheapest < drone_price:
        cheapest = drone_price
        method = "Drone"
    flat_price = 125
    if cheapest < flat_price:
        cheapest = flat_price
        method = "Ground Premium"
elif 6 < weight <= 10:
    ground_price = 4 * weight + 20
    if cheapest < ground_price:
        cheapest = ground_price
        method = "Ground"
    drone_price = 9 * weight
    if cheapest < drone_price:
        cheapest = drone_price
        method = "Drone"
    flat_price = 125
    if cheapest < flat_price:
        cheapest = flat_price
        method = "Ground Premium"
else:
    ground_price = 4.75 * weight + 20
    if cheapest < ground_price:
        cheapest = ground_price
        method = "Ground"
    drone_price = 14.25 * weight
    if cheapest < drone_price:
        cheapest = drone_price
        method = "Drone"
    flat_price = 125
    if cheapest < flat_price:
        cheapest = flat_price
        method = "Ground Premium"

print(f'For the weight of {weight}, the cheapest transportation method is {method}, costing {cheapest}')