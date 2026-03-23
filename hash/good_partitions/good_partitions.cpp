#include <vector>
#include <unordered_map>
using namespace std;

int countGoodPartitions(vector<int> &nums)
{ // LeetCode Q.2963.
    // Each num's 1st and last occurred indices.
    unordered_map<int, pair<int, int>> nums2BoundaryIndices;

    for (int idx = 0; idx < nums.size(); idx++)
    {
        if (nums2BoundaryIndices.find(nums[idx]) == nums2BoundaryIndices.end())
            nums2BoundaryIndices[nums[idx]] = {idx, idx};

        nums2BoundaryIndices[nums[idx]].second = idx;
    }

    int segments = 0;
    int lastSegmentLeftIdx = -1, lastSegmentRightIdx = -1;

    for (int idx = 0; idx < nums.size(); idx++)
    {
        auto [leftIdx, rightIdx] = nums2BoundaryIndices[nums[idx]];
        if (lastSegmentRightIdx < leftIdx)
        { // A new segment is formed.
            segments += 1;
            lastSegmentLeftIdx = leftIdx, lastSegmentRightIdx = rightIdx;
            continue;
        }

        if (lastSegmentRightIdx < rightIdx) // Last segment expands.
            lastSegmentRightIdx = rightIdx;
    }

    long long partitions = 1, modulo = pow(10, 9) + 7;
    while (segments > 1)
    { // Partitions = 2 ** (segments - 1).
        partitions *= 2;
        partitions %= modulo; // Required to control size.
        segments--;
    }

    return partitions;
}
