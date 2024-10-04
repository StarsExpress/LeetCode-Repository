import heapq


def verify_possibility(target: list[int]) -> bool:  # LeetCode Q.1354.
    if len(target) == 1:  # Base case: a single num.
        return target[0] == 1

    max_heap, array_sum = [], 0
    for num in target:
        heapq.heappush(max_heap, -num)  # Negate num to fit into max heap.
        array_sum += num

    while max_heap and max_heap[0] < -1:
        num = -heapq.heappop(max_heap)  # Negate num to original sign.
        array_sum -= num
        if array_sum == 1:
            return True

        if num <= array_sum:  # Max num < 1 after deducted by array sum.
            return False

        num %= array_sum
        if num < 1:  # Max num < 1 after deducted by array sum.
            return False

        array_sum += num
        if num > 1:  # Only num > 1 needs to rejoin max heap.
            heapq.heappush(max_heap, -num)  # Negate num to fit into max heap.

    return True
