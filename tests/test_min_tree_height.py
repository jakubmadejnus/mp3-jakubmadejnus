import pytest
from typing import List

from questions.min_tree_height import find_mht_roots

# Test cases for the function
@pytest.mark.parametrize(
    "vertices, edges, expected",
    [
        # Test case 1
        (5, [[0, 1], [1, 2], [1, 3], [2, 4]], [1, 2]),

        # Test case 2
        (4, [[0, 1], [0, 2], [2, 3]], [0, 2]),

        # Test case 3
        (4, [[0, 1], [1, 2], [1, 3]], [1]),

        # Test case 4: Single node
        (1, [], [0]),

        # Test case 5: Two nodes
        (2, [[0, 1]], [0, 1]),

        # Test case 6: Larger straight line tree
        (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], [2, 3]),

        # Test case 7: Larger tree with multiple MHT roots
        (7, [[0, 1], [0, 2], [1, 3], [1, 4], [4, 5], [4, 6]], [1]),

        # Test case 8: Large star shaped tree (to test efficiency)
        (1001, [[0, i] for i in range(1, 1001)], [0]),
        
        # Test case 9: Larger balanced tree
        (15, [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14]], [0]),
    ]
)
def test_find_mht_roots(vertices: int, edges: List[List[int]], expected: List[int]):
    assert sorted(find_mht_roots(vertices, edges)) == sorted(expected)
