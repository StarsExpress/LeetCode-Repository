#include <vector>
#include <unordered_map>
using namespace std;

int count_limited_subarrays(vector<int> &nums, int distinction_limit)
{
    int total_subarrays = 0;

    unordered_map<int, int> nums2counts;
    int left_idx = 0;
    for (int right_idx = 0; right_idx < nums.size(); right_idx++)
    {
        nums2counts[nums[right_idx]]++;
        while (nums2counts.size() > distinction_limit)
        {
            nums2counts[nums[left_idx]]--;
            if (nums2counts[nums[left_idx]] == 0)
            {
                nums2counts.erase(nums[left_idx]);
            }
            left_idx++;
        }

        total_subarrays += right_idx + 1 - left_idx;
    }
    return total_subarrays;
}

int count_k_distinct_subarrays(vector<int> &nums, int k)
{ // LeetCode Q.992.
    return count_limited_subarrays(nums, k) - count_limited_subarrays(nums, k - 1);
}
