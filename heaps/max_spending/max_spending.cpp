#include <vector>
#include <queue>
using namespace std;

long long maximizeSpending(vector<vector<int>> &values)
{ // LeetCode Q.2931.
    // Min heap. Format: {item, row idx}.
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> itemsHeap;

    for (int rowIdx = 0; rowIdx < values.size(); rowIdx++)
    {
        int item = values[rowIdx].back();
        itemsHeap.push({item, rowIdx});
        values[rowIdx].pop_back();
    }

    long long maxSpentMoney = 0, day = 1;

    while (!itemsHeap.empty())
    {
        auto [item, rowIdx] = itemsHeap.top();
        itemsHeap.pop();
        maxSpentMoney += item * day;
        day++;

        if (!values[rowIdx].empty())
        {
            int newItem = values[rowIdx].back();
            itemsHeap.push({newItem, rowIdx});
            values[rowIdx].pop_back();
        }
    }

    return maxSpentMoney;
}
