import pytest
from questions.town_judge import findJudge

@pytest.mark.parametrize(
    "n,trust,expected",
    [
        # Basic test cases
        (2, [[1,2]], 2),
        (3, [[1,3],[2,3]], 3),
        (3, [[1,3],[2,3],[3,1]], -1),

        # Edge Cases
        # No trust relationships
        (1, [], 1),
        
        # Multiple people trust the judge
        (4, [[1,4],[2,4],[3,4]], 4),
        
        # Judge trusts one person, so no judge exists
        (4, [[1,4],[2,4],[3,4],[4,2]], -1),
        
        # Everyone trusts everyone, so no judge exists
        (3, [[1,2],[2,3],[3,1],[1,3],[2,1],[3,2]], -1),

        # Larger tests with clear judge
        (5, [[1,5],[2,5],[3,5],[4,5]], 5),
        
        # Larger tests with no clear judge due to circular trusts
        (5, [[1,5],[2,5],[3,5],[4,5],[5,1]], -1),
        
        # Larger test, all trust only one person except that person, but that person trusts one another person
        (6, [[1,6],[2,6],[3,6],[4,6],[5,6],[6,2]], -1),

        # Only one trust relationship exists, judge is not found
        (5, [[1,3]], -1),
        
        # Everyone except one person trusts the judge, so no judge exists
        (4, [[1,4],[2,4],[4,3]], -1),

        # Single trust chain, but not everyone trusts the last person
        (5, [[1,2],[2,3],[3,4]], -1),
    ]
)
def test_findJudge(n, trust, expected):
    assert findJudge(n, trust) == expected
