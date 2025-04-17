import heapq
from bisect import bisect_right


def query_closest_rooms(rooms: list[list[int]], queries: list[list[int]]) -> list[int]:  # LeetCode Q.1847.
    # Max heap. Format: (negative min size, preferred ID, idx).
    queries_heap = []
    for idx, (preferred_id, min_size) in enumerate(queries):
        # Negate min size to fit into max heap.
        heapq.heappush(queries_heap, (-min_size, preferred_id, idx))

    # Max heap. Format: (negative room size, room ID).
    rooms_heap = []
    for room_id, room_size in rooms:
        # Negate room size to fit into max heap.
        heapq.heappush(rooms_heap, (-room_size, room_id))

    ids_pool: list[int] = []
    closest_rooms: list[int] = [-1] * len(queries)  # Default to no matching rooms.
    while queries_heap:
        min_size, preferred_id, query_idx = heapq.heappop(queries_heap)
        min_size = -min_size  # Negate value back.

        while rooms_heap and -rooms_heap[0][0] >= min_size:  # Negate room size.
            room_id = heapq.heappop(rooms_heap)[1]
            idx = bisect_right(ids_pool, room_id)
            ids_pool.insert(idx, room_id)

        if ids_pool:
            idx = bisect_right(ids_pool, preferred_id)
            if idx == 0:
                closest_rooms[query_idx] = ids_pool[0]
                continue
            if idx == len(ids_pool):
                closest_rooms[query_idx] = ids_pool[-1]
                continue

            left_diff = preferred_id - ids_pool[idx - 1]
            right_diff = ids_pool[idx] - preferred_id
            if left_diff <= right_diff:  # Tie: choose the min matching ID.
                closest_rooms[query_idx] = ids_pool[idx - 1]

            else:
                closest_rooms[query_idx] = ids_pool[idx]

    return closest_rooms
