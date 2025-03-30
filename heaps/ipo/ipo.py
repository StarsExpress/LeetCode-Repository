import heapq


def maximize_capital(k: int, wealth: int, profits: list[int], capitals: list[int]) -> int:  # LeetCode 502.
    """Select at most k distinct projects to maximize wealth."""
    capitals_heap: list[tuple[int, int]] = []  # Min heap. Format: (capital, idx).
    for idx, iter_capital in enumerate(capitals):
        heapq.heappush(capitals_heap, (iter_capital, idx))

    profits_heap = []  # Max heap.
    while k > 0:
        while capitals_heap and wealth >= capitals_heap[0][0]:
            idx = heapq.heappop(capitals_heap)[1]
            heapq.heappush(profits_heap, -profits[idx])  # Negate profit to fit into max heap.

        if not profits_heap:
            break
        wealth -= heapq.heappop(profits_heap)  # Negate profit back to original value.
        k -= 1

    return wealth
