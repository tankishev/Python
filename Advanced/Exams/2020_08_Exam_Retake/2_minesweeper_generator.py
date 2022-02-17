# You will be given an integer n for the size of the mines field with square shape and another one for the number of
# bombs that you have to place in the field. On the next n lines, you will receive the position for each bomb.
# Your task is to create the game field placing the bombs at the correct positions and mark them with "*", and
# calculate the numbers in each cell of the field. Each cell represents a number of all bombs directly near it
# (up, down, left, right and the 4 diagonals).


def set_cell(cell: tuple, value: str) -> None:
    global matrix
    i, j = cell
    matrix[i][j] = value


def get_cell(cell: tuple) -> str:
    i, j = cell
    return str(matrix[i][j])


def is_valid_cell(cell: tuple) -> bool:
    if min(cell) >= 0 and max(cell) < matrix_size:
        return True
    else:
        return False


def adjacent_cells(cell: tuple) -> tuple:
    i, j = cell
    return tuple([(r, c) for r in range(i-1, i+2) for c in range(j-1, j+2) if is_valid_cell((r, c))])


def adjacent_bombs(cell: tuple) -> int:
    return sum([1 for el in adjacent_cells(cell) if get_cell(el) == '*'])


matrix_size = int(input())
matrix = [[0]*matrix_size for _ in range(matrix_size)]
bombs_num = int(input())
for _ in range(bombs_num):
    row, col = map(int, input().replace('(', '').replace(')', '').split(','))
    set_cell((row, col), '*')

for row in range(matrix_size):
    for col in range(matrix_size):
        if get_cell((row, col)) == '0':
            set_cell((row, col), str(adjacent_bombs((row, col))))

for row in matrix:
    print(*row, sep=' ')
