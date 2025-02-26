#include <vector>
#include <stack>
using namespace std;

int calculate_trapped_water(vector<int> &heights)
{ // LeetCode Q.42.
    // Height decreasing monotonic stack. Format: (height, idx).
    stack<pair<int, int>> stack;
    int trapped_water = 0;
    for (int idx = 0; idx < heights.size(); idx++)
    {
        int anchor_height = 0;
        while (!stack.empty())
        {
            int height = min(heights[idx], stack.top().first) - anchor_height;
            int width = idx - 1 - stack.top().second;
            trapped_water += height * width;

            if (stack.top().first > heights[idx])
            {
                break; // Stop when seeing a remaining taller bar.
            }
            anchor_height = stack.top().first; // Anchors for next encountered left height.

            stack.pop(); // My right bars can't work with left bars no taller than me.
        }

        stack.push({heights[idx], idx});
    }
    return trapped_water;
}
