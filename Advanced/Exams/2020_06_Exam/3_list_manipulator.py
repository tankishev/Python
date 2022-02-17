# Write a function called list_manipulator which receives a list of numbers as first parameter and different amount of other parameters.
# The second parameter might be "add" or "remove". The third parameter might be "beginning" or "end". There might or might not be any other parameters (numbers):
# •	In case of "add" and "beginning", add the given numbers to the beginning of the given list of numbers and return the new list
# •	In case of "add" and "end", add the given numbers to the end of the given list of numbers and return the new list
# •	In case of "remove" and "beginning"
# o	If there is another parameter (number), remove that amount of numbers from the beginning of the list of numbers.
# o	If there are no other parameters, remove only the first element of the list.
# o	Finally, return the new list
# •	In case of "remove" and "end"
# o	If there is another parameter (number), remove that amount of numbers from the end of the list of numbers.
# o	Otherwise if there are no other parameters, remove only the last element of the list.
# o	Finally, return the new list
# For more clarifications, see the examples below.
# Input
# •	There will be no input
# •	Parameters will be passed to your function
# Output
# •	The function should return the new list of numbers


from collections import deque


def list_manipulator(nums: list, add_remove: str, beginning_end: str, *args) -> list:
    retval = deque(nums)

    if add_remove == 'add':
        if beginning_end == 'beginning':
            retval.extendleft(reversed([arg for arg in args]))
        elif beginning_end == 'end':
            retval.extend([arg for arg in args])

    elif add_remove == 'remove':
        if beginning_end == 'beginning':
            if args:
                for _ in range(args[0]):
                    if retval:
                        retval.popleft()
            else:
                if retval:
                    retval.popleft()

        elif beginning_end == 'end':
            if args:
                for _ in range(args[0]):
                    if retval:
                        retval.pop()
            else:
                if retval:
                    retval.pop()
                    
    return [el for el in retval]
