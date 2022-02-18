# On the first line, you will be given a number representing the size of the field with a square shape. On the
# following few lines, you will be given the field with:
# •	One player - randomly placed in it and marked with the symbol "P"
# •	Numbers for coins placed at different positions of the field
# •	Walls marked with "X"
# After the field state, you will be given commands for the player's movement. Commands can be: "up", "down", "left",
# "right". If the command is invalid, you should ignore it.
# The player moves in the given direction with one step for each command and collects all the coins that come across.
# If he goes out of the field, he should continue to traverse the field from the opposite side in the same direction.
# Note: He can go through the same path many times, but he can collect the coins just once (the first time).
# There are only two possible outcomes of the game:
# •	The player hits a wall, loses the game, and his coins are reduced to 50% and rounded down to the next-lowest number.
# •	The player collects at least 100 coins and wins the game.
# For more clarifications, see the examples below.
# Input
# •	A number representing the size of the field (matrix NxN)
# •	A matrix representing the field (each position separated by a single space)
# •	On each of the following lines, you will get a move command.
# Output
# •	If the player won the game, print: "You won! You've collected {total_coins} coins."
# •	If the player loses the game, print: "Game over! You've collected {total_coins} coins."
# •	Collected coins have to be rounded down to the next-lowest number.
# •	The player's path as cooridnates in lists on separate lines: 
# "Your path:
# [{row_position1}, {column_position1}]
# [{row_position2}, {column_position2}]
# …
# [{row_positionN}, {column_positionN}]"


move = {
    'up': lambda x: [x[0]-1, x[1]],
    'down': lambda x: [x[0]+1, x[1]],
    'left': lambda x: [x[0], x[1]-1],
    'right': lambda x: [x[0], x[1]+1]
}


def traverse_cell(cell: tuple, size: int) -> tuple:
    row, col = cell
    if min(cell) >= 0 and max(cell) < size:
        return cell
    elif row < 0:
        return size - 1, col
    elif row >= size:
        return 0, col
    elif col < 0:
        return row, size - 1
    elif col >= size:
        return row, 0


def get_cell(cell: tuple, matrix: list) -> str:
    row, col = cell
    return str(matrix[row][col])


def set_cell(cell: tuple, matrix: list, value: str) -> None:
    row, col = cell
    matrix[row][col] = value


def main() -> None:
    matrix_size = int(input())
    matrix = [[el for el in input().split()] for _ in range(matrix_size)]
    p_cell = next(((x, y) for x in range(matrix_size) for y in range(matrix_size) if get_cell((x, y), matrix) == 'P'))
    game_over = False
    coins = 0
    path = [[x for x in p_cell]]

    while True:
        direction = input()
        if direction not in move.keys():
            break

        new_cell = move[direction](p_cell)
        new_cell = traverse_cell(new_cell, matrix_size)
        path.append([x for x in new_cell])

        cell_value = get_cell(new_cell, matrix)
        if cell_value == 'X':
            game_over = True
            coins = coins // 2
            break

        coins += int(cell_value)
        set_cell(new_cell, matrix, 'P')
        set_cell(p_cell, matrix, '0')
        p_cell = new_cell

        if coins >= 100:
            break

    if game_over:
        print(f"Game over! You've collected {coins} coins.")
    else:
        print(f"You won! You've collected {coins} coins.")

    print('Your path:')
    print(*path, sep='\n')


if __name__ == '__main__':
    main()
