
def find_selfless_products(integers: list[int]):  # LeetCode Q.238.
    prefix_products, suffix_products = [], []
    for integer in integers:
        if not prefix_products:
            prefix_products.append(integer)
            continue

        if prefix_products[-1] == 0:
            prefix_products.append(0)
            continue
        prefix_products.append(prefix_products[-1] * integer)

    for integer in integers[::-1]:  # Suffix products: backward iteration.
        if not suffix_products:
            suffix_products.append(integer)
            continue

        if suffix_products[-1] == 0:
            suffix_products.append(0)
            continue
        suffix_products.append(suffix_products[-1] * integer)

    suffix_products = suffix_products[::-1]  # Reverse to original indices order.

    selfless_products, total_nums = [], len(integers)
    for idx, integer in enumerate(integers):
        if idx == total_nums - 1:
            selfless_products.append(prefix_products[-2])
            return selfless_products

        if idx == 0:
            selfless_products.append(suffix_products[1])
            continue

        selfless_products.append(prefix_products[idx - 1] * suffix_products[idx + 1])
