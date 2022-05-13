class Rectangle:

    def __init__(self, left, top, width, height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height

    def is_inside(self, left2, top2, width2, height2):
        is_inside = False
        if self.left >= left2:
            if self.top <= top2:
                if self.width + self.left <= left2 + width2:
                    if self.height + self.top <= left2 + height2:
                        is_inside = True
        if is_inside:
            return "Inside"
        else:
            return "Not inside"


r1 = [int(i) for i in input().split()]
r2 = [int(i) for i in input().split()]

print(Rectangle(r1[0], r1[1], r1[2], r1[3]).
      is_inside(r2[0], r2[1], r2[2], r2[3]))