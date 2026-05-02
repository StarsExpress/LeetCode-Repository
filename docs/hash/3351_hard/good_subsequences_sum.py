
def sum_good_subsequences(nums: list[int]) -> int:  # LeetCode Q.3351.
    modulo = 10 ** 9 + 7  # Prevents overflow.

    unique_nums = set(nums)

    subseqCounts: dict[int, int] = dict(
        zip(unique_nums, [0] * len(unique_nums))
    )

    subseqSums: dict[int, int] = dict(
        zip(unique_nums, [0] * len(unique_nums))
    )

    for num in nums:
        for validTail in (num - 1, num + 1):
            subseqCounts[num] += subseqCounts.get(validTail, 0)

            subseqSums[num] += num * subseqCounts.get(validTail, 0)

            subseqSums[num] += subseqSums.get(validTail, 0)

        subseqCounts[num] += 1
        if subseqCounts[num] > modulo: subseqCounts[num] %= modulo

        subseqSums[num] += num
        if subseqSums[num] > modulo: subseqSums[num] %= modulo

    return sum(subseqSums.values()) % modulo  # Control value magnitude.
