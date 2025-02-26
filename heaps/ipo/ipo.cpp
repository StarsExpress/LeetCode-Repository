#include <vector>
using namespace std;

int maximize_capital(int k, int w, vector<int> &profits, vector<int> &capital)
{
    // LeetCode 502.
    vector<vector<int>> capitals_min_heap; // Format: {capital, idx}.
    for (int idx = 0; idx < capital.size(); idx++)
    {
        capitals_min_heap.push_back({-capital[idx], idx}); // Negate capital to fit min heap.
        push_heap(capitals_min_heap.begin(), capitals_min_heap.end());
    }

    vector<int> profits_max_heap;
    while (k > 0)
    { // Negate capital back to original value.
        while (!capitals_min_heap.empty() && w >= -capitals_min_heap[0][0])
        {
            // Grab all the affordable projects' profits into max heap.
            int profit_idx = capitals_min_heap[0][1];
            profits_max_heap.push_back(profits[profit_idx]);
            push_heap(profits_max_heap.begin(), profits_max_heap.end());

            pop_heap(capitals_min_heap.begin(), capitals_min_heap.end());
            capitals_min_heap.pop_back();
        }

        if (profits_max_heap.empty())
        { // No more affordable projects.
            break;
        }
        else
        {
            w += profits_max_heap[0];
            k -= 1;
            pop_heap(profits_max_heap.begin(), profits_max_heap.end());
            profits_max_heap.pop_back();
        }
    }

    return w;
}
