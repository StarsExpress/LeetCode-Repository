#include <deque>
#include <vector>
using namespace std;

long long compute_max_min_sum(vector<int> &nums, int k)
{ //  LeetCode Q.3430.
    long long total_max_min_sum = 0;
    long long window_max_sum = 0, window_min_sum = 0;

    // Format: {idx, num, shares}. Use long long to prevent overflow.
    deque<tuple<int, int, long long>> max_stack, min_stack;

    for (int end_idx = 0; end_idx < nums.size(); end_idx++)
    {
        int start_idx = max(0, end_idx - k + 1);

        // Window start idx slides by 1: must update stacks' info.
        if (start_idx > 0)
        {
            get<2>(max_stack.front())--; // Decrement stack's front num shares.
            window_max_sum -= get<1>(max_stack.front());

            // Front num out of window.
            if (get<0>(max_stack.front()) < start_idx)
                max_stack.pop_front();

            get<2>(min_stack.front())--; // Decrement stack's front num shares.
            window_min_sum -= get<1>(min_stack.front());

            // Front num out of window.
            if (get<0>(min_stack.front()) < start_idx)
                min_stack.pop_front();
        }

        long long num = nums[end_idx];

        while (!max_stack.empty() && get<1>(max_stack.back()) <= num)
        {
            window_max_sum -= get<1>(max_stack.back()) * get<2>(max_stack.back());
            max_stack.pop_back();
        }

        long long max_shares = min(end_idx + 1, k);
        if (!max_stack.empty())
            max_shares = end_idx - get<0>(max_stack.back());

        max_stack.push_back({end_idx, num, max_shares});
        window_max_sum += num * max_shares;

        while (!min_stack.empty() && get<1>(min_stack.back()) >= num)
        {
            window_min_sum -= get<1>(min_stack.back()) * get<2>(min_stack.back());
            min_stack.pop_back();
        }

        long long min_shares = min(end_idx + 1, k);
        if (!min_stack.empty())
            min_shares = end_idx - get<0>(min_stack.back());

        min_stack.push_back({end_idx, num, min_shares});
        window_min_sum += num * min_shares;

        total_max_min_sum += window_max_sum + window_min_sum;
    }

    return total_max_min_sum;
}
