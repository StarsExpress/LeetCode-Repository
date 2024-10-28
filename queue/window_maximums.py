
def find_window_maximums(integers: list[int], window_size: int) -> list[int]:  # LeetCode Q.239.
    if window_size == 1:
        return integers

    window_maximums = []
    # Queue contains indices of ints under current sliding window.
    queue = [0]  # Leftmost idx always points to window maximum.
    for idx, integer in enumerate(integers):
        if idx > 0:  # Int at 0th idx is automatically into queue.
            # Ensure last idx's int > current int.
            while queue and integers[queue[-1]] <= integer:
                queue.pop(-1)

            # Ensure leftmost idx is in window.
            while queue and idx - window_size + 1 > queue[0]:
                queue.pop(0)

            queue.append(idx)
            if idx >= window_size - 1:  # When 1st k ints have all been "seen".
                window_maximums.append(integers[queue[0]])

    return window_maximums
