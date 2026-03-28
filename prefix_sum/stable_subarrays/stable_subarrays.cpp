#include <vector>
using namespace std;

vector<long long> countStableSubarrays(vector<int> &nums, vector<vector<int>> &queries)
{ // LeetCode Q.3748.
    vector<long long> prefixSumCounts;
    vector<int> startIndices;

    int streakStartIdx = 0;

    for (int idx = 0; idx < nums.size(); idx++)
    {
        int num = nums[idx];

        if (idx > 0 && num < nums[idx - 1])
            streakStartIdx = idx;
        startIndices.push_back(streakStartIdx);

        if (prefixSumCounts.empty())
            prefixSumCounts.push_back(0);

        else
            prefixSumCounts.push_back(prefixSumCounts.back());

        prefixSumCounts.back() += idx + 1 - streakStartIdx;
    }

    vector<long long> answers;
    for (auto query : queries)
    {
        answers.push_back(0);

        int leftIdx = query[0], rightIdx = query[1];

        int splitIdx = lower_bound(
                           startIndices.begin() + leftIdx, startIndices.begin() + rightIdx + 1, leftIdx) -
                       startIndices.begin();

        if (splitIdx > leftIdx)
        {
            long long cutoff_count = splitIdx - leftIdx;
            answers.back() += (cutoff_count * (1 + cutoff_count)) / 2;
        }

        if (splitIdx <= rightIdx)
        {
            answers.back() += prefixSumCounts[rightIdx];
            if (splitIdx > 0)
                answers.back() -= prefixSumCounts[splitIdx - 1];
        }
    }

    return answers;
}
