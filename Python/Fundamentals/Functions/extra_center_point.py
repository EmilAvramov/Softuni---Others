from math import floor

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def num_coordinates(_x1, _x2, _x3, _x4):
    if abs(_x1) + abs(_x2) <= abs(_x3) + abs(_x4):
        return f'({floor(_x1)}, {floor(_x2)})'
    else:
        return f'({floor(_x3)}, {floor(_x4)})'


print(num_coordinates(x1, y1, x2, y2))
