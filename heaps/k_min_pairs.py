import heapq


def find_k_min_pairs(nums_1: list[int], nums_2: list[int], k: int) -> list[list[int]]:  # LeetCode Q.373.
    total_nums_1, total_nums_2 = len(nums_1), len(nums_2)
    pairs: list[list[int]] = []
    min_heap = [(nums_1[0] + nums_2[0], 0, 0)]  # (Sum, int 1's list idx, int 2's list idx).
    while min_heap and 0 < k:
        _, idx_1, idx_2 = heapq.heappop(min_heap)
        pairs.append([nums_1[idx_1], nums_2[idx_2]])
        k -= 1

        if idx_2 == 0 and idx_1 + 1 < total_nums_1:
            heapq.heappush(min_heap, (nums_1[idx_1 + 1] + nums_2[idx_2], idx_1 + 1, idx_2))

        if idx_2 + 1 < total_nums_2:
            heapq.heappush(min_heap, (nums_1[idx_1] + nums_2[idx_2 + 1], idx_1, idx_2 + 1))

    return pairs
