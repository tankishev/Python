# Write a program that reads a matrix from the console and prints the sum for each column on separate lines. 
# On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for each column separated with a single space. 

# Solution w/o zip
# rows, cols = input().split(', ')
# matrix = []

# for _ in range(int(rows)):
#     matrix.append([int(x) for x in input().split()])
    
# for col in range(int(cols)):
#     result = sum([x[col] for x in matrix])
#     print(result)

# Solution with zip

rows, cols = input().split(', ')
matrix = [[int(x) for x in input().split()] for _ in range(int(rows))]
transposed = list(zip(*matrix))
for t_row in transposed:
    print(sum(t_row))
