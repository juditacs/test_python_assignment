import pytest

from test_assignment.exercises import is_symmetric


@pytest.mark.parametrize(
    "sequence, answer",
    [
        ("abcba", True),
        ([], True),
        ([1], True),
        (["abc", "bcd"], False),
        (["abc", "bcd","abc"], True),
        ((1, 2, 2, 1), True),
    ],
)
def test_is_symmetric(sequence, answer):
    assert is_symmetric(sequence) == answer

