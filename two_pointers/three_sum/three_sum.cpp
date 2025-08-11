#include <vector>
using namespace std;

vector<vector<int>> threeSum(vector<int> &nums)
{ // LeetCode Q.15.
    sort(nums.begin(), nums.end());
    vector<vector<int>> distinct_triplets;

    int min_idx_2 = 1, idx_3 = nums.size() - 1;
    while (idx_3 > min_idx_2)
    {
        if (idx_3 < nums.size() - 1 && nums[idx_3] == nums[idx_3 + 1])
        {
            idx_3--;
            continue;
        }

        while (nums[min_idx_2 - 1] + nums[min_idx_2] + nums[idx_3] < 0)
        {
            min_idx_2++;
            if (min_idx_2 == idx_3)
            {
                break;
            }
        }

        int idx_1 = min_idx_2 - 1;
        for (int idx_2 = min_idx_2; idx_2 < idx_3; idx_2++)
        {
            if (min_idx_2 < idx_2 && nums[idx_2 - 1] == nums[idx_2])
            {
                continue;
            }

            int target_num_1 = -nums[idx_3] - nums[idx_2];
            while (idx_1 >= 0)
            {
                if (nums[idx_1] < target_num_1)
                    break;

                if (nums[idx_1] == target_num_1)
                { // If idx_1, idx_2, idx_3 and idx_1, idx_2 + 1, idx_3 are answers, take the former.
                    distinct_triplets.push_back({nums[idx_1], nums[idx_2], nums[idx_3]});
                    idx_1--; // Prevent idx_2 + 1 from pairing w/ idx_1.
                    break;
                }

                idx_1--;
            }
        }

        idx_3--;
    }

    return distinct_triplets;
}
