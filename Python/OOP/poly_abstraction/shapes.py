from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, _radius) -> None:
        self.__radius = _radius

    def radius(self):
        return self.__radius

    def calculate_perimeter(self):
        return 2 * pi * self.radius()

    def calculate_area(self):
        return pi * (self.radius() ** 2)


class Rectangle(Shape):
    def __init__(self, _width, _height) -> None:
        self.__width = _width
        self.__height = _height

    def width(self):
        return self.__width

    def height(self):
        return self.__height

    def calculate_area(self):
        return self.width() * self.height()

    def calculate_perimeter(self):
        return self.width() * 2 + self.height() * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
