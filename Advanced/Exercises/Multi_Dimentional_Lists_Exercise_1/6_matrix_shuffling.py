# Write a program that reads a matrix from the console and performs certain operations with its elements. User input is provided similarly to the problems above - first, you read the dimensions and then the data. 
# Your program should receive commands in the format: "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two points in the matrix. A valid command starts with the "swap" keyword along with four valid coordinates (no more, no less), separated by a single space.
# •	If the command is valid, you should swap the values at the given indexes and print the matrix at each step (thus, you will be able to check if the operation was performed correctly). 
# •	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered, or the given coordinates are not valid), print "Invalid input!" and move on to the following command. A negative value makes the coordinates not valid.
# Your program should finish when the command "END" is entered.


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for _ in range(rows)]

def valid_command(data: list) -> bool:
    if tokens[0] != 'swap': return False
    if len(tokens) != 5: return False
    coordinates = [int(x) for x in tokens[1:]]
    if min(coordinates) < 0: return False
    x1, y1, x2, y2 = coordinates
    if max(x1, x2) > rows - 1: return False
    if max(y1, y2) > cols - 1: return False
    return True

def print_matrix(data: list) -> None:
    for row in data:
        print(*row, sep=' ')

while True:
    input_line = input()
    if input_line == 'END': break

    tokens = input_line.split()
    if valid_command(tokens):
        x1, y1, x2, y2 = [int(x) for x in tokens[1:]]
        matrix[x1][y1], matrix[x2][y2] = matrix[x2][y2], matrix[x1][y1]
        print_matrix(matrix)

    else:
        print('Invalid input!')
    
