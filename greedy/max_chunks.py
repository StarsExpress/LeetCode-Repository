
def find_max_sortable_chunks(array: list[int]) -> int:  # LeetCode Q.768 & 769.
    prefix_subarrays_maxs = []  # Max of each prefix subarray[:ith idx].
    for number in array[:-1]:  # Forward iteration skips the last number.
        if not prefix_subarrays_maxs:  # 1st number of the original array.
            prefix_subarrays_maxs.append(number)
            continue

        prefix_subarrays_maxs.append(
            max(number, prefix_subarrays_maxs[-1])
        )

    current_idx, separations = -1, 0
    suffix_subarray_min = float("inf")  # Min of current suffix subarray[ith idx:].
    for number in array[::-1][:-1]:  # Backward iteration skips the 1st num.
        if number < suffix_subarray_min:
            suffix_subarray_min = number
        if prefix_subarrays_maxs[current_idx] <= suffix_subarray_min:
            separations += 1

        current_idx -= 1

    separations += 1  # Chunks = Separations + 1.
    return separations
