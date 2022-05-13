import sys
from math import sqrt


class Point:
    closest = sys.maxsize
    closest_points = ()

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_distance(self):
        return sqrt((self.x[0] - self.y[0]) ** 2
                    + (self.x[1] - self.y[1]) ** 2)

    def closest_distance(self):
        if Point.calc_distance(self) < Point.closest:
            Point.closest = Point.calc_distance(self)
            Point.closest_points = self.x, self.y


coord_list = []
num_points = int(input())

for i in range(num_points):
    points = [int(i) for i in input().split()]
    coord_list.append(points)

for i in range(len(coord_list)):
    for j in range(len(coord_list)):
        if i != j:
            Point(coord_list[i], coord_list[j]).calc_distance()
            Point(coord_list[i], coord_list[j]).closest_distance()


print(f"{Point.closest:.3f}")
print(*[tuple(i) for i in Point.closest_points], sep='\n')