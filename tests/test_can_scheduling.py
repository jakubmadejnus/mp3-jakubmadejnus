import pytest
from questions.can_scheduling import can_schedule_tasks

@pytest.mark.parametrize("tasks, prerequisites, expected", [
    # Basic cases
    (3, [[0, 1], [1, 2]], True),
    (3, [[0, 1], [1, 2], [2, 0]], False),
    (6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]], True),

    # Edge cases
    (0, [], False),
    (1, [], True),
    (1, [[0, 0]], False),

    # Inductive steps
    (4, [[0, 1], [1, 2], [2, 3]], True),
    (4, [[0, 1], [1, 2], [2, 0]], False),
    (4, [[0, 1], [1, 2], [2, 3], [3, 1]], False),

    # Larger scenarios
    (5, [[0, 1], [1, 2], [2, 3], [3, 4]], True),
    (5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 2]], False),

    # Isolated nodes
    (5, [[0, 1], [1, 2]], True),  # Nodes 3 and 4 are not connected to the rest of the graph

    # Multiple components, some with circular dependencies
    (6, [[0, 1], [1, 2], [3, 4], [4, 5]], True),  # Two distinct components
    (6, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5]], False),  # First component has circular dependency

    # More complex circular dependencies
    (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 2]], False),  # Circular dependency through nodes 2, 3, 4, 5

    # Large values (for efficiency testing)
    (10**5, [[i, i + 1] for i in range(10**5 - 1)], True),  # Linear dependency
    (10**5, [[i, i + 1] for i in range(10**5 - 1)] + [[10**5 - 1, 0]], False),  # Circular dependency

    # Large values with multiple components
    (10**5, [[i, i + 1] for i in range(49999)] + [[i, i + 1] for i in range(50000, 10**5 - 1)], True),  # Two separate linear components

    # Large star structure, with one central node
    (10**5, [[i, 0] for i in range(1, 10**5)], True),  # Node 0 is the central node

])
def test_can_schedule_tasks(tasks, prerequisites, expected):
    assert can_schedule_tasks(tasks, prerequisites) == expected
