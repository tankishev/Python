# Write a program that finds the difference between the sums of the square matrix diagonals (absolute value). 
# On the first line, you will receive an integer N - the size of a square matrix. 
# The following N lines hold the values for each column - N numbers separated by a single space. 
# Print the absolute difference between the primary and the secondary diagonal sums


result = 0
size = int(input())

for i in range(size):
    row = [int(x) for x in input().split()]
    result += row[i] -row[-i-1]
    
print(abs(result))