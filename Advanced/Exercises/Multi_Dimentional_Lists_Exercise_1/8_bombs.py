matrix = []

def explode(cell:tuple) -> None:
    global matrix

    x, y = cell
    if matrix[x][y] > 0:
        for row in range(x-1, x + 2):
            for col in range(y - 1, y + 2):
                if min(row, col) >= 0 \
                    and row < len(matrix) \
                    and col < len(matrix[0]) \
                    and not (row == x and col == y) \
                    and matrix[row][col] > 0:
                    matrix[row][col] -= matrix[x][y]
        matrix[x][y] = 0


matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
cells = [tuple(int(y) for y in x.split(',')) for x in input().split()]


for cell in cells:
    explode(cell)

alive = sum([1 for row in matrix for el in row if el > 0])
sum_alive = sum([el for row in matrix for el in row if el > 0])

print(f"Alive cells: {alive}")
print(f"Sum: {sum_alive}")
for row in matrix:
    print(' '.join([str(x) for x in row]))