
def sum_good_subsequences(nums: list[int]) -> int:  # LeetCode Q.3351.
    modulo = 10 ** 9 + 7  # Prevents overflow.

    subseqCounts: dict[int, int] = dict()
    subseqSums: dict[int, int] = dict()

    for num in nums:
        if num not in subseqCounts.keys():
            subseqCounts[num] = 0

        if num not in subseqSums.keys():
            subseqSums[num] = 0

        for validTail in (num - 1, num + 1):
            subseqCounts[num] += subseqCounts.get(validTail, 0)

            subseqSums[num] += num * subseqCounts.get(validTail, 0)

            subseqSums[num] += subseqSums.get(validTail, 0)

        subseqCounts[num] += 1
        subseqCounts[num] %= modulo
        subseqSums[num] += num
        subseqSums[num] %= modulo

    return sum(subseqSums.values()) % modulo  # Control value magnitude.
