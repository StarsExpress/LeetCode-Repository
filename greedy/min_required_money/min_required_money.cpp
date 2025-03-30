#include <vector>
using namespace std;

long long calculate_min_required_money(vector<vector<int>> &transactions)
{ // LeetCode Q.2412.
    // Max cumulated losses <= min required money.
    long long min_required_money = 0;

    long long winning_trade_max_cost = 0;    // Absolute value of max cost.
    long long losing_trade_max_cashback = 0; // Absolute value of max cashback.

    for (auto transaction : transactions)
    {
        if (transaction[0] > transaction[1])
        { // Losing trade.
            min_required_money += transaction[0] - transaction[1];
            if (transaction[1] > losing_trade_max_cashback)
            {
                losing_trade_max_cashback = transaction[1];
            }
            continue;
        }
        if (transaction[0] > winning_trade_max_cost)
        {
            winning_trade_max_cost = transaction[0];
        }
    }

    min_required_money += max(winning_trade_max_cost, losing_trade_max_cashback);
    return min_required_money;
}
