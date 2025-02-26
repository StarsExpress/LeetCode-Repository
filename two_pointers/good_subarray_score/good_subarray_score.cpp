#include <vector>
using namespace std;

int find_max_score(vector<int> &nums, int k)
{ // LeetCode Q.1793.

    int subarray_min = nums[k]; // Base case: subarray of only num at kth idx.
    int max_subarray_score = nums[k];
    int left_idx = k;
    int right_idx = k;
    int width = 1;

    while (left_idx >= 0 && right_idx < nums.size())
    {
        int subarray_score = subarray_min * width;
        if (subarray_score > max_subarray_score)
        {
            max_subarray_score = subarray_score;
        }

        if (left_idx == 0 && right_idx == nums.size() - 1)
        {
            break;
        }

        if (left_idx == 0 && right_idx < nums.size() - 1)
        {
            right_idx += 1;
            width += 1;
        }

        if (left_idx > 0 && right_idx == nums.size() - 1)
        {
            left_idx -= 1;
            width += 1;
        }

        if (left_idx > 0 && right_idx < nums.size() - 1)
        { // Both sides can go.
            if (nums[left_idx - 1] > nums[right_idx + 1])
            {
                left_idx -= 1;
            }
            else
            {
                right_idx += 1;
            }
            width += 1;
        }

        if (min(nums[left_idx], nums[right_idx]) < subarray_min)
        {
            subarray_min = min(nums[left_idx], nums[right_idx]);
        }
    }

    return max_subarray_score;
}
