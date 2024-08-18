
def count_bounded_subarrays(numbers: list[int], minimum: int, maximum: int):  # LeetCode Q.2444.
    if not {minimum, maximum}.issubset(set(numbers)):
        return 0

    valid_ranges, current_range = [], []
    while numbers:
        if numbers[0] < minimum or numbers[0] > maximum:  # Reset happens.
            valid_ranges.append(current_range.copy())  # Copy to prevent modification.
            current_range.clear()
            numbers.pop(0)
            continue

        current_range.append(numbers.pop(0))

    valid_ranges.append(current_range)  # Don't forget last piece of range.

    total_count = 0
    range_counts = []  # Subarray counts at each idx in a valid range.
    while valid_ranges:
        valid_range = valid_ranges.pop(0)
        if minimum == maximum:  # Special case: min = max.
            total_count += (1 + len(valid_range)) * len(valid_range) // 2
            continue

        last_min_idx, last_max_idx = None, None  # Last occurred indices of min & max in a valid range.
        for idx, num in enumerate(valid_range):
            if idx == 0:  # 1st num of valid range.
                range_counts.append(0)
                if num == minimum:
                    last_min_idx = idx
                if num == maximum:
                    last_max_idx = idx
                continue

            range_counts.append(range_counts[-1])  # All indices can directly inherit count of last idx.

            if num == minimum:
                # Min & max now both occur.
                if last_max_idx is not None and last_min_idx is None:
                    range_counts[-1] += last_max_idx + 1

                # Min & max have already occurred.
                if last_min_idx is not None and last_max_idx is not None:
                    if last_min_idx < last_max_idx:
                        range_counts[-1] += last_max_idx - last_min_idx

                last_min_idx = idx

            if num == maximum:
                # Min & max now both occur.
                if last_min_idx is not None and last_max_idx is None:
                    range_counts[-1] += last_min_idx + 1

                # Min & max have already occurred.
                if last_min_idx is not None and last_max_idx is not None:
                    if last_max_idx < last_min_idx:
                        range_counts[-1] += last_min_idx - last_max_idx

                last_max_idx = idx

            total_count += range_counts[-1]

        range_counts.clear()  # Reset for next valid range.

    return total_count
