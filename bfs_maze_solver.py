# Uninformed search: BFS
from collections import deque
import sys

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

def bfs(maze, start, goal):
    """
    Use Breadth-First Search to find a path from the start to the goal. 
    Return the path if it is found; otherwise, return None.
    """
    rows, cols = len(maze), len(maze[0])
    q = deque([start]) # FIFO
    parent = {start: None}
    visited = set([start])

    while q: 
        current = q.popleft()
        if current == goal: 
            return backtrack_path(parent, start, goal)

        row, col = current # unpack (row, col) tuple
        
        for next_row, next_col in neighbors(row, col):
            if in_bounds(next_row, next_col, rows, cols) and (next_row, next_col) not in visited and is_passable(maze, next_row, next_col):
                visited.add((next_row, next_col))
                parent[(next_row, next_col)] = current
                q.append((next_row, next_col))

    return None

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

    path = bfs(maze, start, goal)
    if path is None:
        print("No solution found")
        return

    solved = mark_path_on_maze(maze, path)
    print_maze(solved)

    # cost = len(path) - 1
    # print(f"Path cost: {cost}")

if __name__ == "__main__":

    main()
