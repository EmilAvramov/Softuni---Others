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
        """
        self.tl = _tl
        self.tr = _tr
        self.bl = _bl
        self.br = _br

    def calculate_width(self):
        return int(Point(self.tl, self.tr).calc_distance())

    def calculate_height(self):
        return int(Point(self.tl, self.bl).calc_distance())

    @staticmethod
    def calculate_perimeter(_width, _height):
        return int(_width*2 + _height*2)

    @staticmethod
    def calculate_area(_width, _height):
        return int(_width * _height)


data = input()

while data != "end":
    top_l = data.split(" | ")[0].split(":")
    top_r = data.split(" | ")[1].split(":")
    bottom_l = data.split(" | ")[2].split(":")
    bottom_r = data.split(" | ")[3].split(":")

    new_box = Box(top_l, top_r, bottom_l, bottom_r)

    width = new_box.calculate_width()
    height = new_box.calculate_height()
    perimeter = Box.calculate_perimeter(width, height)
    area = Box.calculate_area(width, height)

    Box.box_data.append([width, height, perimeter, area])
    data = input()

for box in Box.box_data:
    print(f"Box: {box[0]}, {box[1]}")
    print(f"Perimeter: {box[2]}")
    print(f"Area: {box[3]}")

