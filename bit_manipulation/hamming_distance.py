
def calculate_hamming_distance(numbers: list[int]):  # LeetCode Q.477.
    hamming_distance = 0
    one_count = zero_count = 0  # Counts for ones and zeros in current bit position.

    max_num_bin_len = len(bin(max(numbers)))  # Keep substring "0b"!
    for bit_position in range(max_num_bin_len - 1):
        for number in numbers:
            # Right shift number by bit position and get the least significant bit.
            bit = (number >> bit_position) & 1

            if bit:  # Update count of ones or zeros by least significant bit.
                one_count += 1

            else:
                zero_count += 1

        hamming_distance += one_count * zero_count
        one_count -= one_count
        zero_count -= zero_count

    return hamming_distance
