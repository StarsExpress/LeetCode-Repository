#include <vector>
#include <stack>
using namespace std;

vector<int> find_second_next_greater(vector<int> &nums) // LeetCode Q.2454.
{
    vector<int> secondNextGreater(nums.size(), -1);

    stack<pair<int, int>> stackOne, stackTwo; // Format: {num, idx}.
    vector<pair<int, int>> transporter;       // Format: {num, idx}.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        while (!stackTwo.empty() && stackTwo.top().first < nums[idx])
        {
            int past_idx = stackTwo.top().second;
            secondNextGreater[past_idx] = nums[idx];
            stackTwo.pop();
        }

        while (!stackOne.empty() && stackOne.top().first < nums[idx])
        {
            transporter.push_back(stackOne.top()); // Keep decreasing monotonicity.
            stackOne.pop();
        }

        while (!transporter.empty())
        {
            stackTwo.push(transporter.back());
            transporter.pop_back();
        }

        stackOne.push({nums[idx], idx});
    }
    return secondNextGreater;
}