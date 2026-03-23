#include <vector>
using namespace std;

int computeCircularMaxSubarraySum(vector<int> &nums)
{ // LeetCode Q.918.
    int array_total_sum = 0;
    int max_num = nums.front();

    int pos_subarray_sum = 0, max_pos_sum = 0;

    int neg_subarray_sum = 0, min_neg_sum = 0;

    int total_nums = nums.size();

    for (int idx = 0; idx < total_nums; idx++)
    {
        int num = nums[idx];
        array_total_sum += num;
        if (num > max_num)
            max_num = num;

        // Positive sum <= 0: reset subarray.
        if (pos_subarray_sum <= 0)
            pos_subarray_sum = 0;

        pos_subarray_sum += num;
        if (pos_subarray_sum > max_pos_sum)
            max_pos_sum = pos_subarray_sum;

        // Front and last nums are excluded by negative sum subarray.
        if (0 < idx && idx < total_nums - 1)
        {
            // Negative sum >= 0: reset subarray.
            if (neg_subarray_sum >= 0)
                neg_subarray_sum = 0;

            neg_subarray_sum += num;
            if (neg_subarray_sum < min_neg_sum)
                min_neg_sum = neg_subarray_sum;
        }
    }

    if (max_num <= 0)
        return max_num; // All numbers are not positive.

    return max(array_total_sum - min_neg_sum, max_pos_sum);
}
