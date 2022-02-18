def get_cell(cell: tuple, matrix: list) -> str:
    row, col = cell
    return matrix[row][col]


def multiple_pts(cell: tuple, matrix: list, multiple: int) -> int:
    row, col = cell
    pts_cells = [ 
        (0, col), 
        (6, col), 
        (row, 0), 
        (row, 6)
        ]
    retval = sum([int(get_cell(c, matrix)) for c in pts_cells]) 
    return retval * multiple


def main() -> None:
    current_player, next_player = input().split(', ')
    matrix = [[el for el in input().split()] for _ in range(7)]
    scoreboard = {player: {'trows': 0, 'pts': 501} for player in (current_player, next_player)}

    while True:
        cell = tuple(map(int, input().replace('(', '').replace(')', '').split(', ')))
        scoreboard[current_player]['trows'] += 1

        if min(cell) < 0 or max(cell) >= 7:
            continue

        pts = 0
        value = get_cell(cell, matrix)
        if value.isnumeric():
            pts = int(value)

        elif value == 'D':
            pts = multiple_pts(cell, matrix, 2)

        elif value == 'T':
            pts = multiple_pts(cell, matrix, 3)

        scoreboard[current_player]['pts'] -= pts
        if value == 'B' or scoreboard[current_player].get('pts') <= 0:
            break

        current_player, next_player = next_player, current_player

    winning_trows = scoreboard[current_player].get('trows')
    print(f'{current_player} won the game with {winning_trows} throws!')


if __name__ == '__main__':
    main()
