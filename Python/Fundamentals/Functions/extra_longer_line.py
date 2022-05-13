import math

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


def num_coordinates(_x1, _y1, _x2, _y2):
    distance = math.sqrt(math.pow((_x2 - _x1), 2) + math.pow((_y2 - _y1), 2))
    return distance


distance_1 = num_coordinates(x1, y1, x2, y2)
distance_2 = num_coordinates(x3, y3, x4, y4)

if distance_1 >= distance_2:
    if abs(x1) + abs(y1) <= abs(x2) + abs(y2):
        print(f'({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})')
    else:
        print(f'({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})')
else:
    if abs(x3) + abs(y3) <= abs(x4) + abs(y4):
        print(f'({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})')
    else:
        print(f'({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})')
