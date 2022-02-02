# 1. Build the maze & get Kate's position
# 2. Ping the maze (measure moves from Kate position to every cell in the maze that Kate can reach)
# 3. Check if the ping reached the perimeter (found an exit). If not - Kate is stuck.
# 4. Block all exits that were not reached by Kate
# 5. Loop through all reachable exit and ping the maze (measure moves from exit to every cell in the maze)
# 6. Store the maximum moves for that exit ping to reach Kate
# 7. Print the maximum for all moves



# Some useful stuff
maze = []
free_blocks = 0
kate_row = 0
kate_column = 0
max_route_list = []

def ping_the_maze(ripples):
    for i in range(ripples + 1):
        for x in range(len(maze)):
            for y in range(len(maze[0])):
                if maze[x][y] == i:
                    if 0 < x:
                        if maze[x - 1][y] == ' ':
                            maze[x - 1][y] = i + 1
                    if x < len(maze) - 1:
                        if maze[x + 1][y] == ' ':
                            maze[x + 1][y] = i + 1
                    if 0 < y:
                        if maze[x][y - 1] == ' ':
                            maze[x][y -1] = i + 1
                    if y < len(maze[0]) - 1:
                        if maze[x][y + 1] == ' ':
                            maze[x][y + 1] = i + 1


# Start here - build the maze
maze_rows = int(input())
input_data = [input() for _ in range(maze_rows)]
maze_cols = max([len(x) for x in input_data])    
input_data = [x if len(x) == maze_cols else x + ' ' * (maze_cols - len(x)) for x in input_data]

for i in range(maze_rows):
    maze_row = [x for x in input_data[i]]
    maze.append(maze_row)
    if 'k' in maze_row:
        index = maze_row.index('k')
        maze_row[index] = 0
        kate_column = index
        kate_row  = i
    free_blocks += maze_row.count(' ')

maze_edges = [(0, x) for x in range(maze_cols)]
maze_edges.extend([(maze_rows - 1, x) for x in range(maze_cols)])
maze_edges.extend([(x,0) for x in range(1,maze_rows - 1)])
maze_edges.extend([(x,maze_cols - 1) for x in range(1,maze_rows - 1)])

kate_adjacent_cells = []
for i in range(maze_rows):
    for j in range(maze_cols):
        if i == kate_row and (j == kate_column - 1 or j == kate_column + 1):
            kate_adjacent_cells.append((i,j))
        elif j == kate_column and (i == kate_row - 1 or i == kate_row + 1):
            kate_adjacent_cells.append((i,j))

# Ping the maze
ping_the_maze(free_blocks)

# Find minumum number of moves to all reachable exits
edges_reached = [(x,y) for x, y in maze_edges if str(maze[x][y]).isnumeric()]

# Check if Kat can get out
if not edges_reached:
    print('Kate cannot get out')

else: 
    # For each reachable exit: clear the maze and ping towards Kate
    maze[kate_row][kate_column] = 'k'
    for edge in edges_reached:    
    
        for i in range(maze_rows):
            for j in range(maze_cols):
                if str(maze[i][j]).isnumeric():
                    maze[i][j] = ' '
        
        maze[edge[0]][edge[1]] = 0
        ping_the_maze(free_blocks)

        max_route = max([maze[x][y] + 2 for x, y in kate_adjacent_cells if str(maze[x][y]).isnumeric()])
        max_route_list.append(max_route)

    print(f'Kate got out in {max(max_route_list)} moves')