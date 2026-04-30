#include <vector>
#include <unordered_map>
using namespace std;

int countGoodPartitions(vector<int> &nums) // LeetCode Q.2963.
{
    unordered_map<int, int> numsLastIndices; // Each num's last idx.

    for (int idx = 0; idx < nums.size(); idx++)
        numsLastIndices[nums[idx]] = idx;

    int windowsCount = 0; // Sliding window by three pointers.
    int leftIdx = 0, midIdx = 0, rightIdx = 0;

    while (rightIdx < nums.size())
    {
        int num = nums[midIdx];
        midIdx++; // Already visited.

        if (rightIdx < numsLastIndices[num])
        { // Num extends current window.
            rightIdx = numsLastIndices[num];
            continue;
        }

        if (midIdx >= rightIdx)
        {
            windowsCount++; // Current window is finalized.

            leftIdx = rightIdx + 1; // Search for another window, if possible.
            midIdx = leftIdx, rightIdx = leftIdx;
        }
    }

    int goodPartitions = 1;

    int power = windowsCount - 1, modulo = pow(10, 9) + 7;

    while (power > 0)
    {
        goodPartitions *= 2;
        goodPartitions %= modulo; // Must prevent overflow.
        power--;
    }

    return goodPartitions;
}
