# Kate is stuck in a maze. You should help her to find her way out.
# On the first line, you will be given how many rows there are in the maze. On the following n lines, you will be given the maze itself. Here is a legend for the maze:
# •	"#" - means a wall; Kate cannot go through there
# •	" " - means empty space; Kate can go through there
# •	"k" - the initial position of Kate; start looking for a way out from there
# There are two options: Kate either gets out or not:
# •	If Kate can get out, print the following: 
# "Kate got out in {number_of_moves} moves". 
# Note: If there are two or more ways out, she always chooses the longest one.
# •	Otherwise, print: "Kate cannot get out".


# Gather the input data
maze = []
paths_list = []
temp_paths_list = []

mz_rows = int(input())
input_data = [input() for _ in range(mz_rows)]

# Address the issue maze rows are of different lenght (e.g. if spaces on the right are missing)
mz_cols = max([len(data) for data in input_data])
input_data = [data if len(data) == mz_cols else data + ' ' * (mz_cols - len(data)) for data in input_data]

# Fill the maze
for i in range(mz_rows):
    maze_row = [data for data in input_data[i]]
    maze.append(maze_row)

# Set Kate's position as the start of all paths
temp_paths_list.append([(row,col) for row in range(mz_rows) for col in range(mz_cols) if maze[row][col] == 'k'])

# Generate all possible paths originating from Kate's position
while True:
    if not temp_paths_list:
        break

    for path in temp_paths_list:
        row, col  = path[-1]

        temp_branches = []
        if row > 0:
            if maze[row - 1][col] == ' ' and (row - 1, col) not in path:
                temp_branches.append((row - 1, col))
        if row < mz_rows - 1:
            if maze[row + 1][col] == ' ' and (row + 1, col) not in path:
                temp_branches.append((row + 1, col))
        if col > 0:
            if maze[row][col - 1] == ' ' and (row, col - 1) not in path:
                temp_branches.append((row, col - 1))
        if col < mz_cols - 1:
            if maze[row][col + 1] == ' ' and (row, col + 1) not in path:
                temp_branches.append((row, col + 1))

        if not temp_branches:
            paths_list.append(path)
            temp_paths_list.remove(path)
            break
        else:
            for branch in temp_branches:
                temp_path = path.copy()
                temp_path.append(branch)
                temp_paths_list.append(temp_path)
            temp_paths_list.remove(path)
            break

# Keep only the patsh exiting the maze
paths_to_keep = []
for path in paths_list:
    row, col  = path[-1]
    if row in (0, mz_rows - 1) or col in (0, mz_cols - 1):
        paths_to_keep.append(path)

# Print out the outcome
if paths_to_keep:
    max_moves = max([len(path) for path in paths_to_keep])
    print(f'Kate got out in {max_moves} moves')
else:
    print('Kate cannot get out')