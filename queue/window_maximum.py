
def find_sliding_window_maximum(integers: list[int], window_size: int):  # LeetCode Q.239.
    if window_size < 1:
        raise ValueError('Window size must >= 1.')
    if len(integers) < window_size:
        raise ValueError('Numbers count must >= window size.')
    if window_size == 1:
        return integers

    maximums, idx_queue, current_idx = [], [0], 1  # 1st item's idx is automatically into queue.
    while True:
        if current_idx >= len(integers):
            return maximums

        while len(idx_queue) > 0:  # Pop last idx as long as its corresponding int < current int.
            if integers[current_idx] <= integers[idx_queue[-1]]:
                break
            idx_queue.pop(-1)

        while len(idx_queue) > 0:  # Pop first idx as long as it isn't in current window.
            if current_idx - window_size + 1 <= idx_queue[0]:
                break
            idx_queue.pop(0)

        idx_queue.append(current_idx)
        if current_idx >= window_size - 1:  # When 1st (window size) ints have all been "seen" by iteration.
            maximums.append(integers[idx_queue[0]])  # Queue's 1st idx always points to window maximum.
        current_idx += 1
