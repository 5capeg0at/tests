import random

def generate_maze(rows, cols):
    maze = [["#" for j in range(cols)] for i in range(rows)]
    visited = [[False for j in range(cols)] for i in range(rows)]
    stack = [(0,0)]

    while stack:
        curr_row, curr_col = stack.pop()
        visited[curr_row][curr_col] = True
        neighbors = [(curr_row-2, curr_col), (curr_row, curr_col+2), (curr_row+2, curr_col), (curr_row, curr_col-2)]
        random.shuffle(neighbors)

        for n_row, n_col in neighbors:
            if n_row >= 0 and n_row < rows and n_col >= 0 and n_col < cols and not visited[n_row][n_col]:
                if n_row == curr_row-2:
                    maze[n_row+1][curr_col] = " "
                elif n_col == curr_col+2:
                    maze[curr_row][n_col-1] = " "
                elif n_row == curr_row+2:
                    maze[n_row-1][curr_col] = " "
                else:
                    maze[curr_row][n_col+1] = " "
                stack.append((n_row, n_col))

    maze[0][1] = " "
    maze[rows-1][cols-2] = " "
    return maze

def solve_maze(maze, start, end):
    stack = [(start[0], start[1], "")]
    visited = set()

    while stack:
        curr_row, curr_col, path = stack.pop()
        if curr_row == end[0] and curr_col == end[1]:
            return path

        if (curr_row, curr_col) in visited:
            continue
        visited.add((curr_row, curr_col))

        if curr_row > 0 and maze[curr_row-1][curr_col] == " ":
            stack.append((curr_row-2, curr_col, path+"U"))
        if curr_col < len(maze[0])-1 and maze[curr_row][curr_col+1] == " ":
            stack.append((curr_row, curr_col+2, path+"R"))
        if curr_row < len(maze)-1 and maze[curr_row+1][curr_col] == " ":
            stack.append((curr_row+2, curr_col, path+"D"))
        if curr_col > 0 and maze[curr_row][curr_col-1] == " ":
            stack.append((curr_row, curr_col-2, path+"L"))

    return "No path found"

maze = generate_maze(15, 15)
print("Generated Maze:")
for row in maze:
    print("".join(row))

print("Solving Maze...")
path = solve_maze(maze, (0,1), (len(maze)-1, len(maze[0])-2))
print("Path: " + path)
