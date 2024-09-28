
def count_min_unique_increments(numbers: list[int]) -> int:  # LeetCode Q.945.
    numbers.sort()
    increments, current_idx, total_numbers = 0, 1, len(numbers)
    while current_idx < total_numbers:
        if numbers[current_idx] <= numbers[current_idx - 1]:
            increment = numbers[current_idx - 1] + 1 - numbers[current_idx]
            numbers[current_idx] += increment
            increments += increment

        current_idx += 1

    return increments
