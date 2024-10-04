
def max_topmost(numbers: list[int], k: int) -> int:  # LeetCode Q.2202.
    total_nums = len(numbers)
    if total_nums == 1:  # Base case.
        return -1 if k % 2 == 1 else numbers[0]
    if k <= 1:  # Base case.
        return numbers[k]

    front_max = max(numbers[:k - 1])  # Max from front k - 1 nums.
    if total_nums <= k:  # Doesn't have kth idx.
        return front_max
    # Max may be the num at kth idx by removing front k nums.
    return max(numbers[k], front_max)
