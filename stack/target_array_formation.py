
def calculate_min_formation(target: list[int]) -> int:  # LeetCode Q.1526.
    min_operations, stack = 0, []  # Decreasing monotonic stack.
    cushion = 0  # Left neighbor of stack[0] in target array. Default to 0.

    for number in target:
        if stack and number > stack[-1]:
            min_operations += stack[0] - cushion
            cushion = stack[-1]
            stack.clear()  # Numbers in stack can't fully cover current number.

        stack.append(number)

    min_operations += stack[0] - cushion  # Deal with the last iteration.
    return min_operations
