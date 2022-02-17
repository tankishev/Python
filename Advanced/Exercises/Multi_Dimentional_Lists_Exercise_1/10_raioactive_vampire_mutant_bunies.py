# First, you will receive a line holding integers N and M, representing the lair's rows and columns.
# Next, you receive N strings that can consist only of ".", "B", "P". They represent the initial state of the lair. There will be only one player. The bunnies are marked with "B", the player is marked with "P", and everything else is free space, marked with a dot ".". 
# Then you will receive a string with commands (e.g., LRRULUD) - each letter represents the next move of the player:
# •	L - the player should move one position to the left
# •	R - the player should move one position to the right
# •	U - the player should move one position up
# •	D - the player should move one position down
# After every step made, each bunny spreads one position up, down, left, and right. If the player moves to a bunny cell or a bunny reaches the player, the player dies. If the player goes out of the lair without encountering a bunny, the player wins.
# When the player dies or wins, the game ends. All the activities for this turn continue (e.g., all the bunnies spread normally), but there are no more turns. There will be no cases where the moves of the player end before he dies or escapes.
# In the end, print the final state of the lair with every row on a separate line. On the last line, print either "dead: {row} {col}" or "won: {row} {col}". "Row" and "col" are the cell coordinates where the player has died or the last cell he has been in before escaping the lair.
# Input
# •	On the first line of input, the numbers N and M are received - the number of rows and columns in the lair
# •	On the following N lines, each row is received in the form of a string. The string will contain only ".", "B", "P". All strings will be the same length. There will be only one "P" for all the input
# •	On the last line, the directions are received in the form of a string, containing "R", "L", "U", "D"
# Output
# •	On the first N lines, print the final state of the bunny lair
# •	On the last line, print:
# o	If the player won - "won: {row} {col}"
# o	If the player dies - "dead: {row} {col}"


direction = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def move(cell:tuple, direction:tuple) -> tuple:
    global matrix
    x, y = cell
    matrix[x][y] = '.'

    new_x = x + direction[0]
    new_y = y + direction[1]

    if 0 <= new_x < rows:
        if 0 <= new_y < cols:
            if matrix[new_x][new_y] != 'B': 
                matrix[new_x][new_y] = 'P'
            return new_x, new_y
        else: return -1, -1
    else:
        return -1, -1

    
def bunny_spread() -> None:
    global matrix
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] not in ('B', 'b'):
                if row - 1 >= 0:
                    if matrix[row - 1][col] == 'B': matrix[row][col] = 'b'
                if row + 1 < rows:
                    if matrix[row + 1][col] == 'B': matrix[row][col] = 'b'
                if col - 1 >= 0:
                    if matrix[row][col - 1] == 'B': matrix[row][col] = 'b'
                if col + 1 < cols:
                    if matrix[row][col + 1] == 'B': matrix[row][col] = 'b'
    matrix = [['B' if x =='b' else x for x in y] for y in matrix]

rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    matrix.append([x for x in input()])
    if 'P' in matrix[i]:
        row, col = i, matrix[i].index('P')
commands = [x for x in input()]

for command in commands:
    new_position = move((row, col), direction[command])
    bunny_spread()
    if new_position == (-1, -1):
        win = True  
        break
    else:
        row, col = new_position
        if matrix[row][col] == 'B':
            win = False
            break

for data in matrix:
    print(''.join(data))

if win:
    print(f"won: {row} {col}")
else:
    print(f"dead: {row} {col}")