
def search_quotient(dividend: int, divisor: int) -> int:
    return min(max(int(dividend / divisor), -(2 ** 31)), 2 ** 31 - 1)


if __name__ == '__main__':
    print(search_quotient(-2147483648, -1))
