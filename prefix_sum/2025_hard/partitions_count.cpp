#include <vector>
#include <unordered_map>
using namespace std;

int countMaxPartitions(vector<int> &nums, int k)
{ // LeetCode Q.2025.
    // Sums related variables must use long long to prevent overflow.
    // Counts and indices related variables can use int.
    long long totalSum = 0;
    for (auto num : nums)
        totalSum += num;

    long long maxPartitionWays = 0, prefixSum = nums[0];

    for (int pivot = 1; pivot < nums.size(); pivot++)
    {
        if (2 * prefixSum == totalSum)
            maxPartitionWays += 1; // A natural pivot.

        prefixSum += nums[pivot];
    }

    unordered_map<long long, int> rightSideDiffs;
    long long suffixSum = 0;

    for (int idx = nums.size() - 1; idx >= 1; idx--)
    {
        suffixSum += nums[idx];
        long long diff = totalSum - 2 * suffixSum; // Diff = prefix sum - suffix sum.
        rightSideDiffs[diff]++;
    }

    unordered_map<long long, int> leftSideDiffs;
    prefixSum = 0;

    for (int idx = 0; idx < nums.size(); idx++)
    {
        long long partitionWays = 0;

        long long rightChange = nums[idx] - k;
        if (rightSideDiffs.find(rightChange) != rightSideDiffs.end())
            partitionWays += rightSideDiffs[rightChange];

        long long leftChange = k - nums[idx];
        if (leftSideDiffs.find(leftChange) != leftSideDiffs.end())
            partitionWays += leftSideDiffs[leftChange];

        if (partitionWays > maxPartitionWays)
            maxPartitionWays = partitionWays;

        prefixSum += nums[idx];
        if (idx > 0) // Suffix doesn't cover num at 0th idx.
            suffixSum -= nums[idx];

        long long diff = prefixSum - suffixSum;
        leftSideDiffs[diff]++;
        rightSideDiffs[diff]--;
    }

    return maxPartitionWays;
}
