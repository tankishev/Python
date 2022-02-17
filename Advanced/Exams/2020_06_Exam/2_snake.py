# You will be given an integer n for the size of the snake territory with square shape. On the next n lines,
# you will receive the rows of the territory. The snake will be placed on a random position, marked with the letter 'S'.
# On random positions there will be food, marked with '*'. There might also be a lair on the territory.
# The lair has two burrows.
# They are marked with the letter - 'B'. All of the empty positions will be marked with '-'.
# Each turn, you will be given command for the snake’s movement. When the snake moves it leaves a trail marked with '.'
# Move commands will be: "up", "down", "left", "right".
# If the snake moves to a food, it eats the food and increases the food quantity with one.
# If it goes inside of a burrow, it goes out on the position of the other burrow and then both burrows disappear.
# If the snake goes out of its territory, it loses, can't return back and the program ends.
# The snake needs at least 10 food quantity to win.
# When the snake has gone outside of its territory or has eaten enough food, the game ends.
# Input
# •	On the first line, you are given the integer n – the size of the square matrix.
# •	The next n lines holds the values for every row.
# •	On each of the next lines you will get a move command.
# Output
# •	On the first line:
# o	If the snake goes out of its territory, print: "Game over!"
# o	If the snake eat enough food, print: "You won! You fed the snake."
# •	On the second line print all food eaten: "Food eaten: {food quantity}"
# •	In the end print the matrix.


move = {
    'up': lambda cell: (cell[0] - 1, cell[1]),
    'down': lambda cell: (cell[0] + 1, cell[1]),
    'left': lambda cell: (cell[0], cell[1] - 1),
    'right': lambda cell: (cell[0], cell[1] + 1)
}


def cell_value(cell: tuple) -> str:
    return matrix[cell[0]][cell[1]]


def is_valid_cell(cell: tuple) -> bool:
    if min(cell) >= 0 and cell[0] < len(matrix) and cell[1] < len(matrix[0]):
        return True
    else:
        return False 


def set_cell(cell: tuple, value: str) -> None:
    global matrix
    row, col = cell 
    matrix[row][col] = value


def move_snake(cell: tuple, direction_: str) -> tuple:
    global matrix
    global food

    new_cell = move[direction_](cell)
    if is_valid_cell(new_cell):
        set_cell(S_cell, '.')
        if cell_value(new_cell) == '*':
            food += 1
        elif cell_value(new_cell) == 'B':
            set_cell(new_cell, '.')
            new_cell = next((x, y) for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][y] == 'B')
        
        set_cell(new_cell, 'S')

        return new_cell
    else:
        set_cell(S_cell, '.')
        return -1, -1


def print_matrix() -> None:
    for row in matrix:
        print(*row, sep='')
    

matrix = [[el for el in input()] for _ in range(int(input()))]
S_cell = next((x, y) for x in range(len(matrix)) for y in range(len(matrix[0])) if matrix[x][y] == 'S')
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
