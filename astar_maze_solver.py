# ipt132-informed.py
# Informed search: A*

import heapq

WALL = 'O'
MARK = '*'
MAZE_FILE = "maze.txt"

def read_maze(file_path: str):
    """
    Read maze from a text file and return it as a 2D list.
    """

    with open(file_path,"r",encoding="utf-8") as f :
        lines = f.read().splitlines() 

    if not lines:
        raise ValueError("Empty maze file.")
    
    maze = [list(line) for line in lines]  
    return maze

def in_bounds(row,col,rows,cols):
    """
    Check whether (row, col) is inside the maze boundaries.
    """
    return 0 <= row < rows and 0 <= col < cols


def is_passable(maze,row,col):
    """
    Return True if the cell is not a wall ('O').
    """
    return maze[row][col] != WALL


def neighbors(row,col):
    """
    Return four adjacent positions (up, down, left, right).
    Diagonal moves are not allowed.
    """
 
    return [
        (row - 1, col),
        (row + 1, col),
        (row, col - 1),
        (row, col + 1)
    ]

def find_start_goal_point(maze):
    """
    Start: first open cell on bottom row from right to left.
    Goal:  first open cell on top row from left to right.
    """
    rows, cols = len(maze),len(maze[0]) # Get the number of rows and columns in the maze
    
    # Find the start point:
    # Search the bottom row from right to left
    start = None
    for col in range(cols-1, -1, -1): 
        if is_passable(maze, rows-1, col):
            start = (rows-1, col)
            break

    # Find the goal point:
    # Search the top row from left to right
    goal = None
    for col in range(cols):
        if is_passable(maze, 0, col):
            goal = (0,col)
            break
    return start, goal

def backtrack_path(parent, start, goal):
    """
    Rebuild the path from the start to the goal using parent pointers. 
    It returns a list of coordinates if a valid path exists; otherwise, it returns None.
    """
    current = goal
    path = []

    while current is not None:
        path.append(current)
        current = parent.get(current)
    path.reverse()
    if path and path[0] == start:
        return path
    return None

def manhattan(a, b):
    """
    Manhattan distance heuristic for grid moves.
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    """
    Use A* search to find the optimal (shortest) path.
    Returns (path, cost) if found, otherwise (None, None).
    """
    rows, cols = len(maze), len(maze[0])

    # Priority queue items: (f, seq, node)
    open_heap = []
    seq = 0

    g = {start: 0}
    parent = {start: None}

    f0 = manhattan(start, goal)
    heapq.heappush(open_heap, (f0, seq, start))

    visited = set()

    while open_heap:
        _, _, current = heapq.heappop(open_heap)

        if current == goal:
            return backtrack_path(parent, start, goal), g[goal]

        if current in visited:
            continue
        visited.add(current)

        for nxt in neighbors(*current):
            if not in_bounds(*nxt, rows, cols) or not is_passable(maze, *nxt) or (nxt in visited):
                continue

            temp_g = g[current] + 1
            
            if temp_g < g.get(nxt, float("inf")):
                parent[nxt] = current
                g[nxt] = temp_g
                seq += 1
                f = temp_g + manhattan(nxt, goal)
                heapq.heappush(open_heap, (f, seq, nxt))

    return None, None

def mark_path_on_maze(maze, path):

    out = [line[:] for line in maze]
    for (row, col) in path:
        out[row][col] = MARK
    return out

def print_maze(maze):
    for line in maze:
        print(''.join(line))

def main():

    try:
        maze = read_maze(MAZE_FILE)
    except Exception:
        print("No solution found")
        return

    start, goal = find_start_goal_point(maze)
    if start is None or goal is None:
        print("No solution found")
        return

    if not is_passable(maze, *start) or not is_passable(maze, *goal):
        print("No solution found")
        return

    path, cost = astar(maze, start, goal)
    if path is None:
        print("No solution found")
        return

    solved = mark_path_on_maze(maze, path)
    print_maze(solved)

    print(f"Path cost: {cost}")

if __name__ == "__main__":
    main()

