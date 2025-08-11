#include <deque>
#include <vector>
using namespace std;

long long compute_max_min_sum(vector<int> &nums, int k)
{ //  LeetCode Q.3430.
    long long total_max_sum = 0, total_min_sum = 0;
    long long window_max_shares = 0, window_min_shares = 0;
    long long window_max_sum = 0, window_min_sum = 0;

    deque<pair<int, long long>> max_stack, min_stack; // Format: {num idx, num shares}.
    for (int idx = 0; idx < nums.size(); idx++)
    {
        long long num = nums[idx];
        while (!max_stack.empty() && nums[max_stack.back().first] < num)
        {
            window_max_shares -= max_stack.back().second;
            window_max_sum -= nums[max_stack.back().first] * max_stack.back().second;
            max_stack.pop_back();
        }

        long long max_shares = min(idx + 1, k);
        if (!max_stack.empty())
            max_shares = idx - max_stack.back().first;

        max_stack.push_back({idx, max_shares});
        window_max_shares += max_shares;
        window_max_sum += num * max_shares;

        if (window_max_shares > k)
        {
            window_max_shares--;
            window_max_sum -= nums[max_stack.front().first];
            max_stack.front().second--;
            if (max_stack.front().second == 0)
                max_stack.pop_front();
        }
        total_max_sum += window_max_sum;

        while (!min_stack.empty() && nums[min_stack.back().first] > num)
        {
            window_min_shares -= min_stack.back().second;
            window_min_sum -= nums[min_stack.back().first] * min_stack.back().second;
            min_stack.pop_back();
        }

        long long min_shares = min(idx + 1, k);
        if (!min_stack.empty())
            min_shares = idx - min_stack.back().first;

        min_stack.push_back({idx, min_shares});
        window_min_shares += min_shares;
        window_min_sum += num * min_shares;

        if (window_min_shares > k)
        {
            window_min_shares--;
            window_min_sum -= nums[min_stack.front().first];
            min_stack.front().second--;
            if (min_stack.front().second == 0)
                min_stack.pop_front();
        }
        total_min_sum += window_min_sum;
    }

    return total_max_sum + total_min_sum;
}
