"""
Problem: Distinct Islands

Description:
Given an m x n binary matrix grid where 1 represents land and 0 represents water, find the number of distinct islands. An island is a group of 1's connected 4-directionally (horizontal or vertical). Two islands are considered distinct if one cannot be translated (i.e., moved without rotation or reflection) to match the other. The grid is surrounded by water on all four sides.

Function Signature:
def num_distinct_islands(grid: List[List[int]]) -> int:

Inputs:
    - grid (List[List[int]]): A 2D matrix representing the map where 1 is land and 0 is water.

Returns:
    - int: The number of distinct islands in the grid.

Examples:
1. Input: grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
   Output: 1

2. Input: grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
   Output: 3

Notes:
    - A Depth-First Search (DFS) can be employed to traverse each island and record its shape.
    - The shape can be determined based on the sequence of moves made during the DFS.
    - To ensure distinct islands, we can use a set to store the shapes.

Tags:
    - Matrix
    - DFS
    - Graph
"""
from typing import List, Set

def num_distinct_islands(grid: List[List[int]]) -> int:
    if not grid:
        return 0
    
    m, n = len(grid), len(grid[0])
    distinct_islands = set()
    
    def dfs(r, c, path):
        if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
            grid[r][c] = 0
            
            path.append((r, c))
            dfs(r + 1, c, path)
            dfs(r - 1, c, path)
            dfs(r, c + 1, path)
            dfs(r, c - 1, path)

    for r in range(m):
        for c in range(n):
            if grid[r][c] == 1:
                path = []
                dfs(r, c, path)
                                
                if path:
                    min_r = min(pt[0] for pt in path)
                    min_c = min(pt[1] for pt in path)
                    distinct_islands.add(tuple((x - min_r, y - min_c) for x, y in path))
    
    return len(distinct_islands)