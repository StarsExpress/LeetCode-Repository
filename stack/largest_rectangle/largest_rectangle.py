
def find_largest_rectangle(heights: list[int]) -> int:  # LeetCode Q.84.
    prev_smaller_indices: list[int] = [-1] * len(heights)
    next_smaller_indices: list[int] = [len(heights)] * len(heights)

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
            next_smaller_indices[past_idx] = idx

        next_stack.append((height, idx))

    largest_rectangle = 0
    for idx, height in enumerate(heights):
        width = 1
        width += next_smaller_indices[idx] - 1 - idx
        width += idx - 1 - prev_smaller_indices[idx]

        rectangle = height * width
        if rectangle > largest_rectangle:
            largest_rectangle = rectangle

    return largest_rectangle
