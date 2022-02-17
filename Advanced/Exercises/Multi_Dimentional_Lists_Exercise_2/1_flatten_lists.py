# Write a program to flatten several lists of numbers received in the following format:
# 	String with numbers or empty strings separated by "|"
# 	Values are separated by spaces (" ", one or several)
# 	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below

input_line = input()
while "  " in input_line:
    input_line = input_line.replace('  ', ' ')
else:
    data = [x for x in reversed([y.strip() for y in input_line.split('|')]) if x != '']
    print(' '.join(data).strip())
