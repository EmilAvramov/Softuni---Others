from math import sqrt


class Point:
    def __init__(self, _x: list, _y: list):
        """
        Pass coordinates of 2 points (both values in list as int)
        param x: first point coordinates
        param y: second point coordinates
        """
        self.x = _x
        self.y = _y

    def calc_distance(self):
        return sqrt((int(self.x[0]) - int(self.y[0])) ** 2
                    + (int(self.x[1]) - int(self.y[1])) ** 2)


class Box:
    box_data = []

    def __init__(self, _tl: list, _tr: list, _bl: list, _br: list):
        """
        Assign coordinates:
        param _tl: top left point
        param _tr: top right point
        param _bl: bottom left point
        param _br: bottom right point

        Afterwards:
        Initialize box width, height, perimeter and area
        """
        self.tl = _tl
        self.tr = _tr
        self.bl = _bl
        self.br = _br
        self.width = None
        self.height = None
        self.perimeter = None
        self.area = None

    def width_height(self):
        self.width = int(Point(self.tl, self.tr).calc_distance())
        self.height = int(Point(self.tl, self.bl).calc_distance())

    def perimeter_area(self):
        self.perimeter = int(self.width * 2 + self.height * 2)
        self.area = int(self.width * self.height)


data = input()
while data != "end":
    top_l = data.split(" | ")[0].split(":")
    top_r = data.split(" | ")[1].split(":")
    bottom_l = data.split(" | ")[2].split(":")
    bottom_r = data.split(" | ")[3].split(":")
    Box.box_data.append(Box(top_l, top_r, bottom_l, bottom_r))
    data = input()

for box in Box.box_data:
    box.width_height()
    box.perimeter_area()
    print(f"Box: {box.width}, {box.height}")
    print(f"Perimeter: {box.perimeter}")
    print(f"Area: {box.area}")

