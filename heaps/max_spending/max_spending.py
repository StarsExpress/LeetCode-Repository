import heapq


def maximize_spending(values: list[list[int]]) -> int:  # LeetCode Q.2931.
    # Min heap. Format: (item, row idx).
    items_heap: list[tuple[int, int]] = []
    for row_idx in range(len(values)):
        item = values[row_idx].pop(-1)
        heapq.heappush(items_heap, (item, row_idx))

    max_spent_money, day = 0, 1
    while items_heap:
        item, row_idx = heapq.heappop(items_heap)
        max_spent_money += item * day
        day += 1

        if values[row_idx]:
            new_item = values[row_idx].pop(-1)
            heapq.heappush(items_heap, (new_item, row_idx))

    return max_spent_money
