# Write a program that reads a single string with numbers separated by comma and space ", ". Print the indices of all even numbers.

num_list = [int(x) for x in input().split(', ')]
print_list = [i for i in range(len(num_list)) if num_list[i] % 2 == 0]
print(print_list)