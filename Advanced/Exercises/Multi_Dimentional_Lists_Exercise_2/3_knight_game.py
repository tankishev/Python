# A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same row, column, or diagonal. 
# (e.g., it can move two squares horizontally, then one square vertically, or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
# The knight game is played on a board with dimensions N x N.
# You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights that can attack one another with one move are left.
# Input
# •	On the first line, you will receive integer N - the size of the board
# •	On the following N lines, you will receive strings with "K" and "0"
# Output
# •	Print a single integer with the minimum number of knights that need to be removed



knight_moves = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
    )

def allowed_moves(cell:tuple) -> list:
    temp_moves = [(x + cell[0], y + cell[1]) for x, y in knight_moves]
    return list(filter(lambda item: min(item[0],item[1]) >= 0 and max(item[0],item[1]) < matrix_size,temp_moves))

def update_take_moves(data:dict) -> dict:
    for key in data.keys():
        data[key] = [x for x in data[key] if x in data.keys()]
    return {k:v for k, v in data.items() if v}

matrix_size = int(input())
knights = {}

for i in range(matrix_size):
    line = input()
    for j in range(matrix_size):
        if line[j] == 'K':
            knights[(i, j)] = allowed_moves((i,j))
knights = update_take_moves(knights)

removes = 0
while knights:
    removes += 1

    s = [k for k, v in sorted(knights.items(), key=lambda item: len(item[1]), reverse=True)]
    
    knights.pop(s[0])
    knights = update_take_moves(knights)

print(removes)