#include <vector>
#include <unordered_map>
using namespace std;

int countMaxPartitions(vector<int> &nums, int k) // LeetCode Q.2025.
{
    long long totalSum = 0; // Prevents overflow.
    for (auto num : nums)
        totalSum += num;

    // Key: diff = prefix sum - suffix sum.
    unordered_map<long long, int> leftDiffCounts, rightDiffCounts;

    // Default to natural value: leave entire array unchanged.
    int maxPartitionWays = 0;

    long long prefixSum = 0;
    for (int pivotIdx = 1; pivotIdx < nums.size(); pivotIdx++)
    {
        prefixSum += nums[pivotIdx - 1];
        long long suffixSum = totalSum - prefixSum;
        rightDiffCounts[prefixSum - suffixSum]++;

        // Born as a great partition. No need to change.
        if (prefixSum == suffixSum)
            maxPartitionWays++;
    }

    prefixSum = 0; // Reset to let next for loop sweep again.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        int num = nums[idx];
        prefixSum += num;

        int partitionWays = 0;

        // Change prefix side: replace num with k.
        if (idx < nums.size() - 1) // Vector back num can't join prefix side.
            partitionWays += rightDiffCounts[num - k];

        // Change suffix side: replace num with k.
        if (idx > 0) // Vector front num can't join suffix side.
            partitionWays += leftDiffCounts[k - num];

        if (partitionWays > maxPartitionWays)
            maxPartitionWays = partitionWays;

        long long diff = 2 * prefixSum - totalSum; // Prefix - suffix.

        // For future indices, this diff is only available as left side.
        leftDiffCounts[diff]++;
        if (rightDiffCounts[diff] > 0)
            rightDiffCounts[diff]--;
    }

    return maxPartitionWays;
}
