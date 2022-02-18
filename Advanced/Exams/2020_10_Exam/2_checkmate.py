# You will be given a chess board (8x8). On the board there will be 3 types of symbols:
# •	"." – empty square
# •	"Q" – a queen
# •	"K" – the king
# Your job is to find which queens can capture the king and print them. The moves that the queen can do is to move
# diagonally, horizontally and vertically (basically all the moves that all the other figures can do except from the
# knight). Beware that there might be queens that stand in the way of other queens and can stop them from capturing
# the king. For more clarification see the examples.
# Input
# •	8 lines – the state of the board (each square separated by single space)
# Output
# •	The positions of the queens that can capture the king as lists
# •	If the king cannot be captured, print: "The king is safe!"
# •	The order of output does not matter


def get_cell(cell: tuple, matrix: list) -> str:
    row, col = cell
    return str(matrix[row][col])


def is_valid_cell(cell: tuple) -> bool:
    if min(cell) >= 0 and max(cell) < 8:
        return True
    else:
        return False


def possible_moves(cell: tuple, matrix: list) -> tuple:
    retval = []
    row, col = cell

    for i in range(row - 1, -1, -1):
        j = col - (row - i)
        if is_valid_cell((i, j)):
            if get_cell((i, j), matrix) == 'Q':
                break
            retval.append((i, j))

    for i in range(row - 1, -1, -1):
        j = col
        if is_valid_cell((i, j)):
            if get_cell((i, j), matrix) == 'Q':
                break
            retval.append((i, j))

    for i in range(row - 1, -1, -1):
        j = col + (row - i)
        if is_valid_cell((i, j)):
            if get_cell((i, j), matrix) == 'Q':
                break
            retval.append((i, j))

    for i in range(row + 1, 8):
        j = col - (row - i)
        if is_valid_cell((i, j)):
            if get_cell((i, j), matrix) == 'Q':
                break
            retval.append((i, j))

    for i in range(row + 1, 8):
        j = col
        if is_valid_cell((i, j)):
            if get_cell((i, j), matrix) == 'Q':
                break
            retval.append((i, j))

    for i in range(row + 1, 8):
        j = col + (row - i)
        if is_valid_cell((i, j)):
            if get_cell((i, j), matrix) == 'Q':
                break
            retval.append((i, j))

    for j in range(col - 1, -1, -1):
        i = row
        if is_valid_cell((i, j)):
            if get_cell((i, j), matrix) == 'Q':
                break
            retval.append((i, j))

    for j in range(col + 1, 8):
        i = row
        if is_valid_cell((i, j)):
            if get_cell((i, j), matrix) == 'Q':
                break
            retval.append((i, j))

    return tuple(retval)


def take_king(moves: tuple, matrix: list) -> bool:
    for cell in moves:
        if get_cell(cell, matrix) == 'K':
            return True

    return False


def main() -> None:
    retval = []
    matrix = [[el for el in input().split()] for _ in range(8)]
    for row in range(8):
        for col in range(8):
            if get_cell((row, col), matrix) == 'Q':
                moves = possible_moves((row, col), matrix)
                if take_king(moves, matrix):
                    retval.append([row, col])

    if retval:
        for el in retval:
            print(el)
    else:
        print('The king is safe!')


if __name__ == '__main__':
    main()
