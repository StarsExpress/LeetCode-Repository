
def find_max_modified_subsequence(numbers: list[int]) -> int:  # LeetCode Q.3041
    """Best modified subsequence from numbers array is a subarray of sorted numbers."""
    max_length = 1  # Base case.

    increment = [0, None]  # [Subarray length, subarray max number].
    put = [0, None]  # [Subarray length, subarray max number].

    numbers.sort()
    for number in numbers:
        if max(increment[0], put[0]) > max_length:  # Update max length.
            max_length = max(increment[0], put[0])

        if number == increment[1]:  # Increment to extend the increment.
            increment[0] += 1
            increment[1] += 1

        if number == put[1] and put[0] >= increment[0]:  # Increment to extend the put.
            increment = put
            increment[0] += 1
            increment[1] += 1

        if number - 1 == put[1]:  # Put to extend the put.
            put[0] += 1
            put[1] += 1

        if number - 1 == increment[1]:  # Put to extend the increment.
            if not (number - 1 == put[1] and increment[0] < put[0]):
                put = increment
                put[0] += 1
                put[1] += 1

        if number + 1 != increment[1]:  # Can't lengthen the increment.
            increment = [1, number + 1]  # Reset.

        if number != put[1]:  # Can't lengthen the put.
            put = [1, number]  # Reset.

    return max(increment[0], put[0], max_length)
