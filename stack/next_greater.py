
def find_next_greater_number(numbers: list[int | float] | tuple[int | float]):
    next_greater, stack = [None] * len(numbers), [(0, numbers[0])]  # Stack format: (idx, num).
    for current_num_idx in range(1, len(numbers)):
        if stack:
            past_idx, past_num = stack.pop()
            while past_num < numbers[current_num_idx]:  # Past num < current num: next greater found.
                next_greater[past_idx] = numbers[current_num_idx]
                if len(stack) <= 0:
                    break
                past_idx, past_num = stack.pop()

            if past_num >= numbers[current_num_idx]:  # Past num >= current num: push it back to stack.
                stack.append((past_idx, past_num))

        # Push current num to stack as it may be a next greater num.
        stack.append((current_num_idx, numbers[current_num_idx]))

    return next_greater
