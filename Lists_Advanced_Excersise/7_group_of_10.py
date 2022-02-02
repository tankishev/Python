# Write a program that receives a sequence of numbers (a string containing integers separated by ", ")
#  and prints the numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
# Examples:
# •	The numbers 2, 8, 4, and 10 fall into the group of 10's.
# •	The numbers 13, 19, 14, and 15 fall into the group of 20's.
# For more clarification, see the examples below.

from math import ceil

input_nums = list(map(int,input().split(', ')))

for i in range(1, ceil(max(input_nums) / 10) + 1):
    group = list(filter(lambda x: (i - 1) * 10 < x <= i * 10, input_nums))
    print (f"Group of {i}0's: {group}")
