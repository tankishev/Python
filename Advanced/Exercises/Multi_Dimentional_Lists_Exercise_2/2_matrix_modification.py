
modify = {
    'Add': lambda x: x,
    'Subtract': lambda x: -x
}

matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

while True:
    input_line = input()
    if input_line == 'END': 
        break
    
    tokens = input_line.split()
    command = tokens[0]
    row, col, value = [int(x) for x in tokens[1:]]
    if min(row, col) < 0 or max(row, col) >= len(matrix):
        print('Invalid coordinates')
    else:
        matrix[row][col] += modify[command](value)

for row in matrix:
    print(' '.join([str(x) for x in row]))