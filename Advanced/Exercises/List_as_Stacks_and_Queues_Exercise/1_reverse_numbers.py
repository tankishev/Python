# Write a program which reads from the console a string with N integers, separated by a single space, and reverses them using a stack. 
# Print the reversed integers on one line, separated by a single space.

input_lst = [x for x in input().split()]
output = [input_lst.pop() for _ in range(len(input_lst))]
print(*output, sep=' ')