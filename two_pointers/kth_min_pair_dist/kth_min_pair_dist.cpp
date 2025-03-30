#include <vector>
using namespace std;

int find_kth_min_pair_dist(vector<int> &nums, int k)
{ // LeetCode Q.719.
    sort(nums.begin(), nums.end());

    int kth_min_dist = 0;
    int min_dist = 0, max_dist = nums.back() - nums.front();
    while (min_dist <= max_dist)
    {
        int mid_dist = (min_dist + max_dist) / 2;
        int count = 0; // Count of pairs with dist <= mid dist.

        // Candidate: max among distances that don't exceed mid dist.
        int candidate = min_dist, left_idx = 0;
        for (int right_idx = 0; right_idx < nums.size(); right_idx++)
        {
            while (nums[right_idx] - nums[left_idx] > mid_dist)
            {
                left_idx++;
            }

            if (nums[right_idx] - nums[left_idx] > candidate)
            {
                candidate = nums[right_idx] - nums[left_idx];
            }
            count += right_idx - left_idx;
        }

        if (count < k)
        {
            min_dist = mid_dist + 1;
            continue;
        }

        kth_min_dist = candidate; // Count >= k: candidate might be the kth min dist.
        if (count == k)
        {
            break;
        }
        max_dist = mid_dist - 1;
    }

    return kth_min_dist;
}
