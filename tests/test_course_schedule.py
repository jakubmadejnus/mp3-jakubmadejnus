import pytest

from questions.course_schedule import canFinish

@pytest.mark.parametrize("numCourses, prerequisites, expected", [
    # Basic tests
    (2, [[1,0]], True),
    (2, [[1,0],[0,1]], False),
    (3, [[0,1],[1,2],[2,0]], False),
    (4, [[1,0],[2,0],[3,1],[3,2]], True),
    (1, [], True),
    
    # Complex tests
    (5, [[4,3],[3,2],[2,1],[1,0]], True),
    (6, [[5,4],[4,3],[3,2],[2,1],[1,0],[0,5]], False),
    (8, [[3,2],[2,1],[1,0],[6,5],[5,4],[7,6]], True),

    # Edge cases
    (1, [[0,0]], False),
    (0, [], True),
    (6, [], True),
    
])
def test_canFinish(numCourses, prerequisites, expected):
    assert canFinish(numCourses, prerequisites) == expected
