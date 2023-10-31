"""
Problem: Find the Town Judge

Description:
In a town with n people, labeled from 1 to n, there is a rumor of a hidden town judge. The town judge has the following characteristics:
    1. The town judge trusts nobody.
    2. Everybody, except the town judge, trusts the town judge.
    3. Only one person satisfies both properties 1 and 2.
You are provided an array named "trust", where each element is a pair [a, b] indicating that person 'a' trusts person 'b'. If a trust relationship isn't in the "trust" array, then it doesn't exist. Determine the identity of the town judge.

Function Signature:
def findJudge(n: int, trust: List[List[int]]) -> int:

Inputs:
    - n (int): The number of people in the town.
    - trust (List[List[int]]): A 2D array where each element [a, b] represents that person 'a' trusts person 'b'.

Returns:
    - int: The label of the town judge if they exist and can be identified, or -1 if not.

Examples:
1. Input: n = 2, trust = [[1,2]]
   Output: 2

2. Input: n = 3, trust = [[1,3],[2,3]]
   Output: 3

3. Input: n = 3, trust = [[1,3],[2,3],[3,1]]
   Output: -1

Notes:
    - Use an array or a dictionary to keep track of the trust count for each person.
    - Iterate through the trust array to update trust counts.
    - Find the person who is trusted by everyone but doesn't trust anyone.

Tags:
    - Array
    - Graph
"""
from typing import List

def findJudge(n: int, trust: List[List[int]]) -> int:
  return -1