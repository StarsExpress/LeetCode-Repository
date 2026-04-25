#include <vector>
#include <algorithm>
using namespace std;

int findKthMinPairDist(vector<int> &nums, int k) // LeetCode Q.719.
{
    sort(nums.begin(), nums.end());

    int kthMinDist = 0;
    int minDist = 0, maxDist = nums.back() - nums.front();

    while (minDist <= maxDist)
    {
        int midDist = (minDist + maxDist) / 2;
        int count = 0; // Count of pairs with dist <= mid dist.

        // Candidate: max among distances that don't exceed mid dist.
        int candidate = minDist, leftIdx = 0;

        for (int rightIdx = 0; rightIdx < nums.size(); rightIdx++)
        {
            while (nums[rightIdx] - nums[leftIdx] > midDist)
                leftIdx++;

            if (nums[rightIdx] - nums[leftIdx] > candidate)
                candidate = nums[rightIdx] - nums[leftIdx];

            count += rightIdx - leftIdx;
        }

        if (count < k)
        {
            minDist = midDist + 1;
            continue;
        }

        kthMinDist = candidate; // Count >= k: candidate might be the kth min dist.
        if (count == k)
            break;

        maxDist = midDist - 1;
    }

    return kthMinDist;
}
