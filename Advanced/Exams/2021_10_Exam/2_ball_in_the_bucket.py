# You will be given a matrix with 6 rows and 6 columns representing the board. On the board, there will be points
# (integers) and buckets marked with the letter "B". Rules of the game:
# •	You can throw a ball only 3 times.
# •	When you hit a bucket (position marked with 'B'), you score the sum of the points in the same column.
# •	You can hit a bucket only once. If you hit the same bucket again, you do not score any points.
# •	If you hit outside a bucket (hit a number on the board) or outside the board, you do not score any points.
# After the board state, you are going to receive the information for every throw on a separate line. The coordinates’
# information of a hit will be in the format: "({row}, {column})".
# Depending on how many points you have collected, you win one of the following:
# Football	100 to 199 points
# Teddy Bear	200 to 299 points
# Lego Construction Set	300 and more points
#
# Your job is to keep track of the scored points and to check if you won a prize.
# For more clarifications, see the examples below.
# Input
# •	6 lines – matrix representing the board (each position separated by a single space)
# •	On the next 3 lines - the coordinates of the throw in the format: "({row}, {column})"
#
# Output
# •	On the first line:
# o	If you won a prize, print:
# "Good job! You scored {points} points, and you've won {prize}."
# o	If you did not win any prize, print the points you need to get at least the first prize:
# "Sorry! You need {points} points more to win a prize."


def get_cell(cell: tuple, matrix: list) -> str:
    row, col = cell
    return matrix[row][col]


def set_cell(cell: tuple, matrix: list, value: int) -> None:
    row, col = cell
    matrix[row][col] = value


def is_valid_cell(cell: tuple, matrix_size: int) -> bool:
    return min(cell) >= 0 and max(cell) < matrix_size


def get_col_value(cell: tuple, matrix: list) -> int:
    row, col = cell
    retval = 0
    for i in range(len(matrix)):
        if i != row:
            val = get_cell((i, col), matrix)
            if val.isnumeric():
                retval += int(val)

    return retval


def main() -> None:
    prices = {
        1: 'Football',
        2: 'Teddy Bear',
        3: 'Lego Construction Set'
    }
    pts = 0
    matrix = [[el for el in input().split()] for _ in range(6)]

    for _ in range(3):
        cell = tuple(map(int, input().replace('(', '').replace(')', '').split(', ')))
        if not is_valid_cell(cell, len(matrix)):
            continue

        value = get_cell(cell, matrix)

        if value == 'B':
            pts += get_col_value(cell, matrix)
            set_cell(cell, matrix, 0)

    if pts < 100:
        print(f"Sorry! You need {100 - pts} points more to win a prize.")
    elif pts > 400:
        print(f"Good job! You scored {pts} points, and you've won Lego Construction Set.")
    else:
        print(f"Good job! You scored {pts} points, and you've won {prices.get(pts//100)}.")


if __name__ == '__main__':
    main()
