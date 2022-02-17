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
    'up': lambda cell, y: (cell[0]-y, cell[1]),
    'down': lambda cell, y: (cell[0]+y, cell[1]),
    'left': lambda cell, y: (cell[0], cell[1]-y),
    'right': lambda cell, y: (cell[0], cell[1]+y)
}


cell_value = lambda cell: matrix[cell[0]][cell[1]]


def move_A_cell(direction:str, steps:str) -> tuple:   
    
    new_cell = move[direction](A_cell, int(steps))
    
    if 0 <= min(new_cell) and max(new_cell) < matrix_size:
        if cell_value(new_cell) in ('.', 'A'):
            return new_cell
     
    return A_cell


def shoot(direction:str) -> tuple:     
    target_cell = A_cell
    while True:
        target_cell = move[direction](target_cell, 1)    
        if min(target_cell) < 0 or max(target_cell) == matrix_size:
            return None

        if cell_value(target_cell) == 'x':
            return target_cell


matrix_size = 5
matrix = [[el for el in input().split()] for _ in range(matrix_size)]
A_cell = next(((x,y) for x in range(matrix_size) for y in range(matrix_size) if matrix[x][y] == 'A'))
starting_targets = sum([row.count('x') for row in matrix])
shot_targets = []

for _ in range(int(input())):
        input_line = input().split()
        command, args = input_line[0], input_line[1:]

        if command == 'move':
            A_cell = move_A_cell(*args)
        
        elif command == 'shoot':
            hit_target = shoot(*args)
            if hit_target:
                matrix[hit_target[0]][hit_target[1]] = '.'
                shot_targets.append(list(hit_target))
        
if len(shot_targets) == starting_targets:
    print(f'Training completed! All {starting_targets} targets hit.')
else:
    print(f'Training not completed! {starting_targets-len(shot_targets)} targets left.')

if shot_targets:
    print(*shot_targets, sep='\n')