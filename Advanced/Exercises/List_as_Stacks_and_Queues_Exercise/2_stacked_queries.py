# You have an empty stack. You will receive an integer – N. On the next N lines you will receive queries. 
# Each query is one of these four types:
# •	'1 {number}' – push the number (integer) into the stack
# •	'2' – delete the number at the top of the stack
# •	'3' – print the maximum number in the stack
# •	'4' – print the minimum number in the stack
# It is guaranteed that each query is valid.
# After you go through all the queries, print the stack from the top to the bottom in the following format:
# "{n}, {n1}, {n2}, ... {nn}"

my_stack = []
for _ in range(int(input())):
    query = input()
    if query[0] == '1':
        my_stack.append(query[2:])
    elif my_stack:
        if query == '2':
            my_stack.pop()
        elif query == '3':
            print(max(my_stack))
        elif query == '4':
            print(min(my_stack))

print(f', '.join([my_stack.pop() for _ in range(len(my_stack))]))
