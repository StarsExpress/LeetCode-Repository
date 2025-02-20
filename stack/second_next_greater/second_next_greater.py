
def find_second_next_greater(nums: list[int]) -> list[int]:  # LeetCode Q.2454.
    total_nums = len(nums)
    second_next_greater = [-1] * total_nums

    stack_1, stack_2 = [(nums[0], 0)], []  # Decreasing monotonic stacks: (num, idx).
    transporter = []  # Increasing monotonic list: transports stack 1 tuples to stack 2.

    for current_idx in range(1, total_nums):
        while stack_2 and stack_2[-1][0] < nums[current_idx]:
            _, past_idx = stack_2.pop(-1)
            second_next_greater[past_idx] = nums[current_idx]

        while stack_1 and stack_1[-1][0] < nums[current_idx]:
            transporter.append(stack_1.pop(-1))

        stack_2.extend(transporter[::-1])  # Ensure decreasing monotonicity.
        transporter.clear()
        stack_1.append((nums[current_idx], current_idx))

    return second_next_greater
