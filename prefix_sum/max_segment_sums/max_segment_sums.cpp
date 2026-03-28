#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<long long> collectMaxSegmentSums(vector<int> &nums, vector<int> &queries)
{ // LeetCode Q.2382.

    vector<long long> prefixSums; // Store sums in long long.
    for (auto num : nums)
    {
        if (prefixSums.empty())
            prefixSums.push_back(num);

        else
            prefixSums.push_back(prefixSums.back() + num);
    }

    // Max heap. Format: {segment sum, segment start idx, segment end idx}.
    priority_queue<vector<long long>, vector<vector<long long>>> sumsHeap;

    int totalNums = nums.size();
    sumsHeap.push({prefixSums.back(), 0, totalNums - 1});

    vector<long long> maxSegmentSums;
    vector<int> sortedQueries;

    for (auto query : queries)
    {
        if (maxSegmentSums.size() == queries.size() - 1)
        {
            maxSegmentSums.push_back(0); // Last query's answer is always 0.
            break;
        }

        int queryIdx = upper_bound(sortedQueries.begin(), sortedQueries.end(), query) - sortedQueries.begin();
        sortedQueries.insert(sortedQueries.begin() + queryIdx, query);

        while (!sumsHeap.empty())
        {
            long long segmentSum = sumsHeap.top()[0]; // Store sums in long long.
            int start = sumsHeap.top()[1];
            int end = sumsHeap.top()[2];

            // Idx of the 1st query >= start.
            int startIdx = upper_bound(sortedQueries.begin(), sortedQueries.end(), start - 1) - sortedQueries.begin();

            // Idx of the 1st query >= end.
            int endIdx = upper_bound(sortedQueries.begin(), sortedQueries.end(), end - 1) - sortedQueries.begin();

            if (startIdx == endIdx)
            {
                if (endIdx == sortedQueries.size())
                { // Edge case.
                    maxSegmentSums.push_back(segmentSum);
                    break;
                }

                if (sortedQueries[endIdx] != end)
                {
                    maxSegmentSums.push_back(segmentSum);
                    break;
                }
            }

            sumsHeap.pop(); // Max segment sum is split by a removed idx.
            int removedIdx = sortedQueries[startIdx];

            int newEnd = removedIdx - 1;
            if (start <= newEnd)
            {
                segmentSum = prefixSums[newEnd];
                if (start > 0)
                    segmentSum -= prefixSums[start - 1];

                sumsHeap.push({segmentSum, start, newEnd});
            }

            int newStart = removedIdx + 1;
            if (newStart <= end)
            {
                segmentSum = prefixSums[end];
                if (newStart > 0)
                    segmentSum -= prefixSums[newStart - 1];

                sumsHeap.push({segmentSum, newStart, end});
            }
        }
    }

    return maxSegmentSums;
}
