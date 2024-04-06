
def count_same_product_tuples(integers: list[int]):  # LeetCode Q.1726.
    integers = list(set(integers))
    if len(integers) <= 0:
        raise ValueError('Empty integers list.')

    if len(integers) < 4:
        return 0

    products, start_idx, end_idx, current_product = dict(), 0, 1, 0
    while True:
        if end_idx >= len(integers):
            if start_idx >= end_idx - 1:
                break

            start_idx += 1
            end_idx += start_idx + 1 - end_idx
            continue

        current_product += integers[start_idx] * integers[end_idx] - current_product
        if current_product not in products.keys():
            products.update({current_product: [(integers[start_idx], integers[end_idx])]})

        else:
            products[current_product].append((integers[start_idx], integers[end_idx]))

        end_idx += 1

    count = 0
    for product in products.values():
        if len(product) == 2:
            count += 8
            continue

        if len(product) > 2:
            # Combination of 2 out of n is n * (n - 1) / 2.
            # Each combination has multiple of 8. So outer multiple is 8 / 2 = 4
            count += (len(product) - 1) * len(product) * 4

    return count
