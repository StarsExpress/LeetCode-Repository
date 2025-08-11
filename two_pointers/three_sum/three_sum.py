
def find_3_sum(nums: list[int | float]):  # LeetCode Q.15.
    nums.sort()
    distinct_triplets: list[list[int]] = []

    min_idx_2, idx_3 = 1, len(nums) - 1
    while idx_3 > min_idx_2:
        if idx_3 < len(nums) - 1 and nums[idx_3] == nums[idx_3 + 1]:
            idx_3 -= 1
            continue

        while nums[min_idx_2 - 1] + nums[min_idx_2] + nums[idx_3] < 0:
            min_idx_2 += 1
            if min_idx_2 == idx_3:
                break

        idx_1 = min_idx_2 - 1
        for idx_2 in range(min_idx_2, idx_3):
            if idx_1 < 0:
                break
            if min_idx_2 < idx_2 and nums[idx_2 - 1] == nums[idx_2]:
                continue

            target_num_1 = -nums[idx_3] - nums[idx_2]
            while idx_1 >= 0:
                if nums[idx_1] < target_num_1:
                    break

                if nums[idx_1] == target_num_1:
                    distinct_triplets.append([nums[idx_1], nums[idx_2], nums[idx_3]])
                    # If idx_1, idx_2, idx_3 and idx_1, idx_2 + 1, idx_3 are answers, take the former.
                    idx_1 -= 1  # Prevent idx_2 + 1 from pairing w/ idx_1.
                    break

                idx_1 -= 1

        idx_3 -= 1

    return distinct_triplets
