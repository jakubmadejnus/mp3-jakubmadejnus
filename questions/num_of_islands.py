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
from typing import List

def num_distinct_islands(grid: List[List[int]]) -> int:
  return 0