
def find_min_unsorted_subarray(integers: list[int] | tuple[int]) -> int:  # LeetCode Q.581.
    total_ints = len(integers)
    next_smaller_indices = [-1] * total_ints  # Indices of next smaller num.
    stack = [(0, integers[0])]  # Monotonic-increasing stack: (idx, num).

    for current_idx in range(1, total_ints):
        while stack and stack[-1][1] > integers[current_idx]:  # Next smaller found.
            past_idx, _ = stack.pop(-1)
            next_smaller_indices[past_idx] = current_idx

        stack.append((current_idx, integers[current_idx]))

    if sum(next_smaller_indices) == -total_ints:  # Integers are perfectly sorted.
        return 0

    first_misplaced_idx = -1  # Forward search: first misplaced idx.
    for iteration_idx, next_smaller_idx in enumerate(next_smaller_indices):
        if next_smaller_idx != -1:
            first_misplaced_idx = iteration_idx
            break

    last_misplaced_idx = -1  # "Backward search (use [::-1])": last misplaced idx.
    for iteration_idx, next_smaller_idx in enumerate(next_smaller_indices[::-1]):
        if next_smaller_idx != -1:
            last_misplaced_idx = total_ints - 1 - iteration_idx
            break

    # First & last misplaced indices slice an unsorted subarray.
    max_misplaced_num = max(integers[first_misplaced_idx: last_misplaced_idx + 1])

    # Extension: nums after last misplaced idx may < unsorted subarray maximum.
    # Backward search (use [::-1]): the furthest extension.
    for iteration_idx, num in enumerate(integers[last_misplaced_idx + 1 - total_ints:][::-1]):
        if num < max_misplaced_num:
            last_misplaced_idx = total_ints - 1 - iteration_idx
            break

    return last_misplaced_idx - first_misplaced_idx + 1
