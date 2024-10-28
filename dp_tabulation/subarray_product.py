
def compute_max_subarray_product(integers: list[int]) -> int:  # LeetCode Q.152.
    max_product = max(integers)  # Base case.

    if integers[0] >= 0:  # Subarray product is the "non-negative" product.
        subarray_prod, negative_prod = integers.pop(0), None  # None: negative product doesn't exist.

    else:
        negative_prod, subarray_prod = integers.pop(0), 0  # 0: subarray product doesn't exist.

    for number in integers:
        if number == 0:  # Number is 0: reset both products to initial values.
            subarray_prod, negative_prod = 0, None
            continue

        if subarray_prod == 0:  # Number isn't 0: "activate" subarray product.
            subarray_prod += 1

        if number > 0:
            subarray_prod *= number
            # Multiply negative product by positive number to await later negative number to "surpass".
            if negative_prod is not None:
                negative_prod *= number

        else:  # Negative number lets negative product surpass subarray product.
            if negative_prod is not None:
                subarray_prod, negative_prod = negative_prod * number, subarray_prod * number

            else:
                subarray_prod, negative_prod = 0, subarray_prod * number

        if subarray_prod > max_product:
            max_product = subarray_prod

    return max_product
