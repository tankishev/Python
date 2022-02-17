# Write a function called multiply that can receive any quantity of numbers (integers) as different parameters and returns the result of the multiplication of all of them. Submit only your function in the Judge system.


def multiply(x, y, *args):
    result = int(x) * int(y)
    for arg in args:
        result *= int(arg)
    return result
