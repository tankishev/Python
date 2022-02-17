# You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
# Print the result back on the console.

input_line = list(input())

my_stack = []
output = []

for i in range(len(input_line)):
    if input_line[i] == '(': 
        my_stack.append(i)
    elif input_line[i] == ')':
        output.append(input_line[my_stack.pop(): i+1])

for res in output:
    print(''.join(res))
