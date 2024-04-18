
def search_quotient(dividend: int, divisor: int):
    return min(max(int(dividend / divisor), -(2 ** 31)), 2 ** 31 - 1)
