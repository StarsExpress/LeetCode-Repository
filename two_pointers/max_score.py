
def find_max_score(nums_1: list[int], nums_2: list[int]) -> int:  # LeetCode Q.1537.
    max_score, modulo = 0, 10 ** 9 + 7
    score_1, score_2 = nums_1[0], nums_2[0]
    nums_1_idx, nums_2_idx = 1, 1
    total_nums_1, total_nums_2 = len(nums_1), len(nums_2)

    while nums_1_idx < total_nums_1 or nums_2_idx < total_nums_2:
        # nums1[nums_1_idx - 1]: latest num of nums 1 added into score 1.
        # nums2[nums_1_idx - 1]: latest num of nums 2 added into score 2.
        while nums_1[nums_1_idx - 1] < nums_2[nums_2_idx - 1] and nums_1_idx < total_nums_1:
            score_1 += nums_1[nums_1_idx]
            nums_1_idx += 1

        while nums_2[nums_2_idx - 1] < nums_1[nums_1_idx - 1] and nums_2_idx < total_nums_2:
            score_2 += nums_2[nums_2_idx]
            nums_2_idx += 1

        if nums_1[nums_1_idx - 1] == nums_2[nums_2_idx - 1]:  # Can change paths.
            max_score += max(score_1, score_2) % modulo
            score_1, score_2 = 0, 0  # Reset both sides' scores.
            if nums_1_idx < total_nums_1:
                score_1 += nums_1[nums_1_idx]
                nums_1_idx += 1

            if nums_2_idx < total_nums_2:
                score_2 += nums_2[nums_2_idx]
                nums_2_idx += 1

        if nums_1_idx == total_nums_1 and nums_1[nums_1_idx - 1] < nums_2[nums_2_idx - 1]:
            break  # Remaining nums in nums 2 > max of nums 1.

        if nums_2_idx == total_nums_2 and nums_2[nums_2_idx - 1] < nums_1[nums_1_idx - 1]:
            break  # Remaining nums in nums 1 > max of nums 2.

    score_1 += sum(nums_1[nums_1_idx:])  # Remaining part of score 1.
    score_2 += sum(nums_2[nums_2_idx:])  # Remaining part of score 2.
    return (max_score + max(score_1, score_2)) % modulo
