
def search_quotient(dividend: int, divisor: int) -> int:  # LeetCode Q.29.
    negative = True if max(dividend, divisor) > 0 > min(dividend, divisor) else False
    dividend, divisor = abs(dividend), abs(divisor)

    quotient, shift_amount = 0, 0
    while divisor <= dividend:  # Keep multiplying divisor by 2 until greater than dividend.
        divisor <<= 1
        shift_amount += 1

    while shift_amount > 0:  # Subtract and shift back to get quotient.
        shift_amount -= 1
        divisor >>= 1

        if dividend >= divisor:  # Divisor can still contribute to quotient.
            dividend -= divisor
            quotient += 1 << shift_amount  # Shift amount = power of 2 by which divisor was multiplied.

    two_to_power_31 = 2 ** 31  # Required to set bounds.
    if negative:
        quotient = max(-quotient, -two_to_power_31)
    return min(quotient, two_to_power_31 - 1)
