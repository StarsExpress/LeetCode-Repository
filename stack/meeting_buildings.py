
def query_meeting_buildings(heights: list[int], queries: list[list[int]]) -> list[int]:  # LeetCode Q.2940.
    common_building_indices = [-1] * len(queries)

    queries = [
        (query_idx, min(alice_idx, bob_idx), max(alice_idx, bob_idx))
        for query_idx, (alice_idx, bob_idx) in enumerate(queries)
    ]
    # Sort queries by descending max(Alice's idx, Bob's idx).
    queries.sort(key=lambda x: -max(x[1], x[2]))

    # Height decreasing monotonic stack. Format: (height, idx).
    stack = [(heights[-1], len(heights) - 1)]

    for query_idx, left_idx, right_idx in queries:
        if left_idx == right_idx or heights[left_idx] < heights[right_idx]:
            common_building_indices[query_idx] = right_idx
            continue

        while stack and stack[-1][1] > right_idx + 1:
            new_idx = stack[-1][1] - 1
            while stack and heights[new_idx] >= stack[-1][0]:
                stack.pop(-1)

            stack.append((heights[new_idx], new_idx))

        front_idx, back_idx = 0, len(stack) - 1
        while front_idx <= back_idx:
            mid_idx = (front_idx + back_idx) // 2
            if stack[mid_idx][0] <= heights[left_idx]:
                back_idx = mid_idx - 1
                continue
            front_idx = mid_idx + 1

        if front_idx > 0:
            common_building_indices[query_idx] = stack[front_idx - 1][1]

    return common_building_indices
