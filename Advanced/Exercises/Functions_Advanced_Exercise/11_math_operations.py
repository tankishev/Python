# Write a function named math_operations that receives a different number of integers as arguments and 4 keyword arguments.
# The keys will be single letters: "a", "s", "d", "m", and the values will be numbers.
# You need to take each integer argument from the sequence and do mathematical operations as follows:
# •	The first element should be added to the value of the key "a"
# •	The second element should be subtracted from the value of the key "s"
# •	The third element should be divisor to the value of the key "d"
# •	The fourth element should be multiplied by the value of the key "m"
# •	Each result should replace the value of the corresponding key
# •	You must repeat the same steps consecutively until you run out of numbers
# Beware: You cannot divide by 0. If the operation could throw an error, you should delete the element from the sequence and continue to the next operation.
# For more clarifications, see the examples below.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input. Just parameters passed to your function.
# •	All of the given numbers will be valid integers in the range [-100, 100]
# Output
# •	The function should return the final dictionary


from collections import deque


def math_operations(*args, **kwargs):
    calc = {
        'a': lambda num: kwargs['a'] + num,
        's': lambda num: kwargs['s'] - num,
        'd': lambda num: kwargs['d'] / num if num != 0 else kwargs['d'],
        'm': lambda num: kwargs['m'] * num
    }

    operations = deque(('a', 's', 'd', 'm'))
    for arg in args:
        func = operations[0]
        kwargs[func] = calc[func](arg)
        operations.rotate(-1)

    return kwargs
