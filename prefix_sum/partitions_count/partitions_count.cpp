#include <vector>
#include <unordered_map>
using namespace std;

int count_max_partitions(vector<int> &nums, int k)
{ // LeetCode Q.2025.
    // Sums related variables must use long long to prevent overflow.
    // Counts and indices related variables can use int.
    long long total_sum = 0;
    for (auto num : nums)
    {
        total_sum += num;
    }

    long long max_partition_ways = 0, prefix_sum = nums[0];
    for (int pivot = 1; pivot < nums.size(); pivot++)
    {
        if (2 * prefix_sum == total_sum)
        {
            max_partition_ways += 1; // A natural pivot.
        }
        prefix_sum += nums[pivot];
    }

    unordered_map<long long, int> right_side_diffs;
    long long suffix_sum = 0;
    for (int idx = nums.size() - 1; idx >= 1; idx--)
    {
        suffix_sum += nums[idx];
        long long diff = total_sum - 2 * suffix_sum; // Diff = prefix sum - suffix sum.
        right_side_diffs[diff]++;
    }

    unordered_map<long long, int> left_side_diffs;
    prefix_sum = 0;
    for (int idx = 0; idx < nums.size(); idx++)
    {
        long long partition_ways = 0;

        long long right_change = nums[idx] - k;
        if (right_side_diffs.find(right_change) != right_side_diffs.end())
        {
            partition_ways += right_side_diffs[right_change];
        }
        long long left_change = k - nums[idx];
        if (left_side_diffs.find(left_change) != left_side_diffs.end())
        {
            partition_ways += left_side_diffs[left_change];
        }

        if (partition_ways > max_partition_ways)
        {
            max_partition_ways = partition_ways;
        }

        prefix_sum += nums[idx];
        if (idx > 0)
        { // Suffix doesn't cover num at 0th idx.
            suffix_sum -= nums[idx];
        }

        long long diff = prefix_sum - suffix_sum;
        left_side_diffs[diff]++;
        right_side_diffs[diff]--;
    }

    return max_partition_ways;
}
