#include <vector>
#include <algorithm>
using namespace std;

int maximizeFrequencyScore(vector<int> &nums, long long limit)
{ // LeetCode Q.2968.
    sort(nums.begin(), nums.end());
    vector<long long> prefixSums;

    for (auto num : nums)
    {
        if (prefixSums.empty())
        {
            prefixSums.push_back(num);
            continue;
        }
        prefixSums.push_back(prefixSums.back() + num);
    }

    int maxScore = 1; // Base case.
    long long operations = 0;

    long long leftIdx = 0, midIdx = 0; // Set long long to prevent overflow.

    for (long long rightIdx = 0; rightIdx < nums.size(); rightIdx++)
    {
        bool firstWhile = true;
        do
        {
            if (firstWhile == false)
                leftIdx++; // Since 2nd while, the subarray left bound rises.

            // Always optimal to change all nums to the num at mid idx.
            midIdx = (leftIdx + rightIdx) / 2;

            operations = prefixSums[rightIdx] - prefixSums[midIdx];
            operations -= nums[midIdx] * (rightIdx - midIdx);

            operations += nums[midIdx] * (midIdx - leftIdx);

            if (midIdx > 0)
                operations -= prefixSums[midIdx - 1];

            if (leftIdx > 0)
                operations += prefixSums[leftIdx - 1];

            firstWhile = false;
        } while (limit < operations && leftIdx < rightIdx);

        int score = rightIdx + 1 - leftIdx;
        if (score > maxScore)
            maxScore = score;
    }

    return maxScore;
}
