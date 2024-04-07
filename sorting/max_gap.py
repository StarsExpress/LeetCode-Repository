from sorting.radix_sort import RadixSort


def find_max_gap(integers: list[int]):  # LeetCode Q.164.
    if len(integers) < 2:
        return 0

    radix_sort = RadixSort(integers)  # Radix sort has linear time complexity.
    integers = radix_sort.sort()

    current_idx, current_gap, max_gap = 0, 0, 0
    while True:
        if current_idx >= len(integers) - 1:
            return max(current_gap, max_gap)

        current_gap += integers[current_idx + 1] - integers[current_idx] - current_gap
        if current_gap > max_gap:
            max_gap += current_gap - max_gap

        current_idx += 1
