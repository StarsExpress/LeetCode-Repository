
def find_valid_subarray_size(nums: list[int], threshold: int) -> int:  # LeetCode Q.2334.
    prev_smaller_indices = [-1] * len(nums)
    next_smaller_indices = [len(nums)] * len(nums)

    prev_stack, next_stack = [], []  # Format: (num, idx).
    for idx, num in enumerate(nums):
        while prev_stack and prev_stack[-1][0] >= num:
            prev_stack.pop(-1)

        if prev_stack:
            past_idx = prev_stack[-1][1]
            prev_smaller_indices[idx] = past_idx

        prev_stack.append((num, idx))

        while next_stack and next_stack[-1][0] > num:
            past_idx = next_stack.pop(-1)[1]
            next_smaller_indices[past_idx] = idx

        next_stack.append((num, idx))

    for idx, num in enumerate(nums):
        width = 1
        width += next_smaller_indices[idx] - 1 - idx
        width += idx - 1 - prev_smaller_indices[idx]

        if num > threshold / width:
            return width

    return -1
