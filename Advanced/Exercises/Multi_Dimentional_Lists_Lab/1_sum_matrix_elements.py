# Write a program that reads a matrix from the console and prints:
# •	The sum of all numbers in the matrix
# •	The matrix itself
# On the first line, you will receive the matrix sizes in the format "{rows}, {columns}". 
# On the next rows, you will get elements for each column separated by a comma and a space ", ". 


rows, cols = input().split(', ')
matrix = []
sum_of_elements = 0 

for _ in range(int(rows)):
    column = [int(x) for x in input().split(', ')]
    matrix.append(column)
    sum_of_elements += sum(column)
  
print(sum_of_elements)
print(matrix)