# You will be given a string. Then, you will be given an integer N for the size of the field with square shape. On the next N lines, you will receive the rows of the field. The player will be placed on a random position, marked with "P". On random positions there will be letters. All of the empty positions will be marked with "-".
# Each turn you will be given commands for the player’s movement. If he moves to a letter, he consumes it, concatеnates it to the initial string and the letter disappears from the field. If he tries to move outside of the field, he is punished - he loses the last letter in the string, if there are any, and the player’s position is not changed.
# At the end print all letters and the field.
# Input
# •	On the first line, you are given the initial string
# •	On the second line, you are given the integer N - the size of the square matrix
# •	The next N lines holds the values for every row
# •	On the next line you receive a number M
# •	On the next M lines you will get a move command
# Output
# •	On the first line the final state of the string
# •	In the end print the matrix


move = {
    'up': lambda x: [x[0]-1, x[1]],
    'down': lambda x: [x[0]+1, x[1]],
    'left': lambda x: [x[0], x[1]-1],
    'right': lambda x: [x[0], x[1]+1]
}


def is_valid_cell(cell: tuple, matrix: list) -> bool:
    return min(cell) >=0 and max(cell) < len(matrix)


def get_cell(cell: tuple, matrix: list) -> str:
    row, col = cell
    return str(matrix[row][col])


def set_cell(cell: tuple, matrix: list, value: str) -> None:
    row, col = cell
    matrix[row][col] = value


def main() -> None:
    initial_string = input()
    matrix = [[el for el in input()] for _ in range(int(input()))]
    P_cell = next(((x, y ) for x in range(len(matrix)) for y in range(len(matrix)) if get_cell((x, y), matrix) == 'P'))

    for _ in range(int(input())):
        direction = input()
        new_cell = move[direction](P_cell)
        
        if is_valid_cell(new_cell, matrix):
            letter = get_cell(new_cell, matrix)
            set_cell(P_cell, matrix, '-')
            set_cell(new_cell, matrix, 'P')
            P_cell = new_cell
            if letter != '-':
                initial_string += letter

        elif len(initial_string) > 0:
            initial_string = initial_string[:-1]

    print (initial_string)
    for row in matrix:
        print(*row, sep='')

if __name__ == '__main__':
    main()