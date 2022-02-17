move = {
    'up': lambda cell: (cell[0] - 1, cell[1]),
    'down': lambda cell: (cell[0] + 1, cell[1]),
    'left': lambda cell: (cell[0], cell[1] - 1),
    'right': lambda cell: (cell[0], cell[1] + 1)
}


def move_cell(cell:tuple, direction:str) -> tuple:
    new_cell = move[direction](cell)
    if min(new_cell) < 0 or max(new_cell) == len(matrix):
        return cell
    else:
        return new_cell

def set_cell(cell:tuple, value:str):
    global matrix
    matrix[cell[0]][cell[1]] = value

cell_value = lambda cell: matrix[cell[0]][cell[1]]


presents = int(input())
matrix = [[el for el in input().split()] for _ in range(int(input()))]
S_cell = next((x, y) for x in range(len(matrix)) for y in range(len(matrix)) if matrix[x][y] == 'S')
num_nice = sum([row.count('V') for row in matrix])

while presents > 0:
    direction = input()
    if direction == 'Christmas morning':
        break

    set_cell(S_cell, '-')
    S_cell = move_cell(S_cell, direction)
    value = cell_value(S_cell)
    set_cell(S_cell, 'S')

    if value == 'V':
        presents -= 1

    elif value == 'C':
        possible_cells = [move_cell(S_cell, key) for key in move.keys()]
        if possible_cells:
            if S_cell in possible_cells:
                possible_cells.remove(S_cell)
        
            for cell in possible_cells:
                if cell_value(cell) in ('X', 'V'):
                    set_cell(cell,'-')
                    presents -= 1


remaining_nice = sum([row.count('V') for row in matrix])
if presents <= 0 and remaining_nice > 0:
    print('Santa ran out of presents!')
for row in matrix:
    print(' '.join(row))
if remaining_nice <= 0:
    print(f"Good job, Santa! {num_nice} happy nice kid/s.")
else:
    print(f'No presents for {remaining_nice} nice kid/s.')