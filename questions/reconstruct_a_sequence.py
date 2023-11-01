"""
Problem: Unique Reconstruction of Sequence

Description:
Given an original sequence 'originalSeq' and a list of sequences 'seqs', we need to determine whether 'originalSeq' can be uniquely reconstructed from 'seqs'. A unique reconstruction means that 'originalSeq' is the only sequence such that all sequences in 'seqs' are subsequences of it.

Function Signature:
def can_construct(originalSeq: List[int], seqs: List[List[int]]) -> bool:

Inputs:
    - originalSeq (List[int]): The main sequence which we want to check if it can be uniquely reconstructed.
    - seqs (List[List[int]]): A list of sequences.

Returns:
    - bool: True if 'originalSeq' can be uniquely reconstructed from 'seqs', otherwise False.

Examples:
1. Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
   Output: True
   Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct   
   [1, 2, 3, 4], implying that all the given sequences define the unique order of numbers in 'originalSeq'.

2. Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
   Output: False
   Explanation: Sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct [1, 2, 3, 4]. 
   There are two possible sequences derived from the given sequences: [1, 2, 3, 4] and [1, 2, 4, 3].

3. Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
   Output: True
   Explanation: Sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct [3, 1, 4, 2, 5].

Notes:
    - This problem can be approached by leveraging the topological sort. We can consider each number as a unique node and draw directed edges from each sequence in 'seqs'.
    - If the resulting topological order is unique and matches the 'originalSeq', then the sequence can be uniquely reconstructed.

Tags:
    - Graphs
    - Topological Sorting
"""
from typing import List
from collections import deque

def can_construct(originalSeq: List[int], seqs: List[List[int]]) -> bool:
    # Initialize the graph and in-degree array
    graph = {}
    in_degree = {}
    
    # Build the graph based on sequences
    for seq in seqs:
        for num in seq:
            if num not in graph:
                graph[num] = []
                in_degree[num] = 0
            
    # Add edges to the graph and update in-degree array
    for seq in seqs:
        for i in range(1, len(seq)):
            parent, child = seq[i-1], seq[i]
            graph[parent].append(child)
            in_degree[child] += 1
    
    # Ensure all numbers in the original sequence are in the graph
    if len(originalSeq) != len(in_degree):
        return False
    
    # Topological sort
    sources = deque()
    for node in in_degree:
        if in_degree[node] == 0:
            sources.append(node)
    
    sorted_order = []
    while sources:
        if len(sources) > 1:
            # More than one source means that there are multiple ways to reconstruct the sequence
            return False
        
        node = sources.popleft()
        sorted_order.append(node)
        
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)
                
    return sorted_order == originalSeq
