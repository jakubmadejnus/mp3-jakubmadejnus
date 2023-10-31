import pytest
from typing import List

from questions.num_of_islands import num_distinct_islands

@pytest.mark.parametrize(
    "grid, expected",
    [
        # Test case 1
        ([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]], 1),

        # Test case 2
        ([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]], 3),

        # Test case 3: No islands.
        ([[0,0,0],[0,0,0],[0,0,0]], 0),

        # Test case 4: Single large island.
        ([[1,1,1],[1,0,1],[1,1,1]], 1),

        # Test case 5: Distinct islands with same area but different shapes.
        ([[1,0,0,0,1],[0,1,1,1,0],[0,1,0,1,0],[0,1,1,1,0],[1,0,0,0,1]], 2),

        # Test case 6: All water, no land.
        ([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]], 0),

        # Test case 7: All land, no water.
        ([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]], 1),

        # Test case 8: Complex layout with multiple distinct islands.
        ([[1,1,0,0,1,0,1,1,1,1],
          [1,1,0,0,1,0,1,1,1,1],
          [1,1,0,0,0,0,0,0,0,0],
          [0,0,0,1,1,1,0,0,0,0],
          [0,1,0,1,1,0,1,1,1,0],
          [0,1,0,0,0,0,1,1,1,0],
          [0,0,1,1,0,1,1,1,0,0],
          [0,0,1,1,1,1,1,1,0,0]], 5),

        # Test case 9: Edge case with single cell island.
        ([[1]], 1),

    ]
)
def test_num_distinct_islands(grid: List[List[int]], expected: int):
    assert num_distinct_islands(grid) == expected
