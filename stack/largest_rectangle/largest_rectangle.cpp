#include <vector>
#include <stack>
using namespace std;

int find_largest_rectangle(vector<int> &heights) // LeetCode Q.84.
{
    vector<int> next_smaller_indices(heights.size(), -1); // -1: non-existent.
    vector<int> prev_smaller_indices(heights.size(), -1);

    stack<pair<int, int>> stack; // Format: {idx, height}.

    for (int idx = 0; idx < heights.size(); idx++)
    { // Next smaller search.
        int height = heights[idx];
        while (!stack.empty() && stack.top().second > height)
        {
            int prev_idx = stack.top().first;
            next_smaller_indices[prev_idx] = idx;
            stack.pop();
        }

        stack.push({idx, height});
    }

    stack = {}; // Empty stack before search.
    for (int idx = heights.size() - 1; idx >= 0; idx--)
    { // Prev smaller search.
        int height = heights[idx];
        while (!stack.empty() && stack.top().second > height)
        {
            int next_idx = stack.top().first;
            prev_smaller_indices[next_idx] = idx;
            stack.pop();
        }

        stack.push({idx, height});
    }

    int max_area = 0;
    for (int idx = 0; idx < heights.size(); idx++)
    {
        int rectangle_left_idx = 0;
        if (prev_smaller_indices[idx] != -1)
            rectangle_left_idx += prev_smaller_indices[idx] + 1;

        int rectangle_right_idx = heights.size() - 1;
        if (next_smaller_indices[idx] != -1)
            rectangle_right_idx = next_smaller_indices[idx] - 1;

        int area = heights[idx] * (rectangle_right_idx + 1 - rectangle_left_idx);
        if (area > max_area)
            max_area = area;
    }

    return max_area;
}
