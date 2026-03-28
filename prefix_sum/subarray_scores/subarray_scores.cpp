#include <vector>
using namespace std;

long long countSubarrayScores(vector<int> &nums, long long k)
{ // LeetCode Q.2302.
    long long totalSubarrays = 0;
    long long subarraySum = 0;

    int startIdx = 0;
    for (int endIdx = 0; endIdx < nums.size(); endIdx++)
    {
        subarraySum += nums[endIdx];
        long long score = subarraySum * (endIdx + 1 - startIdx);

        while (score >= k && startIdx <= endIdx)
        {
            subarraySum -= nums[startIdx];
            startIdx++;
            score = subarraySum * (endIdx + 1 - startIdx);
        }

        totalSubarrays += endIdx + 1 - startIdx;
    }

    return totalSubarrays;
}
