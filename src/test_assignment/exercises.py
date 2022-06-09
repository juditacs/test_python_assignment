from typing import Any, Sequence


# Define a function that takes a sequence as its input and returns whether the sequence is symmetric.
# A sequence is symmetric if it is equal to its reverse.
def is_symmetric(sequence: Sequence[Any]) -> bool:
    for i in range(len(sequence) // 2):
        if sequence[i] != sequence[-(i+1)]:
            return False
    return True
