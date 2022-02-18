# Write function called best_list_pureness which will receive a list of numbers and a number K.
# You have to rotate the list K times (last becomes first) to find the variation of the list with the best pureness
# (pureness is calculated by summing all the elements in the list multiplied by their indices). For example,
# in the list [4, 3, 2, 6] with the best pureness is (3 * 0) + (2 * 1) + (6 * 2) + (4 * 3) = 26.
# At the end the function should return a string containing the highest pureness and the amount of rotations that
# were made to find this pureness in the following format:
# "Best pureness {pureness_value} after {count_rotations} rotations".
# If there is more than one highest pureness, take the first one.
# Note: Submit only the function in the judge system
# Input
# •	There will be no input, just parameters passed to your function
# Output
# •	There is no expected output
# •	The function should return a string in the following format:
# "Best pureness {pureness_value} after {count_rotations} rotations"


from collections import deque


def best_list_pureness(num_list: list, rotations: int) -> str:
    fnc_mem = []
    temp_list = deque(num_list)
    for i in range(rotations + 1):
        pureness = sum([i * num for i, num in enumerate(temp_list)])
        fnc_mem.append((i, pureness))
        temp_list.rotate(1)

    sorted_list = sorted(fnc_mem, key=lambda el: (-el[1], el[0]))
    rotation, value = sorted_list[0]
    return f'Best pureness {value} after {rotation} rotations'
