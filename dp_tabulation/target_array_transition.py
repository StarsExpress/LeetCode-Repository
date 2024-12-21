
def calculate_min_transition(numbers: list[int], targets: list[int]) -> int:  # LeetCode Q.3229.
    min_operations = 0

    positive_stack, positive_cushion = [], 0  # Difference decreasing monotonic stack.
    negative_stack, negative_cushion = [], 0  # Difference increasing monotonic stack.

    for target, number in zip(targets, numbers):
        difference = target - number
        if positive_stack:
            if difference <= 0 or difference > positive_stack[-1]:  # Reset positive stack.
                min_operations += positive_stack[0] - positive_cushion

                positive_cushion = 0 if difference <= 0 else positive_stack[-1]

                positive_stack.clear()

        if negative_stack:
            if difference >= 0 or difference < negative_stack[-1]:  # Reset negative stack.
                min_operations += negative_cushion - negative_stack[0]

                negative_cushion = 0 if difference >= 0 else negative_stack[-1]

                negative_stack.clear()

        if difference > 0:
            positive_stack.append(difference)

        if difference < 0:
            negative_stack.append(difference)

    if positive_stack:  # Last difference might be in positive stack.
        min_operations += positive_stack[0] - positive_cushion

    if negative_stack:  # Last difference might be in negative stack.
        min_operations += negative_cushion - negative_stack[0]

    return min_operations
