
def count_same_product_tuples(integers: list[int]):  # LeetCode Q.1726.
    integers = list(set(integers))  # Only consider unique ints.
    ints_count = len(integers)
    if ints_count < 4:
        return 0

    # For each unique product, track all tuples achieving it.
    products, current_product = dict(), 0
    start_idx, end_idx = 0, 1
    while True:
        if end_idx >= ints_count:
            if start_idx >= end_idx - 1:
                break

            start_idx += 1
            end_idx += start_idx + 1 - end_idx
            continue

        current_product += integers[start_idx] * integers[end_idx] - current_product
        if current_product not in products.keys():
            products.update({current_product: []})

        products[current_product].append((integers[start_idx], integers[end_idx]))
        end_idx += 1

    count = 0
    for product in products.values():
        product_len = len(product)
        if product_len == 2:
            count += 8  # For two tuples each having 2 ints, permutation = 2 * 2 * 2 = 8.
            continue

        if product_len > 2:
            # Combination of 2 out of n is n * (n - 1) / 2.
            # Each combination has multiple of 8. So outer multiple is 8 / 2 = 4
            count += (product_len - 1) * product_len * 4

    return count
