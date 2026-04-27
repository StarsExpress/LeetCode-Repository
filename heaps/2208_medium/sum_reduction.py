import heapq


def halve_array_sum(numbers: list[int]) -> int:  # LeetCode Q.2208.
    max_heap = []
    for number in numbers:
        heapq.heappush(max_heap, -number)  # Negate number to fit max heap.

    array_sum, operations = sum(numbers), 0
    target_sum = array_sum / 2
    while array_sum > target_sum:
        current_max = -heapq.heappop(max_heap)  # Negate number back to original value.
        current_max /= 2
        array_sum -= current_max
        heapq.heappush(max_heap, -current_max)  # Negate number to fit max heap.
        operations += 1

    return operations
