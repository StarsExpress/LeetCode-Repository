
def find_min_coins_usage(coins: list[int], amount: int) -> int:  # LeetCode Q.322.
    # Base case: 0 amount needs no coins at all.
    min_denomination = [0] + [-1] * amount
    for target_amount in range(1, amount + 1):
        for coin in coins:
            if target_amount < coin:  # Current coin can't build up target amount.
                continue

            used_coins_count = min_denomination[target_amount - coin]
            if used_coins_count != -1:  # New combo found.
                used_coins_count += 1  # Plus 1: usage of current coin.

                if min_denomination[target_amount] == -1:  # New combo is the 1st found combo.
                    min_denomination[target_amount] = used_coins_count
                    continue

                if used_coins_count < min_denomination[target_amount]:
                    min_denomination[target_amount] = used_coins_count

    return min_denomination[amount]
