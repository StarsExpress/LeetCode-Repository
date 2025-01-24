
def sum_subarray_max(numbers: list[int]) -> int:
    # Format: [number, non-losing count, sum of max of subarrays ending at this number].
    stack: list[list[int]] = []
    subarray_max_sum = 0
    for number in numbers:
        non_losing_count = 1  # Number itself.
        while stack and stack[-1][0] <= number:
            non_losing_count += stack[-1][1]
            subarray_max_sum += stack.pop(-1)[2]

        last_losing_sum = stack[-1][2] if stack else 0
        stack.append([number, non_losing_count, number * non_losing_count + last_losing_sum])

    return subarray_max_sum + sum(max_sum for _, _, max_sum in stack)
