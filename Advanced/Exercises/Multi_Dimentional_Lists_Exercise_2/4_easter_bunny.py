# On the first line, you will be given a number representing the size of the field. On the following few lines, you will be given a field with:
# •	One bunny - randomly placed in it and marked with the symbol "B"
# •	Number of eggs placed at different positions of the field and traps marked with "X"
# Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.
# Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
# Input
# •	A number representing the size of the field
# •	The matrix representing the field (each position separated by a single space)
# Output
# •	The direction which should be considered as best (lowercase)
# •	The field positions from which we are collecting eggs as lists
# •	The total number of eggs collected


move = {
    'up': lambda x: [x[0]-1, x[1]],
    'down': lambda x: [x[0]+1, x[1]],
    'left': lambda x: [x[0], x[1]-1],
    'right': lambda x: [x[0], x[1]+1]
}

eggs = {}

field = [[x for x in input().split()] for _ in range(int(input()))]

starting_position = next((x, y) for x in range(len(field)) for y in range(len(field)) if field[x][y]=='B')

for direction in move.keys():
    position = starting_position
    while True:
        position = move[direction](position)
        row, col = position
        if min(row,col) < 0 or max(row, col) == len(field):
            break
        elif field[row][col] == 'X':
            break
        else:
            if direction not in eggs:
                eggs[direction] = {'cells': [], 'sum': 0}
            eggs[direction]['cells'].append(position)
            eggs[direction]['sum'] += int(field[row][col])

max_key = [k for k, v in sorted(eggs.items(), key=lambda item: item[1]['sum'], reverse=True)][0]
print(max_key)
print(*eggs[max_key]['cells'], sep='\n')
print(eggs[max_key]['sum'])
