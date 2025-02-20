#include <iostream>
#include <vector>
#include <list>
using namespace std;

vector<int> find_second_next_greater(vector<int> &nums) // LeetCode Q.2454.
{
    vector<int> second_next_greater(nums.size(), -1);
    // Decreasing monotonic stacks format: {num, idx}.
    list<pair<int, int>> stack_2;
    list<pair<int, int>> stack_1;

    // Decreasing monotonic list: transport stack 1 tuples to stack 2.
    list<pair<int, int>> transporter; // Format: {num, idx}.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        while (!stack_2.empty() && stack_2.back().first < nums[idx])
        {
            int past_idx = stack_2.back().second;
            second_next_greater[past_idx] = nums[idx];
            stack_2.pop_back();
        }

        while (!stack_1.empty() && stack_1.back().first < nums[idx])
        {
            transporter.push_front(stack_1.back()); // Keep decreasing monotonicity.
            stack_1.pop_back();
        }
        stack_2.splice(stack_2.end(), transporter);

        stack_1.push_back({nums[idx], idx});
    }
    return second_next_greater;
}