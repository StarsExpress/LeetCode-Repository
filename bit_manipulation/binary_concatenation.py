
def concatenate_binary_strings(n: int):  # LeetCode Q.1680.
    """Return decimal value of concatenated binary strings from 1 to n."""
    decimal_value = 0
    threshold, current_len = 2, 1  # Threshold is always a power of 2.
    for num in range(1, n + 1):
        if num >= threshold:  # This number's bin format adds current length by 1.
            threshold *= 2
            current_len += 1

        decimal_value *= 2 ** current_len  # Enlarge latest value by 2 ** current len.
        decimal_value += num
        decimal_value %= (10 ** 9 + 7)  # Required to control size.

    return decimal_value
