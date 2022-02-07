# Write a program that receives a sequence of numbers, 
# separated by a single space, and prints their absolute value as a list. Use abs().

def abs_float(lst: list) -> list:
    return [abs(float(x)) for x in lst]

input_data = input().split(' ')
num_list = abs_float(input_data)
print(num_list)