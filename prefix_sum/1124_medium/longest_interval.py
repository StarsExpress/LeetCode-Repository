
def find_longest_interval(hours: list[int]) -> int:  # LeetCode Q.1124.
    max_interval_len = 0
    prefix_sum, sums2indices_table = 0, dict()
    for idx, hour in enumerate(hours):
        num = 1 if hour > 8 else -1
        prefix_sum += num

        if prefix_sum not in sums2indices_table.keys():
            sums2indices_table.update({prefix_sum: idx})

        if prefix_sum > 0:  # Interval from 1st hour to current hour is well-performing.
            max_interval_len = idx + 1
            continue

        if prefix_sum - 1 in sums2indices_table.keys():
            # Well-performing interval starts at start_idx and ends at idx.
            start_idx = sums2indices_table[prefix_sum - 1] + 1
            interval_len = idx + 1 - start_idx
            if interval_len > max_interval_len:
                max_interval_len = interval_len

    return max_interval_len
