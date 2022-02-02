# Write a program that receives a sequence of numbers (integers) separated by a single space. 
# It should print a sorted list of numbers in ascending order. Use sorted().


input_string = input()
input_list = [int(x) for x in input_string.split(' ')]

output_list = sorted(input_list)

print(output_list)