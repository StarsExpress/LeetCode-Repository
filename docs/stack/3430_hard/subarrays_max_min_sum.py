
def compute_max_min_sum(nums: list[int], k: int) -> int:  # LeetCode Q.3430.
    subarrays_max_min_sum = 0

    max_stack: list[list[int]] = []  # Format: [idx, num, shares].
    subarrays_max_sum = 0

    min_stack: list[list[int]] = []  # Format: [idx, num, shares].
    subarrays_min_sum = 0

    for end_idx, num in enumerate(nums):
        start_idx = max(0, end_idx - k + 1)

        # Window start idx slides by 1: must update stacks' info.
        if start_idx > 0:
            max_stack[0][2] -= 1  # Decrement stack's front num shares.
            subarrays_max_sum -= max_stack[0][1]

            if max_stack[0][0] < start_idx:  # Front num out of window.
                max_stack.pop(0)

            min_stack[0][2] -= 1  # Decrement stack's front num shares.
            subarrays_min_sum -= min_stack[0][1]

            if min_stack[0][0] < start_idx:  # Front num out of window.
                min_stack.pop(0)

        while max_stack and max_stack[-1][1] <= num:
            _, prev_num, prev_shares = max_stack.pop(-1)
            subarrays_max_sum -= prev_num * prev_shares

        if not max_stack:
            shares = min(end_idx + 1, k)

        else:
            shares = end_idx - max_stack[-1][0]

        subarrays_max_sum += num * shares
        max_stack.append([end_idx, num, shares])

        while min_stack and min_stack[-1][1] >= num:
            _, prev_num, prev_shares = min_stack.pop(-1)
            subarrays_min_sum -= prev_num * prev_shares

        if not min_stack:
            shares = min(end_idx + 1, k)

        else:
            shares = end_idx - min_stack[-1][0]

        subarrays_min_sum += num * shares
        min_stack.append([end_idx, num, shares])

        subarrays_max_min_sum += subarrays_max_sum + subarrays_min_sum

    return subarrays_max_min_sum
