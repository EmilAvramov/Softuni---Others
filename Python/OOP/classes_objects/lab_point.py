class Point:
    def __init__(self, _x: int, _y: int) -> None:
        self.x = _x
        self.y = _y

    def set_x(self, _new_x: int):
        self.x = _new_x

    def set_y(self, _new_y: int):
        self.y = _new_y

    def __str__(self) -> str:
        return f"The point has coordinates ({self.x},{self.y})"


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
