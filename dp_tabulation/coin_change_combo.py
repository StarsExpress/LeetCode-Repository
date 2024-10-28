
def find_all_combinations(amount: int, coins: list[int]) -> int:  # LeetCode Q.518.
    # Base case: 0 amount only has 1 combo (no coins at all).
    all_combo = [1] + [0] * amount
    for coin in coins:
        for target_amount in range(coin, amount + 1):
            all_combo[target_amount] += all_combo[target_amount - coin]

    return all_combo[amount]
