
def find_largest_rectangle(heights: list[int]) -> int:  # LeetCode Q.84.
    prev_smaller_indices: list[int] = [-1] * len(heights)

    largest_rectangle = 0

    prev_stack, next_stack = [], []  # Format: (height, idx).

    for idx, height in enumerate(heights):
        while prev_stack and prev_stack[-1][0] >= height:
            prev_stack.pop(-1)

        if prev_stack:
            past_idx = prev_stack[-1][1]
            prev_smaller_indices[idx] = past_idx

        prev_stack.append((height, idx))

        while next_stack and next_stack[-1][0] > height:
            past_idx = next_stack.pop(-1)[1]

            width = idx - prev_smaller_indices[past_idx] - 1

            rectangle = heights[past_idx] * width
            if rectangle > largest_rectangle: largest_rectangle = rectangle

        next_stack.append((height, idx))

    while next_stack:
        idx = next_stack.pop(-1)[1]
        width = len(heights) - prev_smaller_indices[idx] - 1

        rectangle = heights[idx] * width
        if rectangle > largest_rectangle: largest_rectangle = rectangle

    return largest_rectangle
