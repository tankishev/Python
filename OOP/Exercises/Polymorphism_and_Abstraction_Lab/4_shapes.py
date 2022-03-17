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


# Zero Tests
if __name__ == "__main__":
    circle = Circle(5)
    print(circle.calculate_area())
    print(circle.calculate_perimeter())

    # 78.53981633974483
    # 31.41592653589793

    rectangle = Rectangle(10, 20)
    print(rectangle.calculate_area())
    print(rectangle.calculate_perimeter())

    # 200
    # 60
