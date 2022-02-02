# Write a program that receives a sequence of numbers (integers) separated by a single space. 
# It should print the min and max values of the given numbers and the sum of all the numbers in the list. 
# Use min(), max() and sum().
# 
# The output should be as follows:
# •	On the first line: "The minimum number is {minimum number}"
# •	On the second line: "The maximum number is {maximum number}"
# •	On the third line: "The sum number is {sum of all numbers}"

input_string = input()
input_list = [int(x) for x in input_string.split(' ')]

minimum_number = min(input_list)
maximum_number = max(input_list)
sum_of_all_numbers = sum(input_list)

print(f"The minimum number is {minimum_number}")
print(f"The maximum number is {maximum_number}")
print(f"The sum number is: {sum_of_all_numbers}")