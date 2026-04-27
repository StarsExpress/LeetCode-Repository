#include <vector>
#include <stack>
using namespace std;

int calculateTrappedWater(vector<int> &heights) // LeetCode Q.42.
{
    stack<pair<int, int>> stack; // Format: (height, idx).
    int trappedWater = 0;

    for (int idx = 0; idx < heights.size(); idx++)
    {
        int anchor = 0;

        while (!stack.empty())
        {
            int height = min(heights[idx], stack.top().first) - anchor;
            int width = idx - 1 - stack.top().second;

            trappedWater += height * width;

            // Stop when seeing a remaining taller bar.
            if (stack.top().first > heights[idx])
                break;

            anchor = stack.top().first;
            stack.pop();
        }

        stack.push({heights[idx], idx});
    }

    return trappedWater;
}
