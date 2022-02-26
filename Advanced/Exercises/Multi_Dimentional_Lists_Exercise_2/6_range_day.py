# You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a single space:
# •	Your position is marked with the symbol "A"
# •	Targets marked with symbol "x"
# •	All of the empty positions will be marked with "."
# After the field state, you will be given an integer representing the number of commands you will receive. The possible commands are:
# •	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only move if the field you want to step on is marked with ".".
# •	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving). Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot only the nearest target. When you have shot a target, the field becomes empty position (".").
# Validate the positions since they can be outside the field.
# Keep track of all the shot targets:
# •	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets} targets hit.". 
# •	If, after you perform all the commands, there are some targets left print: "Training not completed! {count_left_targets} targets left.".
# Finally, print the index positions of the targets that you hit, as shown in the examples.
# Input
# •	5 lines representing the field (symbols, separated by a single space)
# •	N - count of commands
# •	On the following N lines - the commands in the format described above
# Output
# •	On the first line, print one of the following:
# o	If all the targets were shot
# "Training completed! All {count_targets} targets hit."
# o	Otherwise:
#               	       "Training not completed! {count_left_targets} targets left."
# •	Finally, print the index positions "[{row}, {column}]" of the targets that you hit, as shown in the examples.


move = {
    'up': lambda cell, steps: (cell[0] - steps, cell[1]),
    'down': lambda cell, steps: (cell[0] + steps, cell[1]),
    'left': lambda cell, steps: (cell[0], cell[1] - steps),
    'right': lambda cell, steps: (cell[0], cell[1] + steps)
}


def move_a_cell(matrix: list, cell: tuple, direction: str, steps: int) -> tuple:
    ''' Move the shooter cell. If new cell is out of range returns the current cell '''
    new_cell = move[direction](cell, int(steps))
    if cell_valid(new_cell):
        if get_value(matrix, new_cell) in ('.', 'A'):
            return new_cell
    return cell


def cell_valid(cell: tuple) -> bool:
    ''' Validates if cell is out of range'''
    if 0 <= min(cell) and max(cell) < 5:
        return True
    else:
        return False


def shoot(matrix: list, cell: tuple, direction: str) -> tuple:
    ''' Finds an 'x' cell in the firing direction. \
        Returns none if no targes in that direction'''
    target_cell = move[direction](cell, 1)
    while cell_valid(target_cell):
        if get_value(matrix, target_cell) == 'x':
            return target_cell
        target_cell = move[direction](target_cell, 1)


def get_value(matrix: list, cell: tuple) -> str:
    ''' Gets the value at the x,y coordinates in the matrix'''
    row, col = cell
    return str(matrix[row][col])


def set_value(matrix: list, cell: tuple, value: str) -> list:
    ''' Changes the value at the x, y coordinates in the matrix '''
    row, col = cell
    matrix[row][col] = value
    return matrix


def main() -> None:

    matrix = []
    shot_targets = []
    starting_targets = 0
    a_cell = None

    for i in range(5):
        row = [el for el in input().split()]
        matrix.append(row)
        starting_targets += row.count('x')
        if 'A' in row:
            a_cell = (i, row.index('A'))

    for _ in range(int(input())):
        input_line = input().split()

        command, direction = input_line[0], input_line[1]
        
        if command == 'move':
            steps = int(input_line[2])
            a_cell = move_a_cell(matrix, a_cell, direction, steps)

        elif command == 'shoot':
            hit_target = shoot(matrix, a_cell, direction)
            if hit_target:
                matrix = set_value(matrix, hit_target, '.')
                shot_targets.append(list(hit_target))

        if len(shot_targets) == starting_targets:
            break

    if len(shot_targets) == starting_targets:
        print(f'Training completed! All {starting_targets} targets hit.')

    else:
        print(f'Training not completed! {starting_targets-len(shot_targets)} targets left.')

    if shot_targets:
        print(*shot_targets, sep='\n')


if __name__ == '__main__':
    main()
