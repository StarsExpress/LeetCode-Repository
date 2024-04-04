
def find_sliding_window_maximum(nums: list[int], size: int):  # LeetCode Q.239.
    if size < 1:
        raise ValueError('Window size must >= 1.')
    if len(nums) < size:
        raise ValueError('Numbers count must >= window size.')

    if size == 1:
        return nums

    maximums, idx_queue, newcomer_idx = [], [0], 1
    while True:
        if newcomer_idx >= len(nums):
            return maximums

        while len(idx_queue) > 0:
            if nums[newcomer_idx] <= nums[idx_queue[-1]]:
                break
            idx_queue.pop(-1)

        while len(idx_queue) > 0:
            if newcomer_idx - size + 1 <= idx_queue[0]:
                break
            idx_queue.pop(0)

        idx_queue.append(newcomer_idx)
        if newcomer_idx >= size - 1:
            maximums.append(nums[idx_queue[0]])
        newcomer_idx += 1
