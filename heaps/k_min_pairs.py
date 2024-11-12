import heapq


def find_k_min_pairs(integers_1: list[int], integers_2: list[int], k: int) -> list[list[int]]:  # LeetCode Q.373.
    integers_1_len, integers_2_len = len(integers_1), len(integers_2)
    pairs = []
    queue = [(integers_1[0] + integers_2[0], 0, 0)]  # (Sum, int 1's list idx, int 2's list idx).
    while queue and len(pairs) < k:
        _, idx_1, idx_2 = heapq.heappop(queue)
        pairs.append([integers_1[idx_1], integers_2[idx_2]])

        if idx_2 == 0 and idx_1 + 1 < integers_1_len:
            heapq.heappush(queue, (integers_1[idx_1 + 1] + integers_2[idx_2], idx_1 + 1, idx_2))

        if idx_2 + 1 < integers_2_len:
            heapq.heappush(queue, (integers_1[idx_1] + integers_2[idx_2 + 1], idx_1, idx_2 + 1))

    return pairs
