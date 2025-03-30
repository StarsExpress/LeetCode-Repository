#include <vector>
#include <queue>
using namespace std;

int maximize_capital(int k, int wealth, vector<int> &profits, vector<int> &capital)
{ // LeetCode 502.
    // Min heap. Format: {capital, profit idx}.
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> capitals_heap;
    for (int idx = 0; idx < capital.size(); idx++)
    {
        capitals_heap.push({capital[idx], idx});
    }

    priority_queue<int> profits_heap; // Max heap.
    while (k > 0)
    {
        while (!capitals_heap.empty() && wealth >= capitals_heap.top().first)
        {
            // Grab all the affordable projects' profits into max heap.
            auto [capital, profit_idx] = capitals_heap.top();
            profits_heap.push(profits[profit_idx]);
            capitals_heap.pop();
        }

        if (profits_heap.empty())
        { // No more affordable projects.
            break;
        }
        else
        {
            wealth += profits_heap.top();
            k -= 1;
            profits_heap.pop();
        }
    }

    return wealth;
}
