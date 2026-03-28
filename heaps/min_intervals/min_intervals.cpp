#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

vector<int> findMinIntervals(vector<vector<int>> &intervals, vector<int> &queries)
{ // LeetCode Q.1851.
    // Min heap. Format: {interval start, size}.
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> startsSizesHeap;

    // Min heap. Format: {size, interval end}.
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> sizesEndsHeap;

    for (auto interval : intervals)
        startsSizesHeap.push({interval[0], interval[1] + 1 - interval[0]});

    vector<pair<int, int>> queriesIndices; // Format: {query num, query idx}.

    for (int queryIdx = 0; queryIdx < queries.size(); queryIdx++)
        queriesIndices.push_back({queries[queryIdx], queryIdx});

    sort( // Sort by ascending query nums.
        queriesIndices.begin(), queriesIndices.end(),
        [](const pair<int, int> &a, const pair<int, int> &b)
        { return a.first < b.first; });

    vector<int> answers(queries.size(), -1); // Default to -1.

    for (auto [queryNum, queryIdx] : queriesIndices)
    {
        while (!startsSizesHeap.empty() && startsSizesHeap.top()[0] <= queryNum)
        {
            int start = startsSizesHeap.top()[0], size = startsSizesHeap.top()[1];
            sizesEndsHeap.push({size, start + size - 1}); // Format: {size, interval end}.
            startsSizesHeap.pop();
        }

        while (!sizesEndsHeap.empty() && sizesEndsHeap.top()[1] < queryNum)
            sizesEndsHeap.pop();

        if (!sizesEndsHeap.empty())
            answers[queryIdx] = sizesEndsHeap.top()[0];
    }

    return answers;
}
