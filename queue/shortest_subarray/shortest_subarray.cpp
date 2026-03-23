#include <vector>
#include <queue>
using namespace std;

int shortestSubarray(vector<int> &nums, int k) // LeetCode Q.862.
{
    int min_len = nums.size() + 1;
    long long subarray_sum = 0; // Avoid subarray sum overflow by long long.

    deque<pair<long long, int>> queue; // Format: {subarray sum, subarray len}.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        if (nums[idx] >= k)
            return 1; // Base case.

        subarray_sum += nums[idx];

        // Subarray from 0th to (idx)th idx.
        if (subarray_sum >= k && idx + 1 < min_len)
            min_len = idx + 1;

        // Subarrays from (queue[0][1] + 1)th idx to (idx)th idx.
        while (!queue.empty() && queue.front().first <= subarray_sum - k)
        {
            if (idx + 1 - queue.front().second < min_len)
                min_len = idx + 1 - queue.front().second;

            // Later subarrays can't reset record with this past subarray.
            queue.pop_front();
        }

        // Make queue's subarray sums smaller if possible.
        while (!queue.empty() && queue.back().first >= subarray_sum)
            queue.pop_back();
        queue.push_back({subarray_sum, idx + 1});
    }

    if (min_len == nums.size() + 1)
        return -1;
    return min_len;
}
