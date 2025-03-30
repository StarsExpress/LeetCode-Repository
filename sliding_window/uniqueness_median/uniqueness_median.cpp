#include <vector>
#include <unordered_map>
using namespace std;

int find_uniqueness_median(vector<int> &nums)
{ // LeetCode Q.3134.
    long long max_total_subarrays = nums.size() * (nums.size() + 1) / 2;
    // Max total subarrays is even: take its exact half as the median.
    long long subarrays_median = (max_total_subarrays + 1) / 2;

    unordered_map<int, int> nums2counts;
    int min_median = 1, max_median = nums.size();
    while (min_median <= max_median)
    {
        int mid_median = (min_median + max_median) / 2;

        long long subarrays_count = 0;
        nums2counts.clear(); // Reset before sliding window search.
        int start_idx = 0;

        for (int end_idx = 0; end_idx < nums.size(); end_idx++)
        {
            nums2counts[nums[end_idx]]++;
            while (nums2counts.size() > mid_median)
            {
                nums2counts[nums[start_idx]]--;
                if (nums2counts[nums[start_idx]] == 0)
                {
                    nums2counts.erase(nums[start_idx]);
                }

                start_idx++;
            }
            // Count of subarrays ending at end idx w/ uniqueness <= mid median.
            subarrays_count += end_idx + 1 - start_idx;
        }

        if (subarrays_count == subarrays_median)
        {
            return mid_median;
        }
        else if (subarrays_count < subarrays_median)
        {
            min_median = mid_median + 1;
        }
        else
        {
            max_median = mid_median - 1;
        }
    }

    return min_median;
}
