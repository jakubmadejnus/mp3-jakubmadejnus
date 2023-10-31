"""
Problem: Minimum Height Trees

Description:
Given an undirected graph that resembles a k-ary tree, we need to determine which node(s), when chosen as the root, will result in a tree of minimum height. Such a tree is called a Minimum Height Tree (MHT). It is possible to have multiple MHTs for a graph. The goal is to find and return a list of roots that give MHTs.

Function Signature:
def find_mht_roots(vertices: int, edges: List[List[int]]) -> List[int]:

Inputs:
    - vertices (int): The number of vertices in the graph.
    - edges (List[List[int]]): A list of edge pairs representing the undirected edges of the graph.

Returns:
    - List[int]: A list containing the root(s) that give MHTs.

Examples:
1. Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
   Output: [1, 2]
   Explanation: Using '1' or '2' as roots results in MHTs. The height of the trees with roots '1' or '2' is three, which is the minimum.

2. Input: vertices: 4, Edges: [[0, 1], [0, 2], [2, 3]]
   Output: [0, 2]
   Explanation: Using '0' or '2' as roots results in MHTs. The height of the trees with roots '0' or '2' is three, which is the minimum.

3. Input: vertices: 4, Edges: [[0, 1], [1, 2], [1, 3]]
   Output: [1]

Notes:
    - The problem can be approached by progressively peeling layers of the graph from the outside, similar to the logic behind topological sort. By removing the outermost leaves, we inch closer to the center of the graph which will give us the MHT.
    - The last remaining one or two nodes will be our answer.

Tags:
    - Graph
    - BFS
"""
from typing import List

def find_mht_roots(vertices: int, edges: List[List[int]]) -> List[int]:
  return []