
def count_steps(binary_integer: str):  # LeetCode Q.1404.
    """Count number of steps to reduce binary-formatted integer to 1."""
    steps, integer = 0, int(binary_integer, 2)
    while integer > 1:
        if integer % 2 == 1:
            integer += 1
            steps += 1

        integer >>= 1
        steps += 1

    return steps
