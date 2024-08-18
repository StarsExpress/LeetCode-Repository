
max_broken_products = dict()


def _build_table():
    max_broken_products.clear()  # Reset before breaking max product.


def break_max_product(integer: int, recursion: bool = False):  # LeetCode Q.343.
    if not recursion:  # Called by outside.
        _build_table()

    max_product = integer - 1  # Base case: 1 * integer - 1.
    half_point = integer // 2
    for i in range(2, half_point + 1):  # Symmetry: only need to iterate to half point.
        try:
            max_broken_products[integer - i]

        except KeyError:
            break_max_product(integer - i, True)

        # Pick better value: max broken product of integer - i or integer - i itself.
        new_product = i * max(max_broken_products[integer - i], integer - i)
        if new_product <= max_product:  # Key: once new product stops rising, answer is found.
            break
        max_product = new_product  # Keep updating max product.

    max_broken_products.update({integer: max_product})
    return max_product
