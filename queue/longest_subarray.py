
def find_longest_subarray(integers: list[int], limit: int):  # LeetCode Q.1438.
    current_len, max_len = 1, 1  # Base case: subarray of only 1st number.
    min_idx_queue, max_idx_queue = [0], [0]

    for idx, newcomer in enumerate(integers):
        if idx == 0:  # Base case is already finished.
            continue

        # Ensure last idx's corresponding int < current int.
        while min_idx_queue and integers[min_idx_queue[-1]] >= newcomer:
            min_idx_queue.pop(-1)

        min_idx_queue.append(idx)

        # Ensure last idx's corresponding int > current int.
        while max_idx_queue and integers[max_idx_queue[-1]] <= newcomer:
            max_idx_queue.pop(-1)

        max_idx_queue.append(idx)

        # Newcomer doesn't cause limit explosion.
        if integers[max_idx_queue[0]] - integers[min_idx_queue[0]] <= limit:
            current_len += 1  # Update current subarray length.
            continue

        # Newcomer causes limit explosion.
        if current_len > max_len:  # Current len doesn't contain newcomer yet.
            max_len = current_len

        if idx == min_idx_queue[0]:  # Newcomer is current subarray min.
            new_subarray_start_idx = 0
            while max_idx_queue and integers[max_idx_queue[0]] - newcomer > limit:
                new_subarray_start_idx = max_idx_queue.pop(0) + 1

            if max_idx_queue:
                current_len = idx + 1 - new_subarray_start_idx

            else:  # New subarray has only newcomer itself.
                current_len = 1

            continue

        # Newcomer is current subarray max.
        new_subarray_start_idx = 0
        while min_idx_queue and newcomer - integers[min_idx_queue[0]] > limit:
            new_subarray_start_idx = min_idx_queue.pop(0) + 1

        if min_idx_queue:
            current_len = idx + 1 - new_subarray_start_idx

        else:  # New subarray has only newcomer itself.
            current_len = 1

    return max(max_len, current_len)
