import pytest
from questions.alien_words import find_order

@pytest.mark.parametrize(
    "words, expected_output",
    [
        # Basic tests
        (["ba", "bc", "ac", "cab"], "bac"),
        
        # Intermediate tests
        (["cab", "aaa", "aab"], "cab"),
        (["ywx", "wz", "xww", "xz", "zyy", "zwz"], "ywxz"),
        
        # Edge cases
        ([], ""),
        (["a"], "a"),
        
        # Large input for efficiency testing
        (["a" * i + "b" + "a" * (1000 - i) for i in range(1000)], "ba"),
        (["z" + chr(i) for i in range(97, 123)] + ["z" * 26], "abcdefghijklmnopqrstuvwxyz")
    ]
)
def test_find_order(words, expected_output):
    assert find_order(words) == expected_output
