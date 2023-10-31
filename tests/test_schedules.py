import pytest
from questions.schedules import possible_task_orders

@pytest.mark.parametrize("tasks, prerequisites, expected", [
    # Basic cases
    (3, [[0, 1], [1, 2]], [[0, 1, 2]]),

    (4, [[3, 2], [3, 0], [2, 0], [2, 1]], 
     [[3, 2, 0, 1], [3, 2, 1, 0]]),

    (6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]], 
     [
        [0, 1, 4, 3, 2, 5],
        [0, 1, 3, 4, 2, 5],
        [0, 1, 3, 2, 4, 5],
        [0, 1, 3, 2, 5, 4],
        [1, 0, 3, 4, 2, 5],
        [1, 0, 3, 2, 4, 5],
        [1, 0, 3, 2, 5, 4],
        [1, 0, 4, 3, 2, 5],
        [1, 3, 0, 2, 4, 5],
        [1, 3, 0, 2, 5, 4],
        [1, 3, 0, 4, 2, 5],
        [1, 3, 2, 0, 5, 4],
        [1, 3, 2, 0, 4, 5]
     ])
])
def test_possible_task_orders(tasks, prerequisites, expected):
    result = possible_task_orders(tasks, prerequisites)
    assert sorted([tuple(r) for r in result]) == sorted([tuple(e) for e in expected])
