
def count_special_subsequences(nums: list[int]) -> int:  # LeetCode Q.1955.
    modulo = 10 ** 9 + 7
    last_digits_counts = {0: 0, 1: 0, 2: 0}
    for num in nums:
        last_digits_counts[num] *= 2  # Double your past ally.
        if num == 0:  # Opens a possible special subseq start.
            last_digits_counts[0] += 1

        if num == 1:  # Extends possible subseqs ending with 0.
            last_digits_counts[1] += last_digits_counts[0]

        if num == 2:  # Fulfills subseqs ending with 1.
            last_digits_counts[2] += last_digits_counts[1]

        last_digits_counts[num] %= modulo  # Required to control size.

    return last_digits_counts[2]
