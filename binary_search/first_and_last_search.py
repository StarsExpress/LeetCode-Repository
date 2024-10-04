
def search_positions(numbers: list[int], target: int) -> list[int]:  # LeetCode Q.34.
    """Find 1st and last indices of a target in sorted array."""
    total_nums = len(numbers)
    back_idx, front_idx = 0, total_nums - 1
    # 1st search: final back idx indicates number of ints < target.
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if numbers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    if not (back_idx < total_nums and numbers[back_idx] == target):
        return [-1, -1]  # Target not found.
    positions = [back_idx]

    front_idx = total_nums - 1
    # 2nd search: final back idx indicates number of ints <= target.
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if numbers[mid_idx] <= target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    positions.append(back_idx - 1)
    return positions
