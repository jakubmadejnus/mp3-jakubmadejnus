"""
Problem: Bipartite Graph

Description:
Given an undirected graph represented by a 2D array where graph[u] lists nodes adjacent to node u, determine if the graph is bipartite. A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

Function Signature:
def isBipartite(graph: List[List[int]]) -> bool:

Inputs:
    - graph (List[List[int]]): A 2D array representing connections between nodes.

Returns:
    - bool: True if the graph is bipartite, otherwise False.

Examples:
1. Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
   Output: false
   Explanation: There is no possible partition that satisfies the bipartite conditions.

2. Input: graph = [[1,3],[0,2],[1,3],[0,2]]
   Output: true
   Explanation: The graph can be partitioned into two sets: {0, 2} and {1, 3}.

Constraints:
    - graph.length == n
    - 1 <= n <= 100
    - 0 <= graph[u].length < n
    - 0 <= graph[u][i] <= n - 1
    - graph[u] does not contain u.
    - All values in graph[u] are unique.
    - If graph[u] contains v, then graph[v] contains u.

Notes:
    - A Depth First Search (DFS) or Breadth First Search (BFS) can be employed to traverse through the graph and check if it's bipartite.
    - A coloring approach can be used, where adjacent nodes must have different colors.
    - If during traversal we find two adjacent nodes with the same color, the graph is not bipartite.

Tags:
    - Graph
    - Depth First Search
    - Breadth First Search
"""

from typing import List
from collections import deque

def isBipartite(graph: List[List[int]]) -> bool:
    n = len(graph)
    color = [-1] * n  # -1: uncolored, 0: color A, 1: color B
    
    for i in range(n):
        # If the node is uncolored and the BFS coloring leads to a contradiction, return False
        if color[i] == -1 and not bfs_coloring(graph, color, i):
            return False
    
    return True

def bfs_coloring(graph: List[List[int]], color: List[int], start: int) -> bool:
    queue = deque([start])
    color[start] = 0  # Start with color A
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            # If the neighbor is uncolored, color it with the opposite color and add it to the queue
            if color[neighbor] == -1:
                color[neighbor] = 1 - color[node]
                queue.append(neighbor)
            # If the neighbor has the same color, the graph is not bipartite
            elif color[neighbor] == color[node]:
                return False
    
    return True
