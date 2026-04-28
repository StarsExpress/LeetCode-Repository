#include <vector>
#include <unordered_map>
using namespace std;

int countSubarrays(vector<int> &nums, int k)
{ // LeetCode Q.2488.
    int medianKSubarrays = 0;
    int kCount = 0, prefixSum = 0;

    unordered_map<int, int> sumsCounts;

    // Keys: prefix sums. Values: {max k count, count of such prefix sums}.
    unordered_map<int, vector<int>> sumsKCounts;

    for (auto num : nums)
    {
        if (num == k)
            kCount += 1;

        if (num < k)
            prefixSum -= 1;

        if (num > k)
            prefixSum += 1;

        if (prefixSum == 0 || prefixSum == 1)
        {
            if (kCount > 0) // Array from 0th to current num has median k.
                medianKSubarrays += 1;
        }

        for (auto pairingSum : {prefixSum - 1, prefixSum})
        {
            if (sumsCounts.find(pairingSum) != sumsCounts.end())
            {
                medianKSubarrays += sumsCounts[pairingSum];

                // Ensure k is in subarray.
                if (sumsKCounts[pairingSum][0] == kCount)
                    medianKSubarrays -= sumsKCounts[pairingSum][1];
            }
        }

        if (sumsCounts.find(prefixSum) == sumsCounts.end())
        {
            sumsCounts[prefixSum] = 0;
            sumsKCounts[prefixSum] = {kCount, 0};
        }

        sumsCounts[prefixSum] += 1;

        if (sumsKCounts[prefixSum][0] < kCount) // Reset max k count of current prefix sum.
            sumsKCounts[prefixSum] = {kCount, 0};

        sumsKCounts[prefixSum][1] += 1;
    }

    return medianKSubarrays;
}
