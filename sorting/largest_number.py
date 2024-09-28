
def _judge_impact(candidate: int, pivot: int) -> bool:
    # Return true if candidate's "impact" > pivot's "impact".
    candidate, pivot = str(candidate), str(pivot)
    candidate_len, pivot_len = len(candidate), len(pivot)
    if candidate_len == pivot_len:
        return True if candidate > pivot else False  # Whenever a tie comes, set pivot as the winner.

    common_range = min(candidate_len, pivot_len)
    if candidate[:common_range] == pivot[:common_range]:  # Identical in common range.
        return True if candidate + pivot > pivot + candidate else False

    return True if candidate > pivot else False


def find_largest_combined_integer(integers: list[int], recursive: bool=False) -> str:  # LeetCode Q.179.
    total_integers = len(integers)
    if total_integers == 1:  # Base case.
        return str(integers[0])
    if set(integers) == {0}:  # Special case: all 0.
        return "0" * total_integers if recursive else "0"

    pivot, front_idx, back_idx = integers[0], 1, 1
    while front_idx < total_integers:
        # Quick sort from biggest to smallest.
        if _judge_impact(integers[front_idx], pivot):
            integers[back_idx], integers[front_idx] = integers[front_idx], integers[back_idx]
            back_idx += 1
        front_idx += 1

    # Switch pivot with item at back idx - 1.
    integers[0], integers[back_idx - 1] = integers[back_idx - 1], integers[0]

    largest_number = ""
    if back_idx > 1:
        largest_number += find_largest_combined_integer(integers[:back_idx - 1], True)
    largest_number += str(integers[back_idx - 1])
    if back_idx < total_integers:
        largest_number += find_largest_combined_integer(integers[back_idx:], True)
    return largest_number
