
def find_longest_length(numbers: list[int]) -> int:  # LeetCode Q.525.
    max_len, prefix_sum, sums2indices_table = 0, 0, dict()
    for idx, number in enumerate(numbers):
        if number == 0:
            prefix_sum -= 1

        else:
            prefix_sum += 1

        if prefix_sum not in sums2indices_table.keys():
            sums2indices_table.update({prefix_sum: idx})

        if prefix_sum == 0:  # nums[:idx + 1] has equal number of 0 and 1.
            max_len = idx + 1
            continue

        if prefix_sum in sums2indices_table.keys():
            # nums[start_idx: idx + 1] has equal number of 0 and 1.
            start_idx = sums2indices_table[prefix_sum] + 1
            interval_len = idx + 1 - start_idx
            if interval_len > max_len:
                max_len = interval_len

    return max_len
