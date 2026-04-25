#include <vector>
using namespace std;

int computeCircularMaxSubarraySum(vector<int> &nums)
{ // LeetCode Q.918.
    int arrayTotalSum = 0;
    int maxNum = nums.front();

    int posSubarraySum = 0, maxPosSum = 0;

    int negSubarraySum = 0, minNegSum = 0;

    for (int idx = 0; idx < nums.size(); idx++)
    {
        int num = nums[idx];
        if (num > maxNum)
            maxNum = num;

        arrayTotalSum += num;

        posSubarraySum += num;
        if (posSubarraySum > maxPosSum)
            maxPosSum = posSubarraySum;

        if (posSubarraySum <= 0) // Positive sum <= 0: reset subarray.
            posSubarraySum = 0;

        negSubarraySum += num;
        if (negSubarraySum < minNegSum)
            minNegSum = negSubarraySum;

        if (negSubarraySum >= 0) // Negative sum >= 0: reset subarray.
            negSubarraySum = 0;
    }

    if (maxPosSum == 0) // All numbers are non-positive.
        return maxNum;

    if (minNegSum == 0) // All numbers are non-negative.
        return arrayTotalSum;

    return max(arrayTotalSum - minNegSum, maxPosSum);
}
