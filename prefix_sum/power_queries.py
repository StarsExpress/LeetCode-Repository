
def query_products(positive_num: int, queries: list[list[int]]) -> list[int]:  # LeetCode Q.2438.
    bin_n = bin(positive_num)[2:][::-1]  # Throw away 0b substring. Reverse entire string.
    powers = [int(digit) * 2 ** idx for idx, digit in enumerate(bin_n) if digit != "0"]

    prefix_products = []
    for power in powers:
        if not prefix_products:
            prefix_products.append(power)
            continue
        prefix_products.append(prefix_products[-1] * power)

    answers, modulo = [], 10 ** 9 + 7
    for start_idx, end_idx in queries:
        answer = prefix_products[end_idx]
        if start_idx > 0:  # Need to divide a prefix product.
            answer //= prefix_products[start_idx - 1]

        answers.append(answer % modulo)  # Required to control size.

    return answers
