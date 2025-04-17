#include <deque>
#include <vector>
using namespace std;

long long compute_subarrays_min_max_sum(vector<int> &nums, int k)
{ //  LeetCode Q.3430.
    long long subarrays_max_min_sum = 0;

    deque<vector<long long>> decreasing_stack; // Format: {idx, num, shares}.
    long long subarrays_max_sum = 0;
    deque<vector<long long>> increasing_stack; // Format: {idx, num, shares}.
    long long subarrays_min_sum = 0;

    int start_idx = 1 - k;
    for (int end_idx = 0; end_idx < nums.size(); end_idx++)
    {
        if (start_idx > 0) // Ensure both stacks have current subarrays' window.
        {
            decreasing_stack.front()[2] -= 1; // Decrement stack's 1st num shares by 1.
            subarrays_max_sum -= decreasing_stack.front()[1];
            if (decreasing_stack.front()[0] < start_idx)
                decreasing_stack.pop_front(); // Stack's 1st num out of window.

            increasing_stack.front()[2] -= 1; // Decrement stack's 1st num shares by 1.
            subarrays_min_sum -= increasing_stack.front()[1];
            if (increasing_stack.front()[0] < start_idx)
                increasing_stack.pop_front(); // Stack's 1st num out of window.
        }

        long long num = nums[end_idx];
        while (!decreasing_stack.empty() && decreasing_stack.back()[1] <= num)
        {
            subarrays_max_sum -= decreasing_stack.back()[1] * decreasing_stack.back()[2];
            decreasing_stack.pop_back();
        }

        int shares = min(end_idx + 1, k);
        if (!decreasing_stack.empty())
        {
            shares = end_idx - decreasing_stack.back()[0];
        }

        subarrays_max_sum += num * shares;
        subarrays_max_min_sum += subarrays_max_sum;
        decreasing_stack.push_back({end_idx, num, shares});

        while (!increasing_stack.empty() && increasing_stack.back()[1] >= num)
        {
            subarrays_min_sum -= increasing_stack.back()[1] * increasing_stack.back()[2];
            increasing_stack.pop_back();
        }

        shares = min(end_idx + 1, k);
        if (!increasing_stack.empty())
        {
            shares = end_idx - increasing_stack.back()[0];
        }

        subarrays_min_sum += num * shares;
        subarrays_max_min_sum += subarrays_min_sum;
        increasing_stack.push_back({end_idx, num, shares});

        start_idx++;
    }
    return subarrays_max_min_sum;
}
