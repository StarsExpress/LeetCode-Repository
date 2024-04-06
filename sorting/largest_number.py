
def judge_impact(candidate: int, pivot: int):
    # Return true if candidate's "impact" > pivot's "impact".
    candidate, pivot = str(candidate), str(pivot)
    if len(candidate) == len(pivot):
        return True if candidate > pivot else False  # Whenever a tie comes, set pivot as the winner.

    common_range = min(len(candidate), len(pivot))
    if candidate[:common_range] == pivot[:common_range]:  # Identical in common range.
        return False if pivot + candidate >= candidate + pivot else True

    return True if candidate > pivot else False


def find_largest_combined_integer(integers: list[int], recursive=False):  # LeetCode Q.179.
    if len(integers) <= 1:
        if recursive:
            return integers
        return str(integers[0])

    pivot, front_idx, back_idx = integers[0], 1, 1

    while front_idx < len(integers):  # Until front idx reaches the end.
        # Quick sort from biggest to smallest.
        if judge_impact(integers[front_idx], pivot):
            integers[back_idx], integers[front_idx] = integers[front_idx], integers[back_idx]
            back_idx += 1
        front_idx += 1

    integers[0], integers[back_idx - 1] = integers[back_idx - 1], integers[0]

    integers[:back_idx - 1] = find_largest_combined_integer(integers[:back_idx - 1], True)
    integers[back_idx:] = find_largest_combined_integer(integers[back_idx:], True)
    if recursive:
        return integers

    if set(integers) == {0}:  # Special case: all 0.
        return '0'
    return ''.join(str(integer) for integer in integers)
