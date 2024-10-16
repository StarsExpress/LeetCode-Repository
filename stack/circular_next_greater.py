
def find_circular_next_greater(numbers: list[int]) -> list[int]:  # LeetCode Q.503.
    total_numbers = len(numbers)
    next_greater = [-1] * total_numbers
    stack = [(0, numbers[0])]  # Decreasing monotonic stack: (idx, num).

    # Circular search: double iterations and let remainder adjust iteration idx.
    for current_idx in range(1, 2 * total_numbers):
        while stack and stack[-1][1] < numbers[current_idx % total_numbers]:
            past_idx, _ = stack.pop(-1)
            if next_greater[past_idx] == -1:  # Only update those not updated yet.
                next_greater[past_idx] = numbers[current_idx % total_numbers]

        stack.append((current_idx % total_numbers, numbers[current_idx % total_numbers]))

    return next_greater
