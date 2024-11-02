
def _binary_search(target: int, sorted_indices: list[int], size: int) -> int:
    if size == 0:
        return 0

    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_indices[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of indices < target.

def count_max_partitions(numbers: list[int], k: int) -> int:  # LeetCode Q.2025.
    original_sum, max_partition_ways = sum(numbers), 0
    prefix_sums2indices, prefix_sum = dict(), 0

    # Can't partition at the last num (doesn't have a right neighbor).
    for idx, num in enumerate(numbers[:-1]):
        prefix_sum += num
        if prefix_sum not in prefix_sums2indices.keys():
            prefix_sums2indices.update({prefix_sum: []})
        prefix_sums2indices[prefix_sum].append(idx)

        if 2 * prefix_sum == original_sum:  # Base case: all numbers unchanged.
            max_partition_ways += 1

    for idx, num in enumerate(numbers):
        new_sum = original_sum + k - num
        if new_sum % 2 == 0:  # Only "even" new sum can work!
            right_side_count = 0
            right_side_prefix_sum = new_sum // 2 + num - k

            if right_side_prefix_sum in prefix_sums2indices.keys():
                indices = prefix_sums2indices[right_side_prefix_sum]
                total_count = len(indices)
                smaller_count = _binary_search(idx, indices, total_count)
                right_side_count += total_count - smaller_count

            left_side_count = 0
            left_side_prefix_sum = new_sum // 2

            if left_side_prefix_sum in prefix_sums2indices.keys():
                indices = prefix_sums2indices[left_side_prefix_sum]
                left_side_count += _binary_search(idx, indices, len(indices))

            if left_side_count + right_side_count > max_partition_ways:
                max_partition_ways = left_side_count + right_side_count

    return max_partition_ways
