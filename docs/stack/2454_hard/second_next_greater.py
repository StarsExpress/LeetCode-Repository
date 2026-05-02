
def find_second_next_greater(nums: list[int]) -> list[int]:  # LeetCode Q.2454.
    second_next_greater = [-1] * len(nums)
    stack_1, stack_2 = [], []  # Decreasing monotonic stacks: (num, idx).
    transporter = []  # Transport tuples from stack 1 to stack 2.

    for idx, num in enumerate(nums):
        while stack_2 and stack_2[-1][0] < num:
            _, past_idx = stack_2.pop(-1)
            second_next_greater[past_idx] = num

        while stack_1 and stack_1[-1][0] < num:
            transporter.append(stack_1.pop(-1))
        
        while transporter:
            stack_2.append(transporter.pop(-1))  # Ensure decreasing monotonicity.
        stack_1.append((num, idx))

    return second_next_greater
