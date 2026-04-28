#include <unordered_map>
#include <vector>
using namespace std;

int countKSumSubarrays(vector<int> &nums, int k) // LeetCode Q.560.
{
    unordered_map<int, int> prefixSumCounts;
    int prefixSum = 0;

    int kSumSubarraysCount = 0;

    for (auto num : nums)
    {
        prefixSum += num;

        kSumSubarraysCount += prefixSumCounts[prefixSum - k];

        if (prefixSum == k)
            kSumSubarraysCount++;

        prefixSumCounts[prefixSum]++;
    }

    return kSumSubarraysCount;
}
