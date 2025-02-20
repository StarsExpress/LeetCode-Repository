
def find_max_score(numbers_1: list[int], numbers_2: list[int]) -> int:  # LeetCode Q.1537.
    max_score = 0
    range_sum_1, range_sum_2 = numbers_1[0], numbers_2[0]

    total_numbers_1, total_numbers_2 = len(numbers_1), len(numbers_2)
    numbers_1_idx, numbers_2_idx = 0, 0
    while numbers_1_idx < total_numbers_1 and numbers_2_idx < total_numbers_2:
        if numbers_1[numbers_1_idx] == numbers_2[numbers_2_idx]:
            max_score += max(range_sum_1, range_sum_2)

            range_sum_1 -= range_sum_1  # Reset range sum 1.
            numbers_1_idx += 1
            if numbers_1_idx < total_numbers_1:
                range_sum_1 += numbers_1[numbers_1_idx]

            range_sum_2 -= range_sum_2  # Reset range sum 2.
            numbers_2_idx += 1
            if numbers_2_idx < total_numbers_2:
                range_sum_2 += numbers_2[numbers_2_idx]

            continue

        while numbers_1[numbers_1_idx] < numbers_2[numbers_2_idx] and numbers_1_idx < total_numbers_1 - 1:
            numbers_1_idx += 1
            range_sum_1 += numbers_1[numbers_1_idx]

        if numbers_1[numbers_1_idx] < numbers_2[numbers_2_idx]:
            break

        while numbers_2[numbers_2_idx] < numbers_1[numbers_1_idx] and numbers_2_idx < total_numbers_2 - 1:
            numbers_2_idx += 1
            range_sum_2 += numbers_2[numbers_2_idx]

        if numbers_2[numbers_2_idx] < numbers_1[numbers_1_idx]:
            break

    while numbers_1_idx < total_numbers_1 - 1:  # nums1[numbers_1_idx] is already included.
        range_sum_1 += numbers_1[numbers_1_idx + 1]
        numbers_1_idx += 1

    while numbers_2_idx < total_numbers_2 - 1:  # nums2[numbers_2_idx] is already included.
        range_sum_2 += numbers_2[numbers_2_idx + 1]
        numbers_2_idx += 1

    max_score += max(range_sum_1, range_sum_2)
    return max_score % (10 ** 9 + 7)
