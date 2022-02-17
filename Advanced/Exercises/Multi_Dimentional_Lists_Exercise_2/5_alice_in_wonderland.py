# You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines, you will receive the rows of the territory:
# •	Alice will be placed in a random position, marked with the letter "A". 
# •	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
# •	There will always be one rabbit hole on the territory marked with the letter "R".
# •	All of the empty positions will be marked with ".".
# After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left" or "right".
# When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends. 
# In the end, the path she walked had to be marked with '*'.
# For more clarifications, see the examples below.
# Input
# •	On the first line, you will be given the integer n – the size of the square matrix
# •	On the following n lines - matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will be given a move command
# Output
# •	On the first line: 
# o	If Alice steps on the rabbit hole or she go out of the territory, print: 
# "Alice didn't make it to the tea party."
# o	If she collected at least 10 bags of tea, print: 
# "She did it! She went to the party."
# •	On the following lines, print the matrix.


move = {
    'up': lambda x: [x[0]-1, x[1]],
    'down': lambda x: [x[0]+1, x[1]],
    'left': lambda x: [x[0], x[1]-1],
    'right': lambda x: [x[0], x[1]+1]
}

cell_value = lambda idx: matrix[idx[0]][idx[1]]

matrix = [[el for el in input().split()] for _ in range(int(input()))]
A_cell  = next((x,y) for x in range(len(matrix)) for y in range(len(matrix)) if matrix[x][y] == 'A')
matrix[A_cell[0]][A_cell[1]] = '*'
tea_bags = 0

while True:
    direction = input()
    A_cell = move[direction](A_cell)
    
    if min(A_cell) < 0 or max(A_cell) == len(matrix): 
        break
    elif cell_value(A_cell) == 'R':
        matrix[A_cell[0]][A_cell[1]] = '*'    
        break
    else:
        value = cell_value(A_cell)
        if value.isnumeric():
            tea_bags += int(value)

        matrix[A_cell[0]][A_cell[1]] = '*'
        if tea_bags >= 10:
            print("She did it! She went to the party.")
            break

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")

for row in matrix:
    print(' '.join(row))