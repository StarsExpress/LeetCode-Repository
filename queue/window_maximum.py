
def find_sliding_window_maximum(integers: list[int], window_size: int):  # LeetCode Q.239.
    if window_size == 1:
        return integers

    window_maximums = []
    # Queue contains indices of ints under current sliding window.
    idx_queue = [0]  # Queue's 1st idx always points to window maximum.
    for idx, integer in enumerate(integers):
        if idx == 0:  # 1st int's idx is automatically into queue.
            continue

        # Ensure last idx's corresponding int > current int.
        while idx_queue and integers[idx_queue[-1]] <= integer:
            idx_queue.pop(-1)

        # Ensure 1st idx is in current window.
        while idx_queue and idx - window_size + 1 > idx_queue[0]:
            idx_queue.pop(0)

        idx_queue.append(idx)
        if idx >= window_size - 1:  # When 1st (window size) ints have all been "seen".
            window_maximums.append(integers[idx_queue[0]])

    return window_maximums
