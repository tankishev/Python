# Find the number of all 2x2 squares containing identical chars in a matrix. 
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}". 
# On the following rows, you will receive characters separated by a single space. 
# Print the number of all square matrices you have found.

count_same = 0

rows, cols = [int(x) for x in input().split()]

matrix  = [[x for x in input().split()] for _ in range(rows)]

for i in range(rows - 1):
    for j in range(cols -1):
        sub_matrix = [matrix[r][j:j + 2] for r in range(i,i+2)]
        elements = [x for row in sub_matrix for x in row]
        if len(set(elements)) == 1:
            count_same += 1

print(count_same)
