
def sum_max_min_subarrays(nums: list[int], k: int) -> int:
    decreasing_stack: list[tuple[int, int]] = []  # Format: (num, idx).
    increasing_stack: list[tuple[int, int]] = []  # Format: (num, idx).

    total_nums = len(nums)
    max_span_indices: list[list[int]] = [
        [0, total_nums - 1] for _ in range(total_nums)
    ]
    min_span_indices: list[list[int]] = [
        [0, total_nums - 1] for _ in range(total_nums)
    ]

    max_min_sum = 0

    for idx, num in enumerate(nums):
        while decreasing_stack and decreasing_stack[-1][1] + k - 1 >= idx:
            if decreasing_stack[-1][0] >= num:
                max_span_indices[idx][0] = decreasing_stack[-1][1]
                if decreasing_stack[-1][0] > num:
                    max_span_indices[idx][0] += 1
                break

            decreasing_stack.pop(-1)

        while increasing_stack and increasing_stack[-1][1] + k - 1 >= idx:
            if increasing_stack[-1][0] <= num:
                min_span_indices[idx][0] = increasing_stack[-1][1]
                if increasing_stack[-1][0] < num:
                    min_span_indices[idx][0] += 1
                break

            increasing_stack.pop(-1)

        decreasing_stack.append((num, idx))
        increasing_stack.append((num, idx))

    decreasing_stack.clear()
    increasing_stack.clear()

    for reverse_idx, num in enumerate(nums[::-1]):
        idx = total_nums - 1 - reverse_idx
        while decreasing_stack and idx + k - 1 >= decreasing_stack[-1][1]:
            if decreasing_stack[-1][0] >= num:
                max_span_indices[idx][1] = decreasing_stack[-1][1]
                if decreasing_stack[-1][1] > num:
                    max_span_indices[idx][1] -= 1
                break
            decreasing_stack.pop(-1)

        while increasing_stack and idx + k - 1 >= increasing_stack[-1][1]:
            if increasing_stack[-1][0] <= num:
                min_span_indices[idx][1] = increasing_stack[-1][1]
                if decreasing_stack[-1][1] < num:
                    min_span_indices[idx][1] -= 1
                break
            increasing_stack.pop(-1)

        max_left_depth = min(idx - max_span_indices[idx][0], k - 1)
        max_right_depth = min(max_span_indices[idx][1] - idx, k - 1)

        max_count = 0
        for l in range(min(max_left_depth, k - 1) + 1):
            max_count += min(max_right_depth, k - 1 - l) + 1

        min_left_depth = min(idx - min_span_indices[idx][0], k - 1)
        min_right_depth = min(min_span_indices[idx][1] - idx, k - 1)

        min_count = 0
        for l in range(min(min_left_depth, k - 1) + 1):
            min_count += min(min_right_depth, k - 1 - l) + 1

        max_min_sum += num * (max_count + min_count)
        print(num, max_count, min_count)

        decreasing_stack.append((num, idx))
        increasing_stack.append((num, idx))

    return max_min_sum


print(sum_max_min_subarrays([16, -6, 19, 19], 4))
