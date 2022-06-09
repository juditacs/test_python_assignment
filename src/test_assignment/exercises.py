from typing import Any, Dict, Sequence


# Define a function that takes a sequence as its input and returns whether the
# sequence is symmetric. A sequence is symmetric if it is equal to its reverse.

def is_symmetric(sequence: Sequence[Any]) -> bool:
    for i in range(len(sequence) // 2):
        if sequence[i] != sequence[-(i+1)]:
            return False
    return True


# Define a function that takes a sequence and counts the frequency of each
# element in the list. The function should return a dictionary of the counts.
# Do not use the collections module.

def count_elements(sequence: Sequence[Any]) -> Dict[Any, int]:
    # TODO
    pass
