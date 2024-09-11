
def minimize_xor(number_1: int, number_2: int) -> int:  # LeetCode Q.2429.
    number_1_ones_count = 0
    for char in bin(number_1)[2:]:
        if char == "1":
            number_1_ones_count += 1

    number_2_ones_count = 0
    for char in bin(number_2)[2:]:
        if char == "1":
            number_2_ones_count += 1

    if number_1_ones_count == number_2_ones_count:
        return number_1

    number_1_bin_chars = bin(number_1)[2:]  # Skip substring "0b".
    number_1_bin_len = len(number_1_bin_chars)

    if number_1_ones_count > number_2_ones_count:
        x = 0
        for idx, char in enumerate(number_1_bin_chars):
            if char == "1":
                x += 2 ** (number_1_bin_len - 1 - idx)
                number_2_ones_count -= 1
                if number_2_ones_count == 0:
                    return x

    x = number_1
    for idx, char in enumerate(number_1_bin_chars[::-1]):
        if char == "0":
            x += 2 ** idx
            number_2_ones_count -= 1
            if number_2_ones_count == number_1_ones_count:
                return x

    for num in range(number_2_ones_count - number_1_ones_count):
        x += 2 ** (number_1_bin_len + num)
    return x
