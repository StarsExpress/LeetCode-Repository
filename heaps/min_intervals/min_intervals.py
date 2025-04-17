import heapq


def find_min_intervals(intervals: list[list[int]], queries: list[int]) -> list[int]:  # LeetCode Q.1851.
    starts_sizes_heap = []  # Min heap. Format: (interval start, size).
    sizes_ends_heap = []  # Min heap. Format: (size, interval end).

    for start, end in intervals:
        heapq.heappush(starts_sizes_heap, (start, end + 1 - start))

    queries_indices = []  # Format: (query num, query idx).
    for query_idx, query_num in enumerate(queries):
        queries_indices.append((query_num, query_idx))

    queries_indices.sort()  # Sort by ascending query nums.

    answers = [-1] * len(queries)  # Default to -1.
    for query_num, query_idx in queries_indices:
        while starts_sizes_heap and starts_sizes_heap[0][0] <= query_num:
            start, size = starts_sizes_heap[0]
            heapq.heappush(sizes_ends_heap, (size, start + size - 1))  # Format: (size, interval end).
            heapq.heappop(starts_sizes_heap)

        while sizes_ends_heap and sizes_ends_heap[0][1] < query_num:
            heapq.heappop(sizes_ends_heap)

        if sizes_ends_heap:
            answers[query_idx] = sizes_ends_heap[0][0]

    return answers
