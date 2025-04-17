#include <vector>
using namespace std;

long long count_subarray_scores(vector<int> &nums, long long k)
{ // LeetCode Q.2302.
    long long total_subarrays = 0;
    long long subarray_sum = 0;

    int start_idx = 0;
    for (int end_idx = 0; end_idx < nums.size(); end_idx++)
    {
        subarray_sum += nums[end_idx];
        long long score = subarray_sum * (end_idx + 1 - start_idx);

        while (score >= k && start_idx <= end_idx)
        {
            subarray_sum -= nums[start_idx];
            start_idx++;
            score = subarray_sum * (end_idx + 1 - start_idx);
        }

        total_subarrays += end_idx + 1 - start_idx;
    }

    return total_subarrays;
}
