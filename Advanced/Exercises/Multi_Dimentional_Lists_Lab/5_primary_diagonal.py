# Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom right). 
# On the first line, you will receive an integer N – the size of a square matrix. 
# The next N lines holds the values for each column - N numbers, separated by a single space. 

result = 0

for i in range(int(input())):
    row = [int(x) for x in input().split()]
    result += row[i]

print(result)