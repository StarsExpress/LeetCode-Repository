import heapq


def maximize_capital(k: int, wealth: int, profits: list[int], capitals: list[int]) -> int:  # LeetCode 502.
    """Select at most k distinct projects to maximize wealth."""
    capitals_profits: list[tuple[int, int]] = [
        (iter_capital, profit) for iter_capital, profit in zip(capitals, profits)
    ]
    capitals_profits.sort()

    profits_heap = []
    while k > 0 and (capitals_profits or profits_heap):
        while capitals_profits and wealth >= capitals_profits[0][0]:
            # Negate profit to fit into max heap.
            heapq.heappush(profits_heap, -capitals_profits.pop(0)[1])

        if not profits_heap:  # All remaining projects are unaffordable.
            break

        wealth -= heapq.heappop(profits_heap)  # Negate profit back.
        k -= 1

    return wealth
