#include <vector>
#include <unordered_map>
#include <deque>
#include <stack>
using namespace std;

long long count_subarrays(vector<int> &nums)
{ // LeetCode Q.3113.
    unordered_map<int, deque<int>> nums2indices;

    vector<int> prev_bigger_indices(nums.size(), -1);
    stack<pair<int, int>> decreasing_stack; // Format: {idx, num}.

    long long subarrays_count = 0;
    for (int idx = 0; idx < nums.size(); idx++)
    {
        int num = nums[idx];
        if (nums2indices.find(num) == nums2indices.end())
            nums2indices[num] = {};
        nums2indices[num].push_back(idx);

        while (!decreasing_stack.empty())
        {
            auto [prev_idx, prev_num] = decreasing_stack.top();
            if (prev_num > num)
            {
                prev_bigger_indices[idx] = prev_idx;
                break;
            }
            decreasing_stack.pop();
        }
        decreasing_stack.push({idx, num});

        while (nums2indices[num].front() < prev_bigger_indices[idx])
        {
            nums2indices[num].pop_front();
        }

        subarrays_count += nums2indices[num].size();
    }

    return subarrays_count;
}
