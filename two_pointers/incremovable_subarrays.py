
def count_incremovable_subarrays(numbers: list[int]) -> int:  # LeetCode Q.2972.
    total_numbers = len(numbers)
    max_prefix_end_idx = total_numbers - 1
    for idx in range(1, total_numbers):
        if numbers[idx] <= numbers[idx - 1]:
            max_prefix_end_idx = idx - 1
            break

    min_suffix_start_idx = 0
    for idx in range(total_numbers - 1, 0, -1):
        if numbers[idx] <= numbers[idx - 1]:
            min_suffix_start_idx = idx
            break

    incremovable_subarrays = 1  # Can always delete the entire original array.
    suffix_start_idx = min_suffix_start_idx
    for prefix_end_idx in range(max_prefix_end_idx + 1):
        while suffix_start_idx < total_numbers - 1 and numbers[prefix_end_idx] >= numbers[suffix_start_idx]:
            suffix_start_idx += 1

        if numbers[prefix_end_idx] < numbers[suffix_start_idx]:
            incremovable_subarrays += total_numbers + 1 - suffix_start_idx
            continue

        if prefix_end_idx < total_numbers - 1:  # Can't delete an empty subarray.
            incremovable_subarrays += 1

    if min_suffix_start_idx > 0:  # When original array isn't strictly increasing.
        incremovable_subarrays += total_numbers - min_suffix_start_idx

    return incremovable_subarrays
