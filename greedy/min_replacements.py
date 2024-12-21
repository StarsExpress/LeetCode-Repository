
def count_min_operations(numbers: list[int]) -> int:  # LeetCode Q.2366.
    min_operations, total_numbers = 0, len(numbers)

    current_idx = -2  # Backward idx.
    comparison_number = numbers[-1]
    while current_idx >= -total_numbers:
        if numbers[current_idx] > comparison_number:
            # Ceiling of division = pieces to break into.
            pieces = (numbers[current_idx] + comparison_number - 1) // comparison_number
            min_operations += pieces - 1
            comparison_number = numbers[current_idx] // pieces

        else:
            comparison_number = numbers[current_idx]

        current_idx -= 1

    return min_operations
