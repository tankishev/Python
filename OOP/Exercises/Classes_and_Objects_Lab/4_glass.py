# Create a class called Glass. Upon initialization it will not receive any parameters,
# you must create however an instance attribute called content which should be equal to 0.
# You should also create a class attribute called capacity which should be 250 ml.
# Create 3 instance methods:
# -	fill(ml) - fill the glass with the given milliliters if there is enough space in it
# and return "Glass filled with {ml} ml", otherwise return "Cannot add {ml} ml"
# -	empty() - empty the glass and return "Glass is now empty"
# -	info() - returns info about the glass in the format "{space_left} ml left"


class Glass:

    capacity = 250

    def __init__(self) -> None:
        self.content = 0

    def fill(self, ml) -> str:
        if ml <= Glass.capacity - self.content:
            self.content += ml
            return f"Glass filled with {ml} ml"

        return f"Cannot add {ml} ml"

    def empty(self) -> str:
        self.content = 0
        return "Glass is now empty"

    def info(self) -> str:
        return f'{Glass.capacity - self.content} ml left'


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
