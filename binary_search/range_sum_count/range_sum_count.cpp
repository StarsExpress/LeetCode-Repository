#include <vector>
#include <deque>
using namespace std;

int count_range_sum(vector<int> &nums, int lower, int upper)
{ // LeetCode Q.327.
    long long prefix_sum = 0;
    deque<long long> prefix_sums; // Use deque to speed up binary search.

    int bounded_range_sums = 0; // Count of range sums in [lower, upper].
    for (auto num : nums)
    {
        prefix_sum += num;
        if (lower <= prefix_sum && prefix_sum <= upper)
            bounded_range_sums++;

        // Targeted prefix sum x satisfies this condition.
        // prefix sum - upper <= target <= prefix sum - lower.
        int right_idx = upper_bound(
                            prefix_sums.begin(), prefix_sums.end(), prefix_sum - lower) -
                        prefix_sums.begin() - 1;

        int left_idx = lower_bound(
                           prefix_sums.begin(), prefix_sums.end(), prefix_sum - upper) -
                       prefix_sums.begin();

        bounded_range_sums += right_idx + 1 - left_idx;

        auto idx = upper_bound(prefix_sums.begin(), prefix_sums.end(), prefix_sum);
        prefix_sums.insert(idx, prefix_sum);
    }

    return bounded_range_sums;
}
