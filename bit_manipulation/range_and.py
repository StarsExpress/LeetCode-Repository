
def calculate_range_and(left: int, right: int):  # LeetCode Q.201.
    """
    Given two integers left and right, return bitwise AND of all numbers in this inclusive range.

    Key: when logs of left & right share same integer part,
    bitwise AND from left to right is the common prefix of left & right binary strings.
    """
    if left == 0 or left == right:  # Base case.
        return left

    left_bin_chars, right_bin_chars = list(bin(left)), list(bin(right))
    if len(left_bin_chars) < len(right_bin_chars):
        return 0  # Different magnitude: answer is definitely 0.

    bitwise_and_chars = ""
    for idx, left_bin_char in enumerate(left_bin_chars):
        if right_bin_chars[idx] != left_bin_char:  # Diff occurs: pad 0 for the rest chars.
            bitwise_and_chars += "0" * (len(left_bin_chars) - idx)
            return int(bitwise_and_chars, 2)
        bitwise_and_chars += left_bin_char
