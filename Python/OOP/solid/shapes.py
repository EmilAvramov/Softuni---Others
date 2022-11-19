class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)


class Triangle(Shape):
    def __init__(self, width, height):
        super().__init__(width, height)


class AreaCalculator:
    def __init__(self, shapes):

        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.width * shape.height

        return total


shapes = [Rectangle(2, 3), Rectangle(1, 6)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)

shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)
print("The total area is: ", calculator.total_area)
