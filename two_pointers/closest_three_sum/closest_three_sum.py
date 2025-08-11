
def find_closest_three_sum(nums: list[int], target: int) -> int:  # LeetCode Q.16.
    nums.sort()
    min_gap, closest_3_sum = float("inf"), 0

    min_idx_2, idx_3 = 1, len(nums) - 1
    while idx_3 > min_idx_2:
        while min_idx_2 < idx_3 and nums[min_idx_2 - 1] + nums[min_idx_2] + nums[idx_3] < target:
            min_idx_2 += 1

        if min_idx_2 >= 2:
            last_three_sum = nums[min_idx_2 - 2] + nums[min_idx_2 - 1] + nums[idx_3]
            gap = abs(last_three_sum - target)
            if gap < min_gap:
                min_gap, closest_3_sum = gap, last_three_sum

        idx_1 = min_idx_2 - 1
        for idx_2 in range(min_idx_2, idx_3):
            if idx_1 < 0:
                break

            two_sum = nums[idx_2] + nums[idx_3]  # Sum of nums 2 and 3.
            while idx_1 >= 0:
                if idx_1 == 0 or nums[idx_1] + two_sum < target:
                    three_sum_1 = nums[idx_1 + 1] + two_sum
                    gap_1 = abs(three_sum_1 - target)
                    three_sum_2 = nums[idx_1] + two_sum
                    gap_2 = abs(three_sum_2 - target)

                    if min(gap_1, gap_2) < min_gap:
                        if gap_1 < gap_2:
                            min_gap, closest_3_sum = gap_1, three_sum_1

                        else:
                            min_gap, closest_3_sum = gap_2, three_sum_2
                    break

                idx_1 -= 1

        idx_3 -= 1

    return closest_3_sum
