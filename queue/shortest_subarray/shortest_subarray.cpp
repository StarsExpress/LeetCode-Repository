#include <vector>
#include <queue>
using namespace std;

int shortestSubarray(vector<int> &nums, int k) // LeetCode Q.862.
{
    // Find the shortest subarray length with sum >= target.
    int min_len = numeric_limits<int>::max();
    long long subarray_sum = 0; // Avoid subarray sum overflow by long long.

    // Subarray sum decreasing monotonic queue.
    deque<pair<long long, int>> queue; // Format: {subarray sum, subarray len}.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        if (nums[idx] >= k)
            return 1; // Base case.

        subarray_sum += nums[idx];
        if (subarray_sum >= k && idx + 1 < min_len)
            min_len = idx + 1; // Subarray from 0th to (idx)th idx.

        // Subarrays from (queue[0][1] + 1)th idx to (idx)th idx.
        while (!queue.empty() && queue.front().first <= subarray_sum - k)
        {
            if (idx + 1 - queue.front().second < min_len)
            {
                min_len = idx + 1 - queue.front().second;
            }
            // Later subarrays can't reset record with this past subarray.
            queue.pop_front();
        }

        // Increase probability of meeting k with shorter subarrays.
        while (!queue.empty() && queue.back().first >= subarray_sum)
        {
            queue.pop_back(); // Make queue's subarray sums smaller if possible.
        }
        queue.push_back({subarray_sum, idx + 1});
    }

    if (min_len == numeric_limits<int>::max())
        return -1;
    return min_len;
}
