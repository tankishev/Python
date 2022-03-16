from abc import ABC
from math import pi

class Shape(ABC):

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius) -> None:
        self.radius = radius

    def calculate_area(self):
        return self.radius ** 2 * pi

    def calculate_perimeter(self):
        return self.radius * 2 * pi

class Rectangle(Shape):

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_area(self):
        return self.height * self.width

    def calculate_perimeter(self):
        return 2 * self.height + 2 * self.width

circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())
