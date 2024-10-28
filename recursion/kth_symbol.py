
def find_kth_symbol(n: int, k: int) -> int:  # LeetCode Q.779.
    """
    Key: nth row = (n - 1)th row + (n - 1)th row 2nd half + (n - 1)th row 1st half.
    """
    if n <= 2:  # Base case.
        return 0 if k == 1 else 1

    latest_row_len = 2 ** (n - 2)  # Length of (n - 1)th row.
    if k <= latest_row_len:  # No need to adjust k.
        return find_kth_symbol(n - 1, k)

    one_point_five_len = latest_row_len * 3 // 2
    if latest_row_len < k <= one_point_five_len:  # k in (n - 1)th row's 2nd half.
        return find_kth_symbol(n - 1, k - (latest_row_len // 2))

    # k in (n - 1)th row's 1st half.
    return find_kth_symbol(n - 1, k - one_point_five_len)
