def is_valid(r, c) -> bool:
    return min(r, c) >= 0 and max(r, c) < 8


def is_taken_cell(r, c, board):
    return board[r][c] == '*'


def is_taken_row(r, board) -> bool:
    return any(el == '*' for el in board[r])


def is_taken_col(c, board) -> bool:
    col = [board[r][c] for r in range(8)]
    return any(el == '*' for el in col)


def is_taken_d(r, c, board):
    for i in range(-7, 8):
        j, k = r + i, c + i
        if not is_valid(j, k):
            continue
        if is_taken_cell(j, k, board):
            return True
    for i in range(-7, 8):
        j, k = r + i, c - i
        if not is_valid(j, k):
            continue
        if is_taken_cell(j, k, board):
            return True
    return False


def is_na(r, c, board) -> bool:
    if not(is_valid(r, c)):
        return True
    if is_taken_cell(r, c, board):
        return True
    if is_taken_col(c, board):
        return True
    if is_taken_row(r, board):
        return True
    if is_taken_d(r, c, board):
        return True
    return False


def print_board(board):
    for row in board:
        print(*row, sep=' ')
    print('')


def place_queens(r=0, board=None):
    if r == 8:
        print_board(board)
        return

    if board is None:
        board = [['-'] * 8 for _ in range(8)]

    for c in range(8):
        board[r] = ['-'] * 8
        if is_na(r, c, board):
            continue
        else:
            board[r][c] = '*'
            place_queens(r + 1, board)
    board[r] = ['-'] * 8


place_queens()
