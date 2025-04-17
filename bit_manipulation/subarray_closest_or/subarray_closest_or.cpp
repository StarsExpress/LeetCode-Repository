#include <vector>
#include <unordered_map>
#include <bitset>
using namespace std;

int count_closest_subarray_or(vector<int> &nums, int k)
{ // LeetCode Q.3171.
    int min_abs_diff = numeric_limits<int>::max();
    int subarray_or_value = 0;
    unordered_map<int, int> values2counts;

    int left_idx = 0;
    for (int right_idx = 0; right_idx < nums.size(); right_idx++)
    {
        bitset<30> bin_right_num(nums[right_idx]);

        int bit_idx = 0, bit_value = 1;
        while (bit_idx < 30)
        {
            if (bin_right_num[bit_idx] == 1)
            {
                values2counts[bit_value] += 1;
                if (values2counts[bit_value] == 1)
                    subarray_or_value += bit_value;
            }

            bit_value *= 2;
            bit_idx += 1;
        }

        while (left_idx < right_idx && subarray_or_value > k)
        {
            bitset<30> bin_left_num(nums[left_idx]);

            int bit_idx = 0, bit_value = 1;
            int left_num_deducted_values = 0;
            while (bit_idx < 30)
            {
                if (bin_left_num[bit_idx] == 1)
                {
                    values2counts[bit_value] -= 1;
                    if (values2counts[bit_value] == 0)
                        left_num_deducted_values += bit_value;
                }

                bit_value *= 2;
                bit_idx += 1;
            }

            subarray_or_value -= left_num_deducted_values;
            if (subarray_or_value <= k)
            {
                int abs_diff = subarray_or_value + left_num_deducted_values - k;
                if (abs_diff < min_abs_diff)
                    min_abs_diff = abs_diff;
            }

            left_idx += 1;
        }

        int abs_diff = abs(subarray_or_value - k);
        if (abs_diff == 0) // Early exit.
            return 0;
        if (abs_diff < min_abs_diff)
            min_abs_diff = abs_diff;
    }

    return min_abs_diff;
}
