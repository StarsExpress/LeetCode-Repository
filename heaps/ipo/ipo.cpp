#include <vector>
#include <queue>
using namespace std;

int maximizeCapital(int k, int wealth, vector<int> &profits, vector<int> &capital)
{ // LeetCode 502.
    // Min heap. Format: {capital, profit idx}.
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> capitalsHeap;

    for (int idx = 0; idx < capital.size(); idx++)
        capitalsHeap.push({capital[idx], idx});

    priority_queue<int> profitsHeap; // Max heap.

    while (k > 0)
    {
        while (!capitalsHeap.empty() && wealth >= capitalsHeap.top().first)
        {
            // Grab all the affordable projects' profits into max heap.
            auto [capital, profit_idx] = capitalsHeap.top();
            profitsHeap.push(profits[profit_idx]);
            capitalsHeap.pop();
        }

        if (profitsHeap.empty()) // No more affordable projects.
            break;

        else
        {
            wealth += profitsHeap.top();
            k -= 1;
            profitsHeap.pop();
        }
    }

    return wealth;
}
