# Trifon has finally become a junior developer and has received his first task. It is about manipulating a list of integers. 
# He is not quite happy about it since he hates manipulating lists. They will pay him a lot of money, though, 
# and he is willing to give somebody half of it if to help him do his job. On the other hand, you love lists (and money), so you decide to try your luck.
# 
# The list may be manipulated by one of the following commands:
# - "exchange {index}" – splits the list after the given index and exchanges the places of the two resulting sub-lists. 
#   E.g., [1, 2, 3, 4, 5] -> "exchange 2" -> result: [4, 5, 1, 2, 3]
#   --> If the index is outside the boundaries of the list, print "Invalid index"
#   --> A negative index is considered invalid
# 
# -	"max even/odd"– returns the INDEX of the max even/odd element. E.g., [1, 4, 8, 2, 3] -> "max odd" -> print: 4
# •	"min even/odd" – returns the INDEX of the min even/odd element. E.g. [1, 4, 8, 2, 3] -> "min even" -> print: 3
# o	If there are two or more equal min/max elements, return the index of the rightmost one
# o	If a min/max even/odd element cannot be found, print "No matches"
# 
# •	"first {count} even/odd" – returns the first count even/odd elements. E.g. [1, 8, 2, 3] -> "first 2 even" -> print [8, 2]
# •	"last {count} even/odd" – returns the last count even/odd elements. E.g. [1, 8, 2, 3] -> "last 2 odd" -> print [1, 3]
# o	If the count is greater than the list length, print "Invalid count"
# o	If there are not enough elements to satisfy the count, print as many as you can. If there are zero even/odd elements, print an empty list "[]"
# 
# •	"end" - stop taking input and print the final state of the list
# 
# Input
# •	The input data should be read from the console.
# •	On the first line, the initial list is received as a line of integers, separated by a single space.
# •	On the following lines, until the command "end" is received, you will receive the list manipulation commands.
# •	The input data will always be valid and in the format described. There is no need to check it explicitly.
# Output
# •	The output should be printed on the console.
# •	On a separate line, print the output of the corresponding command.
# •	On the last line, print the final list in square brackets with its elements separated by a comma and a space.
# •	See the examples below to get a better understanding of your task.
# Constraints
# •	The number of input lines will be in the range [2 … 50].
# •	The list elements will be integers in the range [0 … 1000].
# •	The number of elements will be in the range [1 .. 50].
# •	The split index will be an integer in the range [-231 … 231 – 1].
# •	The first/last count will be an integer in the range [1 … 231 – 1].
# •	There will not be redundant whitespace anywhere in the input.
# •	Allowed working time for your program: 0.1 seconds. Allowed memory: 16 MB.


rightmost_index = lambda x,y: max([i for i in range(len(x)-1,-1,-1) if x[i]==y])

filter_even = lambda x: (x % 2) == 0
filter_odd = lambda x: (x % 2) != 0

last_elements = lambda x, i: x[-i:]
first_elements = lambda x, i: x[:i]

def filter_list(input_list,type):
    if type == 'even':
        return list(filter(filter_even, input_list))
    elif type == 'odd':
        return list(filter(filter_odd, input_list))

def exchange_index(index,input_list):
    output = []
    output = input_list[index+1:]
    output.extend(input_list[:index+1])
    return output

input_data = input()
input_list = [int(x) for x in input_data.split(' ')]
input_command = input()
while input_command != 'end':
    command = [x for x in input_command.split(' ')]
    if command[0] == 'exchange':
        index = int(command[1])
        if index < 0 or index > (len(input_list) - 1):
            print('Invalid index')
        else:
            input_list = exchange_index(index,input_list)
    
    elif command[0] in ('max','min'):
        temp_list = filter_list(input_list,command[1])
        if temp_list:
            if command[0] == 'max':
                temp_num = max(temp_list)
            elif command[0] == 'min':
                temp_num = min(temp_list)

            output = rightmost_index(input_list,temp_num)
            print(output)    
        else: 
            print('No matches')

    elif command[0] in ('first','last'):
        temp_list = filter_list(input_list,command[2])
        num = int(command[1])
        if num > len(input_list):
            print('Invalid count')
        else:
            if command[0] == 'first':
                temp_list = first_elements(temp_list,num)
            elif command[0] == 'last':
                temp_list = last_elements(temp_list,num)
            print(temp_list)
    
    input_command = input()

else:
    print (input_list)