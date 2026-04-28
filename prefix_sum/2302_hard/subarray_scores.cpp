#include <vector>
using namespace std;

long long countSubarrayScores(vector<int> &nums, long long k) // LeetCode Q.2302.
{
    long long lessThanKSubarraysCount = 0; // Long long prevents overflow.

    long long subarraySum = 0; // Long long prevents overflow.

    int leftIdx = 0;
    for (int rightIdx = 0; rightIdx < nums.size(); rightIdx++)
    {
        subarraySum += nums[rightIdx];

        while (subarraySum * (rightIdx + 1 - leftIdx) >= k)
        {
            subarraySum -= nums[leftIdx];
            leftIdx++;
        }

        lessThanKSubarraysCount += rightIdx + 1 - leftIdx;
    }

    return lessThanKSubarraysCount;
}
