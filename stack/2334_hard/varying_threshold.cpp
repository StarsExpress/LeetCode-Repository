#include <vector>
#include <stack>
using namespace std;

int find_valid_subarray_size(vector<int> &nums, int threshold)
{ // LeetCode Q.2334.
    vector<int> prev_smaller_indices(nums.size(), -1);
    vector<int> next_smaller_indices(nums.size(), nums.size());

    stack<pair<int, int>> prev_stack, next_stack; // Format: {num, idx}.
    for (int idx = 0; idx < nums.size(); idx++)
    {
        int num = nums[idx];

        while (!prev_stack.empty() && prev_stack.top().first >= num)
        {
            prev_stack.pop();
        }
        if (!prev_stack.empty())
        {
            int past_idx = prev_stack.top().second;
            prev_smaller_indices[idx] = past_idx;
        }
        prev_stack.push({num, idx});

        while (!next_stack.empty() && next_stack.top().first > num)
        {
            int past_idx = next_stack.top().second;
            next_smaller_indices[past_idx] = idx;
            next_stack.pop();
        }
        next_stack.push({num, idx});
    }

    for (int idx = 0; idx < nums.size(); idx++)
    {
        int width = 1;
        width += next_smaller_indices[idx] - 1 - idx;
        width += idx - 1 - prev_smaller_indices[idx];

        if (nums[idx] > threshold / width)
        {
            return width;
        }
    }

    return -1;
}
