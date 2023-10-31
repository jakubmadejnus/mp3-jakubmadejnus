import pytest
from typing import List

from questions.provinces import findCircleNum

@pytest.mark.parametrize(
    "isConnected,expected",
    [
        # Basic test cases from the problem's description
        ([[1,1,0],[1,1,0],[0,0,1]], 2),
        ([[1,0,0],[0,1,0],[0,0,1]], 3),
        
        # Edge Cases
        # Smallest input possible, one city
        ([[1]], 1),
        
        # Larger input with multiple connected components
        ([[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]], 2),
        
        # All cities are connected
        ([[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], 1),
        
        # No cities are connected, each city is its own province
        ([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], 4),
        
        # Complex connection matrix
        ([[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,0,1,0,1]], 2),
        
        # Diagonal cities connected, should be individual provinces
        ([[1,0,0,1],[0,1,1,0],[0,1,1,0],[1,0,0,1]], 2),
        
        # Alternate cities connected
        ([[1,1,0,1],[1,1,1,0],[0,1,1,0],[1,0,0,1]], 1),
        
        # Larger input to test efficiency
        ([[1,0,1] * 100] * 300, 101),
        
        # Cities in a chain but not forming a cycle
        ([[1,1,0,0,0],[1,1,1,0,0],[0,1,1,1,0],[0,0,1,1,1],[0,0,0,1,1]], 1),
        
        # Cities forming multiple chains
        ([[1,1,0,0,0,0,0],[1,1,0,0,0,0,0],[0,0,1,1,0,0,0],[0,0,1,1,0,0,0],[0,0,0,0,1,1,0],[0,0,0,0,1,1,1],[0,0,0,0,0,1,1]], 3)
    ]
)
def test_findCircleNum(isConnected: List[List[int]], expected: int):
    assert findCircleNum(isConnected) == expected
