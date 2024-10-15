
def calculate_min_money(transactions: list[list[int]]) -> int:  # LeetCode Q.2412.
    total_non_loss_transactions, max_non_loss_cost = 0, 0
    max_cumulated_loss = 0
    for cost, cashback in transactions:
        if cashback < cost:
            max_cumulated_loss += cashback - cost
            continue

        total_non_loss_transactions += 1
        if cost > max_non_loss_cost:
            max_non_loss_cost = cost

    min_required_money = 0
    for cost, cashback in transactions:
        if cashback < cost:
            required_money = cost - (max_cumulated_loss + cost - cashback)
            if required_money > min_required_money:
                min_required_money = required_money

    if total_non_loss_transactions > 0:  # Not all transactions have losses.
        if max_non_loss_cost - max_cumulated_loss > min_required_money:
            min_required_money = max_non_loss_cost - max_cumulated_loss

    return min_required_money
