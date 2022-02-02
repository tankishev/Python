# You will be given two sequences of strings, separated by ", ".
#  Print a new list containing only the strings from the first input line, which are substrings of any string in the second input line.

list_1 = input().split(', ')
list_2 = input().split(', ')

output_list = []

for x in list_1:
    for y in list_2:
        if x in y:
            output_list.append(x)
            break

print(output_list)

