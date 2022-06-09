import pytest

from test_assignment.exercises import is_symmetric, count_elements


@pytest.mark.parametrize(
    "sequence, answer",
    [
        ("abcba", True),
        ([], True),
        ([1], True),
        (["abc", "bcd"], False),
        (["abc", "bcd","abc"], True),
        ((1, 2, 2, 1), True),
        ([None, None], True),
        ([1, 2, 3, 1], False),
        ([1, "foo", "bar", "foo", 1], True),
        (list(range(100)) + list(range(99, -1, -1)), True),
        (list(range(100)) + list(range(100, 0, -1)), False),
        ([1, "1"], False),
    ],
)
def test_is_symmetric(sequence, answer):
    assert is_symmetric(sequence) == answer


def test_count_elements():
    assert count_elements([1, 2, 0, 1, 1]) == {1: 3, 2: 1, 0: 1}
    # test for tuple
    assert count_elements((1, 2, 0, 1, 1)) == {1: 3, 2: 1, 0: 1}
    # test empty list
    assert count_elements([]) == {}
    # test mixed types
    assert count_elements([1, "1", 1]) == {1: 2, "1": 1}
