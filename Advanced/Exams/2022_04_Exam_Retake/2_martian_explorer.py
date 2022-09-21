def validate_cell(cell: tuple) -> tuple:
    x, y = cell
    if x == 6:
        x = 0
    elif x == -1:
        x = 5
    if y == 6:
        y = 0
    elif y == -1:
        y = 5
    return x, y


def get_cell(cell: tuple, field: list) -> str:
    row, col = cell
    return field[row][col]


def set_cell(cell: tuple, field: list, value: int) -> None:
    row, col = cell
    matrix[row][col] = value


move = {
    'up': lambda x: (x[0]-1, x[1]),
    'down': lambda x: (x[0]+1, x[1]),
    'left': lambda x: (x[0], x[1]-1),
    'right': lambda x: (x[0], x[1]+1)
}


deposits = {
    'W': ['Water', 0],
    'M': ['Metal', 0],
    'C': ['Concrete', 0]
}


matrix = [[x for x in input().split(' ')] for _ in range(6)]
current_position = next((x, y) for x in range(6) for y in range(6) if matrix[x][y] == 'E')
commands = input().split(', ')

for command in commands:
    next_position = move[command](current_position)
    next_position = validate_cell(next_position)
    row, col = next_position
    item_at_cell = get_cell(next_position, matrix)
    if item_at_cell in ('W', 'M', 'C'):
        deposits[item_at_cell][1] += 1
        print(f"{deposits[item_at_cell][0]} deposit found at ({row}, {col})")
        set_cell(current_position, matrix, '-')
        set_cell(next_position, matrix, 'E')
    elif item_at_cell == 'R':
        print(f"Rover got broken at ({row}, {col})")
        break
    current_position = next_position

if deposits['W'][1] > 0 and deposits['C'][1] > 0 and deposits['M'][1] > 0:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
