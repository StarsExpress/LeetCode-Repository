#include <vector>
#include <stack>
using namespace std;

vector<int> find_second_next_greater(vector<int> &nums) // LeetCode Q.2454.
{
    vector<int> second_next_greater(nums.size(), -1);

    stack<pair<int, int>> stack_1, stack_2; // Format: {num, idx}.
    vector<pair<int, int>> transporter;     // Format: {num, idx}.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        while (!stack_2.empty() && stack_2.top().first < nums[idx])
        {
            int past_idx = stack_2.top().second;
            second_next_greater[past_idx] = nums[idx];
            stack_2.pop();
        }

        while (!stack_1.empty() && stack_1.top().first < nums[idx])
        {
            transporter.push_back(stack_1.top()); // Keep decreasing monotonicity.
            stack_1.pop();
        }

        while (!transporter.empty())
        {
            stack_2.push(transporter.back());
            transporter.pop_back();
        }

        stack_1.push({nums[idx], idx});
    }
    return second_next_greater;
}