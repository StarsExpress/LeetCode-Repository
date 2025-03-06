
def count_and_pair_xor_sum(nums_1: list[int], nums_2: list[int]) -> int:  # LeetCode Q.1835.
    # Key: (a & b) ^ (a & c) = a & (b ^ c).
    xor_value_1, xor_value_2 = 0, 0
    for num in nums_1:
        xor_value_1 ^= num

    for num in nums_2:
        xor_value_2 ^= num

    return xor_value_1 & xor_value_2
