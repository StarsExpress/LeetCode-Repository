#include <vector>
#include <unordered_map>
using namespace std;

int count_subarrays(vector<int> &nums, int k)
{ // LeetCode Q.2488.
    int median_k_subarrays = 0;
    int k_count = 0, prefix_sum = 0;

    unordered_map<int, int> sums2counts;

    // Keys: prefix sums. Values: {max k count, count of such prefix sums}.
    unordered_map<int, vector<int>> sums2k_counts;

    for (auto num : nums)
    {
        if (num == k)
        {
            k_count += 1;
        }
        if (num < k)
        {
            prefix_sum -= 1;
        }
        if (num > k)
        {
            prefix_sum += 1;
        }

        if (prefix_sum == 0 || prefix_sum == 1)
        {
            if (k_count > 0)
            { // Array from 0th to current num has median k.
                median_k_subarrays += 1;
            }
        }

        for (auto pairing_sum : {prefix_sum - 1, prefix_sum})
        {
            if (sums2counts.find(pairing_sum) != sums2counts.end())
            {
                median_k_subarrays += sums2counts[pairing_sum];

                // Ensure k is in subarray.
                if (sums2k_counts[pairing_sum][0] == k_count)
                {
                    median_k_subarrays -= sums2k_counts[pairing_sum][1];
                }
            }
        }

        if (sums2counts.find(prefix_sum) == sums2counts.end())
        {
            sums2counts[prefix_sum] = 0;
            sums2k_counts[prefix_sum] = {k_count, 0};
        }
        sums2counts[prefix_sum] += 1;

        if (sums2k_counts[prefix_sum][0] < k_count)
        { // Reset max k count of current prefix sum.
            sums2k_counts[prefix_sum] = {k_count, 0};
        }
        sums2k_counts[prefix_sum][1] += 1;
    }

    return median_k_subarrays;
}
