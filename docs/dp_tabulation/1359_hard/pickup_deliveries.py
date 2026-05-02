
def count_valid_sequences(total_orders: int) -> int:  # LeetCode Q.1359.
    modulo = 10 ** 9 + 7

    # Base case when n is 1: pickup 1 followed by delivery 1.
    valid_sequences = 1

    for prev_order_num in range(1, total_orders):
        spots_count = 2 * prev_order_num + 1

        # Sum from 1 to spots count.
        multiple = spots_count * (spots_count + 1) // 2

        valid_sequences *= multiple
        valid_sequences %= modulo

    return valid_sequences
