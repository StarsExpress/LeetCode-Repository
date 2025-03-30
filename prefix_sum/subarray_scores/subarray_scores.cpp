#include <vector>
#include <queue>
using namespace std;

long long count_subarray_scores(vector<int> &nums, long long k)
{ // LeetCode Q.2302.
    long long total_subarrays = 0;

    long long prefix_sum = 0;          // Prefix sum from 0th to ith num.
    queue<pair<int, long long>> queue; // Format: {idx, prefix sum}.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        prefix_sum += nums[idx];

        while (!queue.empty())
        {
            int subarray_len = idx - queue.front().first;
            long long subarray_sum = prefix_sum - queue.front().second;
            if (subarray_sum * subarray_len < k)
            {
                break;
            }
            queue.pop();
        }

        total_subarrays += queue.size();

        if (prefix_sum * (idx + 1) < k)
        {
            total_subarrays += 1;
        }

        queue.push({idx, prefix_sum});
    }

    return total_subarrays;
}
