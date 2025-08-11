#include <vector>
using namespace std;

int find_closest_three_sum(vector<int> &nums, int target)
{ // LeetCode Q.16.
    sort(nums.begin(), nums.end());
    int min_gap = numeric_limits<int>::max(), closest_3_sum = 0;

    int min_idx_2 = 1, idx_3 = nums.size() - 1;
    while (idx_3 > min_idx_2)
    {
        while (nums[min_idx_2 - 1] + nums[min_idx_2] + nums[idx_3] < target)
        {
            min_idx_2++;
            if (min_idx_2 == idx_3)
            {
                break;
            }
        }

        if (min_idx_2 >= 2)
        {
            int last_three_sum = nums[min_idx_2 - 2] + nums[min_idx_2 - 1] + nums[idx_3];
            int gap = abs(last_three_sum - target);
            if (gap < min_gap)
                min_gap = gap, closest_3_sum = last_three_sum;
        }

        int idx_1 = min_idx_2 - 1;
        for (int idx_2 = min_idx_2; idx_2 < idx_3; idx_2++)
        {
            if (idx_1 < 0)
                break;

            int two_sum = nums[idx_2] + nums[idx_3]; // Sum of nums 2 and 3.
            while (idx_1 >= 0)
            {
                if (idx_1 == 0 || nums[idx_1] + two_sum < target)
                {
                    int three_sum_1 = nums[idx_1 + 1] + two_sum;
                    int gap_1 = abs(three_sum_1 - target);
                    int three_sum_2 = nums[idx_1] + two_sum;
                    int gap_2 = abs(three_sum_2 - target);

                    if (min(gap_1, gap_2) < min_gap)
                        if (gap_1 < gap_2)
                        {
                            min_gap = gap_1, closest_3_sum = three_sum_1;
                        }
                        else
                        {
                            min_gap = gap_2, closest_3_sum = three_sum_2;
                        }
                    break;
                }
                idx_1--;
            }
        }

        idx_3--;
    }

    return closest_3_sum;
}
