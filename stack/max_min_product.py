
def find_max_min_product(numbers: list[int]) -> int:  # LeetCode Q.1856.
    """
    Key: each number is the minimum of a certain range. Find out this range,
    and multiply this number with range sum to find its min product.
    """
    prefix_sums, total_numbers = [], len(numbers)

    next_smaller_indices: list[int | None] = [None] * total_numbers
    stack = [(0, numbers[0])]  # Increasing monotonic stack: (idx, number).

    for current_idx, number in enumerate(numbers):
        if current_idx == 0:  # 1st number.
            prefix_sums.append(number)
            continue

        # Past number > current number: next smaller found.
        while stack and stack[-1][1] > number:
            past_idx, _ = stack.pop(-1)
            next_smaller_indices[past_idx] = current_idx

        stack.append((current_idx, number))
        prefix_sums.append(prefix_sums[-1] + number)

    last_smaller_indices: list[int | None] = [None] * total_numbers
    stack.clear()
    stack.append((-1, numbers[-1]))  # Increasing monotonic stack: (idx, number).

    for reverse_idx, number in enumerate(numbers[::-1]):  # Backward iteration.
        if reverse_idx > 0:  # Not the last number.
            current_idx = total_numbers - 1 - reverse_idx
            # Future number > current number: last smaller found.
            while stack and stack[-1][1] > number:
                future_idx, _ = stack.pop(-1)
                last_smaller_indices[future_idx] = current_idx

            stack.append((current_idx, number))

    max_min_product = -float("inf")
    for idx, number in enumerate(numbers):
        subarray_sum = number

        next_smaller_idx = next_smaller_indices[idx]
        if next_smaller_idx is not None:  # All the way to (next smaller idx - 1)th number.
            subarray_sum += prefix_sums[next_smaller_idx - 1] - prefix_sums[idx]

        else:  # All the way to the rightmost number.
            subarray_sum += prefix_sums[-1] - prefix_sums[idx]

        last_smaller_idx = last_smaller_indices[idx]
        if last_smaller_idx is not None:  # All the way to (last smaller idx + 1)th number.
            subarray_sum += prefix_sums[idx - 1] - prefix_sums[last_smaller_idx]

        if idx > 0 and last_smaller_idx is None:
            # Current number isn't the 1st number and doesn't have a last smaller number.
            subarray_sum += prefix_sums[idx - 1]

        min_product = number * subarray_sum
        if min_product > max_min_product:
            max_min_product = min_product

    return max_min_product % (10 ** 9 + 7)  # Required to control size.
