#include <vector>
using namespace std;

long long countBoundedSubarrays(vector<int> &nums, int minK, int maxK)
{ // LeetCode Q.2444.
    long long boundedSubarraysCount = 0;

    int prevMinIdx = -1, prevMaxIdx = -1;

    int leftIdx = 0;
    for (int rightIdx = 0; rightIdx < nums.size(); rightIdx++)
    {
        int num = nums[rightIdx];

        if (num < minK || num > maxK)
        { // Reset.
            prevMinIdx = -1, prevMaxIdx = -1;
            leftIdx = rightIdx + 1;
            continue;
        }

        if (num == maxK)
            prevMaxIdx = rightIdx;
        if (num == minK)
            prevMinIdx = rightIdx;

        if (min(prevMinIdx, prevMaxIdx) >= 0)
            boundedSubarraysCount += min(prevMinIdx, prevMaxIdx) + 1 - leftIdx;
    }

    return boundedSubarraysCount;
}
