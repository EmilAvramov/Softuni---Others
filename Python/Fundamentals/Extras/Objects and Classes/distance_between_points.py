from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_distance(self):
        return sqrt((self.x[0] - self.y[0]) ** 2
                    + (self.x[1] - self.y[1]) ** 2)


distance = Point([int(i) for i in input().split()],
                 [int(i) for i in input().split()])
print(f"{distance.calc_distance():.3f}")

