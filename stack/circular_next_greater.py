
def find_next_greater_number(numbers: list[int] | tuple[int]):  # LeetCode Q.503.
    next_greater, stack = [-1] * len(numbers), [(0, numbers[0])]  # Monotonic-decreasing stack: (idx, num).

    total_nums = len(numbers)  # Circular search: double iterations and let remainder adjust iteration idx.
    for current_num_idx in range(1, 2 * total_nums):
        if stack:
            past_idx, past_num = stack.pop(-1)
            # Past num < current num: next greater found.
            while past_num < numbers[current_num_idx % total_nums]:
                if next_greater[past_idx] == -1:  # Only update those not updated yet.
                    next_greater[past_idx] = numbers[current_num_idx % total_nums]
                if len(stack) <= 0:
                    break
                past_idx, past_num = stack.pop(-1)

            if past_num >= numbers[current_num_idx % total_nums]:  # Past num >= current num: back to stack.
                stack.append((past_idx, past_num))

        stack.append((current_num_idx % total_nums, numbers[current_num_idx % total_nums]))

    return next_greater
