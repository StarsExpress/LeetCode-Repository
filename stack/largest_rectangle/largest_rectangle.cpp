#include <vector>
#include <stack>
using namespace std;

int find_largest_rectangle(vector<int> &heights)
{ // LeetCode Q.84.
    vector<int> prev_smaller_indices(heights.size(), -1);
    vector<int> next_smaller_indices(heights.size(), heights.size());

    stack<pair<int, int>> prev_stack, next_stack; // Format: {height, idx}.
    for (int idx = 0; idx < heights.size(); idx++)
    {
        int height = heights[idx];

        while (!prev_stack.empty() && prev_stack.top().first >= height)
        {
            prev_stack.pop();
        }
        if (!prev_stack.empty())
        {
            int past_idx = prev_stack.top().second;
            prev_smaller_indices[idx] = past_idx;
        }
        prev_stack.push({height, idx});

        while (!next_stack.empty() && next_stack.top().first > height)
        {
            int past_idx = next_stack.top().second;
            next_smaller_indices[past_idx] = idx;
            next_stack.pop();
        }
        next_stack.push({height, idx});
    }

    int largest_rectangle = 0;
    for (int idx = 0; idx < heights.size(); idx++)
    {
        int width = 1;
        width += next_smaller_indices[idx] - 1 - idx;
        width += idx - 1 - prev_smaller_indices[idx];

        int rectangle = heights[idx] * width;
        if (rectangle > largest_rectangle)
        {
            largest_rectangle = rectangle;
        }
    }

    return largest_rectangle;
}
