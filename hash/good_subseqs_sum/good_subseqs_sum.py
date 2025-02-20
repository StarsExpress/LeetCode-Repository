
def sum_good_subsequences(nums: list[int]) -> int:  # LeetCode Q.3351.
    good_subseqs_sum = 0
    subsequences_table: dict[int, list[int]] = dict()
    for num in nums:
        if num not in subsequences_table.keys():
            subsequences_table.update(
                {num: [0, 0]}  # Format: [count, subseqs sum].
            )
        subsequences_table[num][0] += 1
        subsequences_table[num][1] += num
        good_subseqs_sum += num

        # Current num extends subseqs at such two ends.
        for subseq_end in (num - 1, num + 1):
            if subseq_end in subsequences_table.keys():
                subsequences_table[num][0] += subsequences_table[subseq_end][0]

                new_sum = subsequences_table[subseq_end][1]
                new_sum += subsequences_table[subseq_end][0] * num

                subsequences_table[num][1] += new_sum
                good_subseqs_sum += new_sum

    return good_subseqs_sum % (10 ** 9 + 7)  # Required to control size.
