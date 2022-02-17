# Write program that:
# •	Reads an input string
# •	Reverses it using a stack
# •	Prints the result back on the console

my_stack = list(input())
output = []

for _ in range(len(my_stack)):
    output.append(my_stack.pop())

print(*output, sep='')