
def search_positions(numbers: list[int], target: int) -> list[int]:  # LeetCode Q.34.
    """Find 1st and last indices of a target in sorted array."""
    total_nums = len(numbers)
    left_idx, right_idx = 0, total_nums - 1
    # 1st search: final back idx indicates number of ints < target.
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if numbers[mid_idx] < target:
            left_idx = mid_idx + 1
            continue
        right_idx = mid_idx - 1

    if not (left_idx < total_nums and numbers[left_idx] == target):
        return [-1, -1]  # Target not found.
    positions = [left_idx]

    right_idx = total_nums - 1
    # 2nd search: final back idx indicates number of ints <= target.
    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if numbers[mid_idx] <= target:
            left_idx = mid_idx + 1
            continue
        right_idx = mid_idx - 1

    positions.append(left_idx - 1)
    return positions
