
def find_min_coins_usage(coins: list[int], amount: int) -> int | float:  # LeetCode Q.322.
    min_coins = [0] + [float("inf")] * amount  # Idx = amount. Base case: 0 amount.
    for iter_amount in range(1, amount + 1):
        for coin in coins:
            if iter_amount == coin:
                min_coins[iter_amount] = 1
                break

            if iter_amount > coin:
                if 1 + min_coins[iter_amount - coin] < min_coins[iter_amount]:
                    min_coins[iter_amount] = 1 + min_coins[iter_amount - coin]

    return -1 if min_coins[amount] == float("inf") else min_coins[amount]
