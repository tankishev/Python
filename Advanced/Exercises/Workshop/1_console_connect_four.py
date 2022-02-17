series = {
    'row': lambda cell: tuple(board[cell[0]][col] for col in range(cell[1],min(7,cell[1]+4))),
    'col': lambda cell: tuple(board[row][cell[1]] for row in range(cell[0],min(6,cell[0]+4))),
    'primary_diagonal': lambda cell: tuple(board[cell[0]+i][cell[1]+i] for i in (0,1,2,3) if cell[0]+i < 6 and cell[1]+i < 7),
    'secondary_diagonal': lambda cell: tuple(board[cell[0]+i][cell[1]-i] for i in (0,1,2,3) if cell[0]+i < 6 and cell[1]-i >= 0),
}


def play_move(player):
    global board

    while True:
        column = input(f'Player {player}, please choose a column (1-7): ')
        if column.isnumeric():
            column  = int(column)
            if 0 < column < 8 and board[0][column-1] == ' ':
                break
        else:
            print('Invalid choice.')  

    for row in range(5,-1,-1):
        if board[row][column-1] == ' ':
            break    

    board[row][column-1] = player


def won_game(player):
    for row in range(6):
        for col in range(7):
            if board[row][col] == player:
                for key in series.keys():
                    test_tuple = series[key]((row,col))
                    if test_tuple:
                        if test_tuple.count(player) == 4:
                            return True
    return False


def print_board():
    print('\n')
    for row in board:
        print('|', ' | '.join([str(el) for el in row]), '|')
    print('-'*29)
    print('\n')



board = [[' ']*7 for _ in range(6)]
play_id, next_id = 1, 2
print("Let's start!\n")
print_board()

while True:  
    play_move(play_id)
    print_board()
    
    if won_game(play_id):
        print(f'The winner is player {play_id}!')
        break
    
    play_id, next_id = next_id, play_id