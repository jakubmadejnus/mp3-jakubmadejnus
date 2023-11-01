"""
Problem: Task Scheduling with Prerequisites

Description:
Given a number of tasks and a list of prerequisite pairs, determine if it is possible to schedule all the tasks in a manner that fulfills all prerequisite requirements. Each task is labeled from 0 to N-1 and might have some other tasks that need to be completed before it can be scheduled.

Function Signature:
def can_schedule_tasks(tasks: int, prerequisites: List[List[int]]) -> bool:

Inputs:
    - tasks (int): The total number of tasks.
    - prerequisites (List[List[int]]): A list of pairs, where the first task in the pair is a prerequisite for the second task.

Returns:
    - bool: True if it's possible to schedule all tasks without any conflicts, False otherwise.

Examples:
1. Input: tasks=3, prerequisites=[[0, 1], [1, 2]]
   Output: True
   Explanation: Task '0' should be completed before '1' and task '1' before '2'. One possible order is: [0, 1, 2].

2. Input: tasks=3, prerequisites=[[0, 1], [1, 2], [2, 0]]
   Output: False
   Explanation: The tasks have a cyclic dependency which makes them impossible to be scheduled.

3. Input: tasks=6, prerequisites=[[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]
   Output: True
   Explanation: The tasks can be scheduled in various orders, one of them is: [0, 1, 4, 3, 2, 5].

Notes:
    - The problem can be visualized as a directed graph where tasks are nodes and prerequisites are directed edges. The problem then translates to detecting a cycle in the graph.
    - Depth-first search (DFS) can be employed to detect the cycle.

Tags:
    - Graphs
    - Topological Sorting
    - Depth-First Search
"""

from typing import List
from collections import defaultdict

def can_schedule_tasks(tasks: int, prerequisites: List[List[int]]) -> bool:
    # Build the graph
    graph = defaultdict(list)
    for pre, task in prerequisites:
        graph[pre].append(task)
    
    # Helper function to perform DFS
    def dfs(node, visited, rec_stack):
        visited[node] = True
        rec_stack[node] = True
        
        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor, visited, rec_stack):
                    return True
            elif rec_stack[neighbor]:
                # Cycle detected
                return True
            
        # Remove the node from the recursion stack as we leave the recursion
        rec_stack[node] = False
        return False
    
    # Initialize visited and recursion stack arrays
    visited = [False] * tasks
    rec_stack = [False] * tasks
    
    # Perform DFS to detect cycle
    for i in range(tasks):
        if not visited[i]:
            if dfs(i, visited, rec_stack):
                return False
    
    # No cycle detected
    return True