"""
Problem: Course Schedule

Description:
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. Each course has prerequisites that must be completed before it can be taken. Determine if it's possible for you to finish all the courses given these prerequisites.

Function Signature:
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:

Inputs:
    - numCourses (int): The total number of courses.
    - prerequisites (List[List[int]]): A list of course pairs, where for each pair [a, b], course b needs to be finished before course a.

Returns:
    - bool: True if it's possible to finish all courses, False otherwise.

Examples:
1. Input: numCourses = 2, prerequisites = [[1,0]]
   Output: true
   Explanation: 
   There are a total of 2 courses to take. 
   To take course 1 you should have finished course 0. So it is possible.

2. Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
   Output: false
   Explanation: 
   There are a total of 2 courses to take. 
   To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
    - 1 <= numCourses <= 2000
    - 0 <= prerequisites.length <= 5000
    - 0 <= ai, bi < numCourses for each pair [ai, bi] in prerequisites.
    - All the pairs in prerequisites are unique.

Notes:
    - This problem can be thought of as determining if a cycle exists in a directed graph.
    - A Depth First Search (DFS) can be used to detect a cycle in the course schedule.
    - A node (or course) is considered visited once it has been marked in the DFS process. If a visited course is encountered again, then a cycle exists.

Tags:
    - Graph
    - Depth First Search
    - Cycle Detection

"""
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Construct the adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)
    
    # States: 0 = unvisited, 1 = visiting, 2 = visited
    states = [0] * numCourses
    
    def hasCycle(node):
        if states[node] == 1:
            return True
        if states[node] == 2:
            return False
        
        states[node] = 1
        
        for neighbor in graph[node]:
            if hasCycle(neighbor):
                return True
        
        states[node] = 2
        return False
    
    for i in range(numCourses):
        if hasCycle(i):
            return False
    
    return True