
def count_subarrays(nums: list[int]) -> int:  # LeetCode Q.3113.
    nums2indices: dict[int, list[int]] = dict()

    prev_bigger_indices: list[int] = [-1] * len(nums)
    decreasing_stack: list[tuple[int, int]] = []  # Format: (idx, num).

    subarrays_count = 0

    for idx, num in enumerate(nums):
        if num not in nums2indices.keys():
            nums2indices.update({num: []})
        nums2indices[num].append(idx)

        while decreasing_stack and decreasing_stack[-1][1] <= num:
            decreasing_stack.pop()

        if decreasing_stack:
            prev_bigger_indices[idx] = decreasing_stack[-1][0]

        decreasing_stack.append((idx, num))

        while nums2indices[num][0] < prev_bigger_indices[idx]:
            nums2indices[num].pop(0)

        subarrays_count += len(nums2indices[num])

    return subarrays_count
