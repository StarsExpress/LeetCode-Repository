
def find_next_permutation(numbers: list[int]) -> None:  # LeetCode Q.31.
    """Required to modify numbers in-place."""
    total_nums = len(numbers)
    start_idx = 0  # Default to sort the entire nums from smallest to biggest.
    for pivot_idx in range(total_nums - 2, -1, -1):
        if numbers[pivot_idx] >= numbers[pivot_idx + 1]:  # Not pivot.
            continue

        for successor_idx in range(total_nums - 1, pivot_idx, -1):  # Find successor once pivot is set.
            if numbers[successor_idx] > numbers[pivot_idx]:
                numbers[pivot_idx], numbers[successor_idx] = numbers[successor_idx], numbers[pivot_idx]
                start_idx += pivot_idx + 1
                break
        break

    numbers[start_idx:] = sorted(numbers[start_idx:])  # Indexing: modify in-place.
