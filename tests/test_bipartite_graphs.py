import pytest
from typing import List
from questions.bipartite_graphs import isBipartite

@pytest.mark.parametrize(
    "graph, expected",
    [
        # Test case from prompt
        ([[1,2,3],[0,2],[0,1,3],[0,2]], False),
        ([[1,3],[0,2],[1,3],[0,2]], True),

        # Node 0 is not connected to any other node, so it's always bipartite
        ([[1],[]], True),

        # A triangle graph (not bipartite)
        ([[1,2],[0,2],[0,1]], False),

        # Square graph (bipartite)
        ([[1],[0,2],[1,3],[2]], True),

        # Large disconnected components, where each component is a bipartite graph
        ([[1],[0,2,3],[1,3],[1,2,4,5],[3,5],[3,4,6,7],[5,7],[5,6]], False),

        # Large graph where all nodes are connected in a linear fashion (bipartite)
        ([[i - 1, i + 1] for i in range(1, 9999)] + [[9998], [9999]], False),

        # Large complete graph (not bipartite)
        ([list(range(1000)) for _ in range(1000)], False),

        # Star graph (bipartite)
        ([[i for i in range(1, 1000)]] + [[0] for _ in range(1, 1000)], True),

        # Edge case: Empty graph
        ([], True),

        # Edge case: Single node without any edges (bipartite)
        ([[]], True),

        # Graph with two nodes and one edge (bipartite)
        ([[1],[0]], True),

        # Graph with two nodes but no edges (bipartite)
        ([[],[]], True),

        # Multiple components, one of which is not bipartite
        ([[1],[0,2,3],[1,3],[1,2,4,5],[3,5],[3,4], [7,8],[6,8],[6,7]], False)
    ]
)
def test_isBipartite(graph: List[List[int]], expected: bool):
    assert isBipartite(graph) == expected
