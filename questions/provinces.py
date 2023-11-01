"""
Problem: Number of Provinces

Description:
Given an n x n matrix isConnected where each value isConnected[i][j] indicates if the ith city and the jth city are directly connected, determine the total number of provinces. A province is a group of cities that are directly or indirectly connected, with no other cities outside the group.

Function Signature:
def findCircleNum(isConnected: List[List[int]]) -> int:

Inputs:
    - isConnected (List[List[int]]): An n x n matrix representing connections between cities.

Returns:
    - int: The total number of provinces.

Examples:
1. Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
   Output: 2
   Explanation: There are two provinces, one for the first two cities and one for the third.

2. Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
   Output: 3
   Explanation: Each city is its own province since they're not connected.

Constraints:
    - 1 <= n <= 200
    - n == isConnected.length
    - n == isConnected[i].length
    - isConnected[i][j] is either 1 or 0.
    - isConnected[i][i] == 1
    - isConnected[i][j] == isConnected[j][i]

Notes:
    - A Depth First Search (DFS) or Union-Find can be used to identify connected cities and group them into provinces.
    - If two cities are directly connected, they belong to the same province.
    - If two cities are indirectly connected, they also belong to the same province.

Tags:
    - Graph
    - Depth First Search
    - Union-Find
"""

from typing import List

def findCircleNum(isConnected: List[List[int]]) -> int:
    def dfs(city):
        for next_city in range(n):
            # If the next city is connected and has not been visited
            if isConnected[city][next_city] == 1 and not visited[next_city]:
                visited[next_city] = True
                dfs(next_city)
                
    n = len(isConnected)
    visited = [False] * n
    provinces = 0
    
    for city in range(n):
        # If the city has not been visited, start DFS from it
        if not visited[city]:
            provinces += 1
            visited[city] = True
            dfs(city)
            
    return provinces
