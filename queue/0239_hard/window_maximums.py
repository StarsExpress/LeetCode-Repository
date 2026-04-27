
def find_window_maximums(nums: list[int], window_size: int) -> list[int]:  # LeetCode Q.239.
    window_maximums = []
    # Queue contains indices of nums under current sliding window.
    queue = []  # Leftmost idx always points to window maximum.
    for idx, num in enumerate(nums):
        # Ensure last idx's num > current num.
        while queue and nums[queue[-1]] <= num:
            queue.pop(-1)

        # Ensure leftmost idx is in window.
        while queue and idx - window_size + 1 > queue[0]:
            queue.pop(0)

        queue.append(idx)
        if idx >= window_size - 1:  # Can collect rolling window maximums.
            window_maximums.append(nums[queue[0]])

    return window_maximums
