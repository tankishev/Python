# You will be given a number n representing the number of rows of the field. On the following n lines, 
# you will receive each field row as a string with numbers separated by a space. 
# Each number greater than zero represents a ship with health equal to the number value. 
# After that, you will receive the squares that are being attacked in the format: "{row}-{col} {row}-{col}". 
# Each time a square is being attacked, if there is a ship (number greater than 0), you should reduce its value by 1. 
# If a ship's health reaches zero, it is destroyed. After the attacks have ended, print how many ships were destroyed.


game_board = [[int(x) for x in input().split(' ')] for _ in range(int(input()))]
attacks = [(int(x[0]), int(x[2])) for x in input().split(' ')]

kills = 0
for attack in attacks:
    row, col =  attack
    if 0 <= row < len(game_board) and 0 <= col < len(game_board[0]):
        game_board[row][col] -= 1
        if game_board[row][col] == 0:
            kills += 1

print (kills)