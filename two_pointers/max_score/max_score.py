
def find_max_score(nums_1: list[int], nums_2: list[int]) -> int:  # LeetCode Q.1537.
    max_score, modulo = 0, 10 ** 9 + 7
    idx_1, sum_1, total_nums_1 = 0, nums_1[0], len(nums_1)
    idx_2, sum_2, total_nums_2 = 0, nums_2[0], len(nums_2)

    while idx_1 < total_nums_1 and idx_2 < total_nums_2:
        while nums_1[idx_1] < nums_2[idx_2]:
            if idx_1 == total_nums_1 - 1:
                break
            idx_1 += 1
            sum_1 += nums_1[idx_1]

        if nums_1[idx_1] < nums_2[idx_2]:
            break  # Nums 1 can't catch up with nums 2.

        while nums_2[idx_2] < nums_1[idx_1]:
            if idx_2 == total_nums_2 - 1:
                break
            idx_2 += 1
            sum_2 += nums_2[idx_2]

        if nums_2[idx_2] < nums_1[idx_1]:
            break  # Nums 2 can't catch up with nums 1.

        if nums_1[idx_1] == nums_2[idx_2]:
            max_score += max(sum_1, sum_2)
            max_score %= modulo

            sum_1 = 0  # Reset sum 1.
            idx_1 += 1
            if idx_1 < total_nums_1:
                sum_1 += nums_1[idx_1]

            sum_2 = 0  # Reset sum 2.
            idx_2 += 1
            if idx_2 < total_nums_2:
                sum_2 += nums_2[idx_2]

    while idx_1 < total_nums_1 - 1:  # Sum the rest of nums 1.
        idx_1 += 1
        sum_1 += nums_1[idx_1]

    while idx_2 < total_nums_2 - 1:  # Sum the rest of nums 2.
        idx_2 += 1
        sum_2 += nums_2[idx_2]

    max_score += max(sum_1, sum_2)
    return max_score % modulo
