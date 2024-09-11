
def maximize_xor(numbers: list[int], max_bits: int) -> list[int]:  # LeetCode Q.1829.
    maximum = int("1" * max_bits, 2)
    xor_values, results = [], []
    for number in numbers:
        if not xor_values:
            xor_values.append(number)
            results.append(maximum - number)
            continue
        xor_values.append(xor_values[-1] ^ number)
        results.append(maximum - xor_values[-1])

    return results[::-1]  # Required to reverse queried results.
