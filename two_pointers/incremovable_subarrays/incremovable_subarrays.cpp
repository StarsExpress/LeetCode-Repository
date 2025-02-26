#include <vector>
using namespace std;

long long count_incremovable_subarrays(vector<int> &nums)
{ // LeetCode Q.2972.
    int max_rising_prefix_len = 1;
    int idx = 0;
    while (idx < nums.size() - 1 && nums[idx] < nums[idx + 1])
    {
        max_rising_prefix_len += 1;
        idx += 1;
    }

    if (max_rising_prefix_len == nums.size())
    {
        // Base case: entire original array is increasing.
        return (1 + nums.size()) * nums.size() / 2;
    }

    int max_rising_suffix_len = 1;
    idx = nums.size() - 1;
    while (idx > 0 && nums[idx] > nums[idx - 1])
    {
        max_rising_suffix_len += 1;
        idx -= 1;
    }

    // Must use long long to prevent overflow!
    long long incremovable_subarrays = 1; // Incremovable: entire original array.
    // Incremovable: only non-empty suffixes.
    incremovable_subarrays += max_rising_prefix_len;
    // Incremovable: only non-empty prefixes.
    incremovable_subarrays += max_rising_suffix_len;

    int left_idx = 0;
    int right_idx = nums.size() - max_rising_suffix_len;
    while (left_idx < max_rising_prefix_len && right_idx < nums.size())
    { // Incremovable: non-empty subarray in the middle.
        while (nums[left_idx] >= nums[right_idx] && right_idx < nums.size() - 1)
        {
            right_idx += 1; // Find the next compatible non-empty suffix.
        }

        if (nums[left_idx] >= nums[right_idx])
        {
            break; // No compatible non-empty suffixes for remaining prefixes.
        }

        incremovable_subarrays += nums.size() - right_idx;
        left_idx += 1;
    }

    return incremovable_subarrays;
}
