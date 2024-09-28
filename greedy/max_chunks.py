
def find_max_sortable_chunks(array: list[int]) -> int:  # LeetCode Q.768 & 769.
    prefix_subarrays_maxs = []  # Max of each prefix subarray[:ith idx].
    for number in array[:-1]:  # Forward iteration skips the last number.
        if not prefix_subarrays_maxs:  # 1st number of the original array.
            prefix_subarrays_maxs.append(number)
            continue

        prefix_subarrays_maxs.append(
            max(number, prefix_subarrays_maxs[-1])
        )

    current_idx, separation_idx = -1, None
    suffix_subarray_min = float("inf")  # Min of current suffix subarray[ith idx:].
    for number in array[::-1][:-1]:  # Backward iteration skips the 1st number.
        if number < suffix_subarray_min:
            suffix_subarray_min = number
        if prefix_subarrays_maxs[current_idx] <= suffix_subarray_min:
            separation_idx = current_idx  # A better separation idx to shorten prefix subarray.

        current_idx -= 1

    if not separation_idx:  # Can't split the original array at all.
        return 1

    # Fixed chunk 1: subarray from 0th idx to (separation idx - 1)th.
    # Unknown chunk 2: recursion on subarray from (separation idx)th to the end.
    return 1 + find_max_sortable_chunks(array[separation_idx:])
