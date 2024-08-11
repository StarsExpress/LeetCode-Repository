
def find_next_greater(numbers: list[int | float] | tuple[int | float]):
    next_greater = [-1] * len(numbers)
    stack = [(0, numbers[0])]  # Decreasing monotonic stack: (idx, num).

    for current_idx in range(1, len(numbers)):
        if stack:
            past_idx, past_num = stack.pop(-1)
            while past_num < numbers[current_idx]:  # Past num < current num: next greater found.
                next_greater[past_idx] = numbers[current_idx]
                if not stack:
                    break
                past_idx, past_num = stack.pop(-1)

            if past_num >= numbers[current_idx]:  # Past num >= current num: back to stack.
                stack.append((past_idx, past_num))

        stack.append((current_idx, numbers[current_idx]))

    return next_greater
