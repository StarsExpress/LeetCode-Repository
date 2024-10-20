
def _binary_search(index: int, sorted_indices: list[int]) -> int:
    if not sorted_indices:
        return 0

    back_idx, front_idx = 0, len(sorted_indices) - 1
    while back_idx <= front_idx:
        mid_idx = (back_idx + front_idx) // 2
        if sorted_indices[mid_idx] < index:
            back_idx = mid_idx + 1
            continue
        front_idx = mid_idx - 1

    return back_idx  # Number of indices < target idx, implying insertion idx.


def count_subarrays(numbers: list[int]) -> int:  # LeetCode Q.3113.
    """
    Count subarrays where subarrays' max number is on both boundaries.
    Key is to find each number's "latest left side" bigger num. Iteration goes in reverse.
    """
    total_numbers = len(numbers)
    latest_greater_indices = [-1] * total_numbers
    stack = [(-1, numbers[-1])]  # Decreasing monotonic stack: (idx, num).

    for current_idx in range(total_numbers - 2, -1, -1):
        while stack and stack[-1][1] < numbers[current_idx]:  # Latest found.
            future_idx, _ = stack.pop(-1)
            latest_greater_indices[future_idx] = current_idx

        stack.append((current_idx, numbers[current_idx]))

    indices_table = dict()  # Track each number's occurred indices.
    for idx, num in enumerate(numbers):
        if num not in indices_table.keys():
            indices_table.update({num: []})
        indices_table[num].append(idx)

    total_subarrays = 0
    for idx, num in enumerate(numbers):
        # From start_idx to idx, find how many times num occurs.
        # This counts all valid subarrays ending at idx.

        start_idx = 0  # No last greater.
        if latest_greater_indices[idx] != -1:  # Latest greater exists.
            start_idx += latest_greater_indices[idx] + 1

        insertion_idx_1 = _binary_search(start_idx, indices_table[num])
        insertion_idx_2 = _binary_search(idx, indices_table[num])
        total_subarrays += insertion_idx_2 - insertion_idx_1 + 1

    return total_subarrays
