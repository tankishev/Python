# Write a function called numbers_searching which receives a different amount of parameters. All parameters will be
# integer numbers forming a sequence of consecutive numbers. Your task is to find an unknown amount of duplicates from
# the given sequence and a missing value, such that all the duplicate values and the missing value are between the smallest and the biggest received number.
# The function should return a list with the last missing number as a first argument and a sorted list, containing the duplicates found, in ascending order.
# For example: if we have the following numbers: 1, 2, 4, 2, 5, 4 will return 3 as missing number and 2, 4 as duplicate numbers in the following format: [3, [2, 4]]
# Input
# •	There will be no input
# •	Parameters will be passed to your function
# Output
# •	The function should return a list in the following format: [missing number, [duplicate_numbers separated with comma and space]]


def numbers_searching(*args) -> list:
    duplicates = [arg for arg in args if args.count(arg) > 1]
    missing = next((i for i in range(min(args), max(args)) if i not in args))
    retval = list()
    retval.append(missing)
    retval.append(sorted(set(duplicates)))
    return retval
