# Create a class called Cup. Upon initialization it should receive size (number) and
# quantity (a number representing how much liquid is in it).
# The class should have two methods:
# •	fill(milliliters) which will increase the amount of liquid in the cup with the
# given milliliters (if there is space in the cup, otherwise ignore).
# •	status() which will return the amount of free space left in the cup.


class Cup:

    def __init__(self, size: int, quantity: int) -> None:
        self.size = size
        self.quantity = quantity

    def fill(self, ml: int) -> None:
        if ml <= self.status():
            self.quantity += ml

    def status(self) -> int:
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
