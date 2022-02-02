# Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list. Use round().

input_list = input().split(' ')
input_list = [round(float(x)) for x in input_list]
print (input_list)