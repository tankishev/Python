# Write a program that receives a sequence of numbers (integers) separated by a single space. 
# It should print a list of only the even numbers. Use filter().

input_list = input().split(' ')
input_list = [int(x) for x in input_list]

output_list = list(filter(lambda x: (x % 2) == 0, input_list))
print(output_list)