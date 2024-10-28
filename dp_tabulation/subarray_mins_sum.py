
def _find_next_smallers(integers: list[int]) -> list[tuple[int, int]]:
    total_ints = len(integers)
    next_smaller = [(-1, -1)] * total_ints
    stack = [(0, integers[0])]  # Increasing monotonic stack: (idx, num).

    for current_idx in range(1, total_ints):
        while stack and stack[-1][1] > integers[current_idx]:  # Next smaller found.
            past_idx, _ = stack.pop(-1)
            next_smaller[past_idx] = (current_idx, integers[current_idx])

        stack.append((current_idx, integers[current_idx]))

    return next_smaller


def sum_subarray_mins(integers: list[int]) -> int:  # LeetCode Q.907.
    total_ints = len(integers)
    subarray_mins = [0] * total_ints

    next_smallers = _find_next_smallers(integers)
    for reverse_idx, current_num in enumerate(reversed(integers)):
        current_idx = total_ints - 1 - reverse_idx  # Index mapping.

        next_smaller_idx = next_smallers[current_idx][0]
        if next_smaller_idx == -1:  # No next smaller for current num.
            # Current num is min of all subarrays from current idx toward the end.
            subarray_mins[current_idx] += current_num * (total_ints - current_idx)
            continue

        # Next smaller int is min of all subarrays from next smaller idx toward the end.
        subarray_mins[current_idx] += subarray_mins[next_smaller_idx]
        # Current num is min of subarrays ending before next smaller int.
        subarray_mins[current_idx] += current_num * (next_smaller_idx - current_idx)

    return sum(subarray_mins) % (10 ** 9 + 7)
