
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

    return back_idx  # Numbers < target, implying insertion idx.


def find_smallest_containing_set(intervals: list[list[int]]) -> int:  # LeetCode Q.757.
    # Key: deal with more "interior-located" and smaller intervals first.
    intervals.sort(key=lambda x: (x[1], -x[0]))  # Sort by rising end and falling start.
    containing_set, set_size = [], 0
    for start, end in intervals:
        start_idx = _binary_search(start, containing_set, set_size)
        if start_idx == set_size:  # Containing set's nums all < start.
            containing_set.extend([end - 1, end])  # Add the biggest two nums of interval.
            set_size += 2
            continue

        end_idx = _binary_search(end, containing_set, set_size)
        if start_idx + 2 > end_idx:  # Set likely doesn't have 2+ nums within interval.
            if end_idx == set_size:  # Containing set's nums all < end.
                containing_set.append(end)
                set_size += 1

            if end < containing_set[end_idx]:  # Num at set's end_idx < end.
                containing_set.insert(end_idx, end)
                set_size += 1

    return set_size
