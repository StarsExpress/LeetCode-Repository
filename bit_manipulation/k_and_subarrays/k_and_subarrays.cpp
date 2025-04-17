#include <vector>
#include <unordered_map>
#include <bitset>
using namespace std;

long long count_limited_subarrays(vector<int> nums, int k)
{ // LeetCode Q.3209.
    unordered_map<int, int> values2counts;

    long long total_subarrays = 0;
    int start_idx = 0;
    for (int end_idx = 0; end_idx < nums.size(); end_idx++)
    {
        if (k > nums[end_idx])
        {                          // Subarrays ending at current num have AND values < k.
            values2counts.clear(); // Reset.
            start_idx = end_idx + 1;
            continue;
        }

        int subarray_and_value = 0;
        int subarray_len = end_idx + 1 - start_idx;

        bitset<30> bin_end_num(nums[end_idx]);
        int bit_idx = 0, bit_value = 1;
        while (bit_idx < 30)
        {
            if (bin_end_num[bit_idx] == 1)
            {
                values2counts[bit_value] += 1;
                if (values2counts[bit_value] == subarray_len) // A set bit.
                    subarray_and_value += bit_value;
            }

            bit_value *= 2;
            bit_idx += 1;
        }

        while (start_idx < end_idx && subarray_and_value < k)
        {
            subarray_len -= 1;

            bitset<30> bin_start_num(nums[start_idx]);
            int bit_idx = 0, bit_value = 1;
            while (bit_idx < 30)
            {
                if (values2counts.find(bit_value) != values2counts.end())
                {
                    if (bin_start_num[bit_idx] == 1)
                        values2counts[bit_value] -= 1;

                    if (bin_start_num[bit_idx] == 0)
                        if (values2counts[bit_value] == subarray_len)
                            subarray_and_value += bit_value; // A set bit.
                }

                bit_value *= 2;
                bit_idx += 1;
            }

            start_idx += 1;
        }

        total_subarrays += subarray_len;
    }

    return total_subarrays;
}

long long count_k_and_subarrays(vector<int> &nums, int k)
{
    return count_limited_subarrays(nums, k) - count_limited_subarrays(nums, k + 1);
}
