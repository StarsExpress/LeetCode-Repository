
def find_valid_subarray_size(numbers: list[int], threshold: int) -> int:  # LeetCode Q.2334.
    if max(numbers) > threshold:  # Base case.
        return 1

    total_nums = len(numbers)
    next_smaller_indices: list[int | None] = [None] * total_nums
    stack = [(0, numbers[0])]

    for current_idx in range(1, total_nums):
        # Past num > current num: next smaller found.
        while stack and stack[-1][1] > numbers[current_idx]:
            past_idx, _ = stack.pop(-1)
            next_smaller_indices[past_idx] = current_idx

        stack.append((current_idx, numbers[current_idx]))

    previous_smaller_indices: list[int | None] = [None] * total_nums
    stack.clear()
    stack.append((total_nums - 1, numbers[total_nums - 1]))

    for current_idx in range(total_nums - 2, -1, -1):  # Backward iteration.
        # Future num > current num: previous smaller found.
        while stack and stack[-1][1] > numbers[current_idx]:
            past_idx, _ = stack.pop(-1)
            previous_smaller_indices[past_idx] = current_idx

        stack.append((current_idx, numbers[current_idx]))

    for idx, num in enumerate(numbers):
        width = 1  # Each num starts from width of 1 (subarray of only itself).

        next_smaller_idx = next_smaller_indices[idx]
        if next_smaller_idx is None:  # All the way to the rightmost num.
            width += total_nums - 1 - idx

        else:  # All the way to (next smaller idx - 1)th num.
            width += next_smaller_idx - 1 - idx

        previous_smaller_idx = previous_smaller_indices[idx]
        if previous_smaller_idx is None:  # All the way to the leftmost num.
            width += idx

        else:  # All the way to (previous smaller idx + 1)th num.
            width += idx - 1 - previous_smaller_idx

        if num > threshold / width:
            return width

    return -1
