![Python](https://img.shields.io/badge/Python-3.12-blue)
![Algorithm](https://img.shields.io/badge/Algorithm-Search-orange)
![AI](https://img.shields.io/badge/AI-Pathfinding-green)
![BFS](https://img.shields.io/badge/Search-BFS-blueviolet)
![A*](https://img.shields.io/badge/Search-A*-red)
# Maze Search Algorithms

This project implements two fundamental AI search algorithms — **Breadth-First Search (BFS)** and **A\*** — to solve a maze pathfinding problem and compare uninformed vs informed search strategies.

---

## Overview
The program finds a path in a maze from the **bottom-right corner (start)** to the **top-left corner (goal)** using two different search methods.  
Both algorithms successfully found the **optimal path** with a total cost of **76**.

---

## Algorithms
- **BFS (Uninformed Search)** — explores nodes level by level without heuristic guidance
- **A\* (Informed Search)** — uses a heuristic to guide search toward the goal

---

## Maze Rules
- Start position: bottom-right
- Goal position: top-left
- Allowed moves: up, down, left, right
- Diagonal movement: not allowed
- Step cost: uniform cost of **1 per move**

---

## Result
Both BFS and A\* found the same optimal path with identical total cost:

```
Total Cost: 76
```

---

## Environment
Developed using:

```
Python 3.12
```

---

## How to Run
```bash
python bfs_maze_solver.py
python astar_maze_solver.py
```

---

## Learning Purpose
This project demonstrates:
- Difference between uninformed and informed search
- How heuristics influence search efficiency
- Optimal pathfinding in grid environments

---

## Author
**Jinhee Kim**  
M.S. Artificial Intelligence Student
