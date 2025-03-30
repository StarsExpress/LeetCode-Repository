
def calculate_min_required_money(transactions: list[list[int]]) -> int:  # LeetCode Q.2412.
    min_required_money = 0  # Max cumulated losses <= min required money.

    winning_trade_max_cost = 0  # Absolute value of max cost.
    losing_trade_max_cashback = 0  # Absolute value of max cashback.

    for cost, cashback in transactions:
        if cost > cashback:  # Losing trade.
            min_required_money += cost - cashback
            if cashback > losing_trade_max_cashback:
                losing_trade_max_cashback = cashback
            continue

        if cost > winning_trade_max_cost:
            winning_trade_max_cost = cost

    min_required_money += max(winning_trade_max_cost, losing_trade_max_cashback)
    return min_required_money
