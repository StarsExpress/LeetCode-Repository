
def find_largest_rectangle(heights: list[int]) -> int:  # LeetCode Q.84.
    heights_count = len(heights)
    next_smaller_indices: list[int | None] = [None] * heights_count
    stack = [(0, heights[0])]

    for current_idx in range(1, heights_count):
        # Past height > current height: next smaller found.
        while stack and stack[-1][1] > heights[current_idx]:
            past_idx, _ = stack.pop(-1)
            next_smaller_indices[past_idx] = current_idx

        stack.append((current_idx, heights[current_idx]))

    previous_smaller_indices: list[int | None] = [None] * heights_count
    stack.clear()
    stack.append((heights_count - 1, heights[-1]))

    for current_idx in range(heights_count - 2, -1, -1):  # Backward iteration.
        # Future height > current height: previous smaller found.
        while stack and stack[-1][1] > heights[current_idx]:
            past_idx, _ = stack.pop(-1)
            previous_smaller_indices[past_idx] = current_idx

        stack.append((current_idx, heights[current_idx]))

    largest_rectangle = -float("inf")
    for idx, height in enumerate(heights):
        width = 1  # Each height has width of 1.

        next_smaller_idx = next_smaller_indices[idx]
        if next_smaller_idx is None:  # All the way to the rightmost height.
            width += heights_count - 1 - idx

        else:  # All the way to (next smaller idx - 1)th height.
            width += next_smaller_idx - 1 - idx

        previous_smaller_idx = previous_smaller_indices[idx]
        if previous_smaller_idx is None:  # All the way to the leftmost height.
            width += idx

        else:  # All the way to (previous smaller idx + 1)th height.
            width += idx - 1 - previous_smaller_idx

        rectangle = height * width
        if rectangle > largest_rectangle:
            largest_rectangle = rectangle

    return largest_rectangle
