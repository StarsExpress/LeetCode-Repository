
def count_subarray_products(positive_integers: list[int], k: int) -> int:  # LeetCode Q.713.
    """Count the number of continuous subarrays with product < k."""
    continuous_subarrays = 0
    prefix_products, length = [], 0  # Length: prefix products array length.
    for idx, integer in enumerate(positive_integers):
        if idx == 0:  # 1st integer.
            prefix_products.append(integer)
            length += 1
            if integer < k:
                continuous_subarrays += 1
            continue

        prefix_products.append(prefix_products[-1] * integer)
        length += 1

        while length > 1 and prefix_products[-1] // prefix_products[0] >= k:
            prefix_products.pop(0)
            length -= 1

        continuous_subarrays += length - 1  # Minus 1: don't re-count latest prefix product.
        if prefix_products[-1] < k:  # Subarray from 0th idx to (idx)th idx.
            continuous_subarrays += 1

    return continuous_subarrays
