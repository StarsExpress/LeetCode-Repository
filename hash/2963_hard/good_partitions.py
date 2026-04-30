
def count_good_partitions(nums: list[int]) -> int:  # LeetCode Q.2963.
    nums_last_indices: dict[int, int] = dict()  # Each num's last idx.

    for idx, num in enumerate(nums):
        nums_last_indices[num] = idx

    windows_count = 0  # Sliding window by three pointers.
    left_idx, mid_idx, right_idx = 0, 0, 0

    while right_idx < len(nums):
        num = nums[mid_idx]
        mid_idx += 1  # Already visited.

        if right_idx < nums_last_indices[num]:  # Num extends current window.
            right_idx = nums_last_indices[num]
            continue

        if mid_idx >= right_idx:
            windows_count += 1  # Current window is finalized.

            left_idx = right_idx + 1  # Search for another window, if possible.
            mid_idx, right_idx = left_idx, left_idx

    good_partitions = 1
    power = windows_count - 1
    base = 2  # Mod exp method speeds up quite some in Python.
    modulo = 10 ** 9 + 7

    while power > 0:
        if power % 2 == 1:  # Power is odd: product times current base.
            good_partitions *= base
            good_partitions %= modulo

        base = (base * base) % modulo  # Square base and reduce power.
        power //= 2

    return good_partitions
