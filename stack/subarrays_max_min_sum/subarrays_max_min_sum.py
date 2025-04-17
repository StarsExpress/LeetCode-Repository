
def compute_subarrays_min_max_sum(nums: list[int], k: int) -> int:  # LeetCode Q.3430.
    subarrays_max_min_sum = 0

    decreasing_stack: list[list[int]] = []  # Format: [idx, num, shares].
    subarrays_max_sum = 0
    increasing_stack: list[list[int]] = []  # Format: [idx, num, shares].
    subarrays_min_sum = 0

    start_idx = 1 - k
    for end_idx, num in enumerate(nums):
        if start_idx > 0:  # Ensure both stacks have current subarrays' window.
            decreasing_stack[0][2] -= 1  # Decrement stack's 1st num shares by 1.
            subarrays_max_sum -= decreasing_stack[0][1]
            if decreasing_stack[0][0] < start_idx:  # Stack's 1st num out of window.
                decreasing_stack.pop(0)

            increasing_stack[0][2] -= 1  # Decrement stack's 1st num shares by 1.
            subarrays_min_sum -= increasing_stack[0][1]
            if increasing_stack[0][0] < start_idx:  # Stack's 1st num out of window.
                increasing_stack.pop(0)

        while decreasing_stack and decreasing_stack[-1][1] <= num:
            subarrays_max_sum -= decreasing_stack[-1][1] * decreasing_stack[-1][2]
            decreasing_stack.pop(-1)

        if not decreasing_stack:
            shares = min(end_idx + 1, k)

        else:
            shares = end_idx - decreasing_stack[-1][0]

        subarrays_max_sum += num * shares
        subarrays_max_min_sum += subarrays_max_sum
        decreasing_stack.append([end_idx, num, shares])

        while increasing_stack and increasing_stack[-1][1] >= num:
            subarrays_min_sum -= increasing_stack[-1][1] * increasing_stack[-1][2]
            increasing_stack.pop(-1)

        if not increasing_stack:
            shares = min(end_idx + 1, k)

        else:
            shares = end_idx - increasing_stack[-1][0]

        subarrays_min_sum += num * shares
        subarrays_max_min_sum += subarrays_min_sum
        increasing_stack.append([end_idx, num, shares])

        start_idx += 1

    return subarrays_max_min_sum
