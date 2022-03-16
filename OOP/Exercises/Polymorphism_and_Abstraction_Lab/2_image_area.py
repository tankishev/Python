# Create a class called ImageArea which will store the width and the height of an image.
# Create a method called get_area() which will return the area of the image.
# We have also to implement all the magic methods for comparison of two image areas
# (>, >=, <, <=, ==, !=), which will compare their areas.


class ImageArea:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_area(self) -> int:
        return self.width * self.height

    def __eq__(self, other) -> bool:
        return self.get_area() == other.get_area()

    def __lt__(self, other) -> bool:
        return self.get_area() < other.get_area()

    def __le__(self, other) -> bool:
        return self.get_area() <= other.get_area()

    def __gt__(self, other) -> bool:
        return self.get_area() > other.get_area()

    def __ge__(self, other) -> bool:
        return self.get_area() >= other.get_area()

    def __ne__(self, other) -> bool:
        return self.get_area() != other.get_area()
