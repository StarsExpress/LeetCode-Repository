
def count_valid_options(n: int, return_table: bool = False):  # LeetCode Q.1359.
    if n == 1:  # Base case.
        # Table format: key = orders count, value = tuple.
        # Tuple format: combinations, each combination's length.
        return {1: (1, 2)} if return_table else 1

    counts_table = count_valid_options(n - 1, True)
    combinations, length = counts_table[n - 1]  # Last orders' information.
    combinations *= (1 + length + 1) * (length + 1) // 2
    if not return_table:  # Can skip length updates.
        return combinations % (10 ** 9 + 7)  # Required to control size.

    counts_table.update({n: (combinations, length + 2)})
    return counts_table
