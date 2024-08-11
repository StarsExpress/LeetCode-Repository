
def find_circular_next_greater(numbers: list[int] | tuple[int]):  # LeetCode Q.503.
    total_nums = len(numbers)
    next_greater = [-1] * total_nums
    stack = [(0, numbers[0])]  # Decreasing monotonic stack: (idx, num).

    # Circular search: double iterations and let remainder adjust iteration idx.
    for current_idx in range(1, 2 * total_nums):
        while stack and stack[-1][1] < numbers[current_idx % total_nums]:
            past_idx, _ = stack.pop(-1)
            if next_greater[past_idx] == -1:  # Only update those not updated yet.
                next_greater[past_idx] = numbers[current_idx % total_nums]

        stack.append((current_idx % total_nums, numbers[current_idx % total_nums]))

    return next_greater
