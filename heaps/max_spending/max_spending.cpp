#include <vector>
#include <queue>
using namespace std;

long long maximize_spending(vector<vector<int>> &values)
{ // LeetCode Q.2931.
    // Min heap. Format: {item, row idx}.
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> items_heap;

    for (int row_idx = 0; row_idx < values.size(); row_idx++)
    {
        int item = values[row_idx].back();
        items_heap.push({item, row_idx});
        values[row_idx].pop_back();
    }

    long long max_spent_money = 0, day = 1;
    while (!items_heap.empty())
    {
        auto [item, row_idx] = items_heap.top();
        items_heap.pop();
        max_spent_money += item * day;
        day++;

        if (!values[row_idx].empty())
        {
            int new_item = values[row_idx].back();
            items_heap.push({new_item, row_idx});
            values[row_idx].pop_back();
        }
    }

    return max_spent_money;
}
