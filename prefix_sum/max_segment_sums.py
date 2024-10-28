import heapq


def _binary_search(target: int, sorted_integers: list[int], size: int) -> int:
    if size == 0:
        return 0

    back_idx, front_idx = 0, size - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_integers[mid_idx] < target:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of ints < target.


def collect_max_segment_sums(numbers: list[int], queries: list[int]) -> list[int]:  # LeetCode Q.2382.
    total_numbers = len(numbers)
    if total_numbers == 1:  # Base case.
        return [0]

    prefix_sums = []
    for number in numbers:
        if not prefix_sums:
            prefix_sums.append(number)
            continue
        prefix_sums.append(prefix_sums[-1] + number)

    max_segment_sums = []
    max_heap = []  # Format: (negated segment sum, sum's range).

    ranges2sums = {f"0:{total_numbers - 1}": prefix_sums[-1]}
    removed_indices, removals = [], 0

    for removal_idx in queries:
        insertion_idx = _binary_search(removal_idx, removed_indices, removals)
        if insertion_idx == removals:  # All removed indices < removal idx.
            right_idx = total_numbers - 1

        else:
            right_idx = removed_indices[insertion_idx] - 1

        if insertion_idx == 0:  # Removal idx < all removed indices.
            left_idx = 0

        else:
            left_idx = removed_indices[insertion_idx - 1] + 1

        del ranges2sums[f"{left_idx}:{right_idx}"]  # No longer existing segment.

        if removal_idx < total_numbers - 1:  # A new right segment sum appears.
            right_segment_sum = prefix_sums[right_idx] - prefix_sums[removal_idx]
            ranges2sums.update(
                {f"{removal_idx + 1}:{right_idx}": right_segment_sum}
            )
            heapq.heappush(  # Negate sum to fit into max heap.
                max_heap, (-right_segment_sum, f"{removal_idx + 1}:{right_idx}")
            )

        if removal_idx > 0:  # A new left segment sum appears.
            left_segment_sum = prefix_sums[removal_idx - 1]
            if left_idx > 0:
                left_segment_sum -= prefix_sums[left_idx - 1]

            ranges2sums.update(
                {f"{left_idx}:{removal_idx - 1}": left_segment_sum}
            )
            heapq.heappush(  # Negate sum to fit into max heap.
                max_heap, (-left_segment_sum, f"{left_idx}:{removal_idx - 1}")
            )

        while max_heap[0][1] not in ranges2sums.keys():
            heapq.heappop(max_heap)
        max_segment_sums.append(-max_heap[0][0])  # Negate sum back to original value.

        removed_indices.insert(insertion_idx, removal_idx)
        removals += 1

    return max_segment_sums
