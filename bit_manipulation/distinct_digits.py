
def verify_distinct_digits(integer: int):
    bit_mask = 0  # Start with empty bitmask.
    while integer > 0:
        rightmost_digit = integer % 10
        if bit_mask & (1 << rightmost_digit):
            return False  # The bit for rightmost digit is already set: repeat occurs.

        bit_mask |= (1 << rightmost_digit)  # Set rightmost digit's bit.
        integer //= 10  # Remove rightmost digit.

    return True  # All digits are distinct.
