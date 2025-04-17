
def count_valid_options(total_orders: int) -> int:  # LeetCode Q.1359.
    valid_pickups = 1  # Base case at n = 1: (P1, D1).

    modulo = 10 ** 9 + 7
    for order in range(2, total_orders + 1):
        last_order_seq_len = 2 * (order - 1)
        combos = (1 + last_order_seq_len + 1) * (last_order_seq_len + 1) // 2
        valid_pickups *= combos
        valid_pickups %= modulo

    return valid_pickups
