# Write a program that reads a number - N, representing the rows and columns of a square matrix. 
# On the next N lines, you will receive rows of the matrix. Each row consists of ASCII characters. 
# After that, you will receive a symbol. Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".
# You should start searching from the top left. If there is no such symbol print the message "{symbol} does not occur in the matrix".

size = int(input())

matrix = []
unique_set = set()

for i in range(size):
    row = [x for x in input()]
    matrix.append(row)
    unique_set.update(row)

find_char = input()

if find_char not in unique_set:
    print(f"{find_char} does not occur in the matrix")
else:
    for i in range(size):
        if find_char in matrix[i]:
            print(f'({i}, {matrix[i].index(find_char)})')
            break

