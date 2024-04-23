
def compute_max_subarray_product(integers: list[int]):  # LeetCode Q.152.
    max_product = max(integers)  # Base case.

    if integers[0] >= 0:  # Subarray product is the "non-negative" product.
        subarray_prod, negative_prod = integers.pop(0), None  # None: negative product doesn't exist.

    else:
        negative_prod, subarray_prod = integers.pop(0), 0  # 0: subarray product doesn't exist.

    while len(integers) > 0:
        newcomer = integers.pop(0)
        if newcomer == 0:  # Newcomer is 0: reset both products to initial values.
            subarray_prod, negative_prod = 0, None
            continue

        if subarray_prod == 0:  # Newcomer isn't 0: "activate" subarray product.
            subarray_prod += 1

        if newcomer > 0:
            subarray_prod *= newcomer
            # Multiply negative product by positive newcomer to await later negative number to "surpass".
            if negative_prod is not None:
                negative_prod *= newcomer

        else:  # Negative newcomer lets negative product surpass subarray product.
            if negative_prod is not None:
                subarray_prod, negative_prod = negative_prod * newcomer, subarray_prod * newcomer

            else:
                subarray_prod, negative_prod = 0, subarray_prod * newcomer

        if subarray_prod > max_product:
            max_product = subarray_prod

    return max_product
