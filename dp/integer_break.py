
def break_max_product(
    integer: int, max_broken_products: dict[int, int], return_dict: bool = False
):  # LeetCode Q.343.
    if not max_broken_products:
        max_broken_products = dict()

    max_product = integer - 1  # Base case: 1 * integer - 1.
    half_point = integer // 2
    for i in range(2, half_point + 1):  # Symmetry: only need to iterate to half point.
        try:
            max_broken_products[integer - i]

        except KeyError:
            max_broken_products = break_max_product(integer - i, max_broken_products, True)

        # Pick the best of max broken product of integer - i or integer - i itself.
        new_product = i * max(max_broken_products[integer - i], integer - i)

        # Key: once new product stops rising, answer is found.
        if new_product <= max_product:
            break
        max_product = new_product  # Keep updating max product.

    max_broken_products.update({integer: max_product})

    if return_dict:
        return max_broken_products
    return max_product
