move = {
    'up': lambda cell: (cell[0] - 1, cell[1]),
    'down': lambda cell: (cell[0] + 1, cell[1]),
    'left': lambda cell: (cell[0], cell[1] - 1),
    'right': lambda cell: (cell[0], cell[1] + 1)
}


cell_value = lambda cell: matrix[cell[0]][cell[1]]

def is_valid_cell(cell:tuple) -> bool:
    if min(cell) >=0 and cell[0] < len(matrix) and cell[1] < len(matrix[0]):
        return True
    else:
        return False 


def set_cell(cell:tuple, value:str) -> None:
    global matrix
    row, col = cell 
    matrix[row][col] = value


def move_snake(cell:tuple, direction:str) -> tuple:
    global matrix
    global food

    new_cell = move[direction](cell)
    if is_valid_cell(new_cell):
        set_cell(S_cell, '.')
        if cell_value(new_cell) == '*':
            food += 1
        elif cell_value(new_cell) == 'B':
            set_cell(new_cell, '.')
            new_cell = [(x,y) for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][y] == 'B']
        
        set_cell(new_cell,'S')

        return new_cell
    else:
        return (-1, -1)


def print_matrix() -> None:
    for row in matrix:
        print(*row, sep='')
    

matrix = [[el for el in input()] for _ in range(int(input()))]
S_cell = [(x,y) for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][y] == 'S']
food = 0

while True:
    direction = input()
    S_cell = move_snake(S_cell, direction)
    
    if food == 10: 
        print("You won! You fed the snake.")
        break

    elif S_cell == (-1, -1):
        print("Game over!")
        break

print(f"Food eaten: {food}")
print_matrix()