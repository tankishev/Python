# You will be given a number n representing the number of rows of a board of dots and dashes. 
# On the following n lines, you will receive each row of the board as a string with symbols (dots and dashes only), separated by a single space. 
# Your task is to find and print the largest count of dots that could be connected at once. You could only connect horizontally or vertically.
# Example
# Input	Output
# 5
# . . - - -
# . . - - -
# - - - - -
# - - - . .
# - - - . .	4
# 6
# . . - . - .
# - . . . . .
# - . - - - -
# - . . - - -
# - . . . . -
# - - - . . -	18
# 4
# - . - . . –
# . - . . - .
# . - - - - -
# - - - . - -	4


board = [[x for x in input().split(' ')] for _ in range(int(input()))]

bd_rows = len(board)
bd_cols = max([len(x) for x in board])

processed_cells = []
processed_groups = []

for row in range(bd_rows):
    for col in range(bd_cols):
        if (row,col) in processed_cells:
            continue

        if board[row][col] == '.':
            temp_cells = [(row,col)]
            while True:
                branches = []
                for cell in temp_cells:
                    x, y = cell
                    if x > 0:
                        if board[x - 1][y] == '.' and (x - 1, y) not in temp_cells:
                            branches.append((x - 1, y))
                    if x < bd_rows - 1:
                        if board[x + 1][y] == '.' and (x + 1, y) not in temp_cells:
                            branches.append((x + 1, y))
                    if y > 0:
                        if board[x][y - 1] == '.' and (x, y - 1) not in temp_cells:
                            branches.append((x, y - 1))
                    if y < bd_cols - 1:
                        if board[x][y + 1] == '.' and (x, y + 1) not in temp_cells:
                            branches.append((x, y + 1))

                if branches:
                    for branch in branches:
                        if branch not in temp_cells:
                            temp_cells.extend([branch])

                else:
                    processed_cells.extend(temp_cells)
                    processed_groups.append(len(temp_cells))
                    break

if processed_groups:           
    print(max(processed_groups))
else:
    print(0)