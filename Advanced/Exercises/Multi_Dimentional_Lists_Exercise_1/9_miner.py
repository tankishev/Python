# You are going to create a game called "Miner".
# First, you will receive the size of a square field in which the miner should move. 
# On the second line, you will receive the commands for the miner's movement, separated by a single space. The possible commands are "left", "right", "up" and "down". 
# In the end, you will receive each row of the field on a separate line. The possible characters that may appear on the screen are:
# •	* - a regular position on the field
# •	e - the end of the route
# •	c - coal
# •	s - miner
# The miner starts moving from the position "s". He should perform the given commands successively, moving with only one position in the given direction. If the miner has reached the edge of the field and the following command indicates that he has to get out of the area, he must remain in his current position and ignore the command.
# When the miner finds coal, he collects it and replaces it with "*". Keep track of the collected coal. In the end, you should print whether the miner has succeeded in collecting the coal or not and his final position:
# •	If the miner has collected all coal in the field, the program stops, and you should print the message: "You collected all coal! ({row_index}, {col_index})".
# •	If the miner steps at "e", the game is over (the program stops), and you should print the message: "Game over! ({row_index}, {col_index})".
# •	If there are no more commands and none of the above cases had happened, you should print the message: "{number_of_remaining_coal} pieces of coal left. ({row_index}, {col_index})".
# Input
# •	Field size - an integer number
# •	Commands to move the miner - a sequence of directions, separated by single whitespace (" ")
# •	The field: some of the following characters ("*", "e", "c ", "s"), separated by a single whitespace (" ")
# Output
# •	There are three types of output as mentioned above.



direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

def move(cell:tuple, direction:tuple) -> tuple:
    global matrix
    new_x = cell[0] + direction[0]
    new_y = cell[1] + direction[1]

    if 0 <= new_x < len(matrix):
        if 0 <= new_y < len(matrix[0]):
            return new_x, new_y
    else:
        return cell

def collect(cell:tuple) -> bool:
    global collected_coal
    row, col = cell
    symbol = matrix[row][col]
    if symbol == 'e':
        return False
    elif symbol == 'c':
        collected_coal += 1
        matrix[row][col] = '*'
    return True

size = int(input())
commands = input().split()
matrix = [[x for x in input().split()] for _ in range(size)]
starting_coal = 0
collected_coal = 0

for i, row in enumerate(matrix):
    starting_coal += row.count('c')    
    if 's' in row:
        position = (i, row.index('s'))

for command in commands:
    new_position = move(position, direction[command])
    if new_position:
        position = new_position
        if collect(position):
            game_over = False
            continue
        else:
            game_over = True
            break

if game_over:
    print(f"Game over! {position}")
elif collected_coal == starting_coal:
    print(f"You collected all coal! {position}")
else:
    print(f"{starting_coal - collected_coal} pieces of coal left. {position}")