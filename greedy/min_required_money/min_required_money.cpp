#include <vector>
using namespace std;

long long calculateMinRequiredMoney(vector<vector<int>> &transactions)
{ // LeetCode Q.2412.
    // Max cumulated losses <= min required money.
    long long minRequiredMoney = 0;

    long long winningTradeMaxCost = 0;    // Absolute value of max cost.
    long long losingTradeMaxCashback = 0; // Absolute value of max cashback.

    for (auto transaction : transactions)
    {
        if (transaction[0] > transaction[1]) // Losing trade.
        {
            minRequiredMoney += transaction[0] - transaction[1];
            if (transaction[1] > losingTradeMaxCashback)
                losingTradeMaxCashback = transaction[1];

            continue;
        }
        if (transaction[0] > winningTradeMaxCost)
            winningTradeMaxCost = transaction[0];
    }

    minRequiredMoney += max(winningTradeMaxCost, losingTradeMaxCashback);
    return minRequiredMoney;
}
