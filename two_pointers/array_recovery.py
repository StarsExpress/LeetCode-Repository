
def recover_array(nums: list[int]) -> list[int]:  # LeetCode Q.2122.
    total_nums = len(nums)
    if total_nums == 2:  # Base case.
        return [sum(nums) // 2]

    original_array_len = total_nums // 2

    nums.sort()
    valid_high_array_mins = []
    for idx, num in enumerate(nums[:original_array_len + 1]):
        if (num - nums[0]) % 2 == 0 and num > nums[0]:
            valid_high_array_mins.append((idx, num, num - nums[0]))

    original_array, used_indices = [], set()
    for valid_idx, valid_min, valid_diff in valid_high_array_mins:
        original_array.append((nums[0] + valid_min) // 2)
        used_indices.update({0, valid_idx})

        back_idx, front_idx = 1, valid_idx + 1
        while True:
            while back_idx in used_indices:
                back_idx += 1

            while front_idx in used_indices:
                front_idx += 1

            if front_idx >= total_nums:
                break

            if nums[front_idx] - nums[back_idx] == valid_diff:
                original_array.append(
                    (nums[front_idx] + nums[back_idx]) // 2
                )

                used_indices.add(back_idx)
                used_indices.add(front_idx)
                back_idx += 1

            front_idx += 1

        if len(original_array) == original_array_len:
            break

        original_array.clear()
        used_indices.clear()

    return original_array
