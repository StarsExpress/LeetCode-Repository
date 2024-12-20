
def find_next_greater(numbers: list[int | float]) -> list[int | float]:
    total_numbers = len(numbers)
    next_greater = [-1] * total_numbers
    stack = [(0, numbers[0])]  # Decreasing monotonic stack: (idx, num).

    for current_idx in range(1, total_numbers):
        # Past num < current num: next greater found.
        while stack and stack[-1][1] < numbers[current_idx]:
            past_idx, _ = stack.pop(-1)
            next_greater[past_idx] = numbers[current_idx]

        stack.append((current_idx, numbers[current_idx]))

    return next_greater
