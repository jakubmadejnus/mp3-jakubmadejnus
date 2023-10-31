import pytest
from questions.reconstruct_a_sequence import can_construct

@pytest.mark.parametrize(
    "originalSeq, seqs, expected_output",
    [
        # Basic tests
        ([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]], True),
        
        # Intermediate tests
        ([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]], False),
        ([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]], True),
        
        # Edge cases
        ([], [], False),
        ([1], [], False),
        ([1], [[1]], True),
        
        # Large input for efficiency testing
        (list(range(1, 1001)), [list(range(i, i + 20)) for i in range(1, 1000, 20)], False),
        
        # Overlapping sequences but valid construction
        ([1, 2, 3, 4], [[1, 2, 3], [3, 4]], True),
        
        # Overlapping sequences but invalid construction
        ([1, 2, 3, 4], [[1, 3], [3, 2]], False),
        
        # Missing sequences
        ([1, 2, 3, 4], [[1, 2], [3, 4], [2]], False),
        
        # Extra sequences not present in original
        ([1, 2, 3], [[1, 2], [2, 3], [3, 4]], False),
        
        # Sequence sets with duplicated sequences
        ([1, 2, 3, 4], [[1, 2], [1, 2], [3, 4]], False),
        
        # Reverse order
        ([4, 3, 2, 1], [[4, 3], [3, 2], [2, 1]], True),
        
        # Complex overlapping sequences
        ([1, 3, 5, 7, 9, 2, 4, 6, 8], [[1, 3, 5], [5, 7, 9], [9, 2, 4], [4, 6, 8]], True),
    ]
)
def test_can_construct(originalSeq, seqs, expected_output):
    assert can_construct(originalSeq, seqs) == expected_output
