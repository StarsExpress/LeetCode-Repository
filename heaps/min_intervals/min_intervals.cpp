#include <vector>
#include <queue>
using namespace std;

vector<int> find_min_intervals(vector<vector<int>> &intervals, vector<int> &queries)
{ // LeetCode Q.1851.
    // Min heap. Format: {interval start, size}.
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> starts_sizes_heap;

    // Min heap. Format: {size, interval end}.
    priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> sizes_ends_heap;

    for (auto interval : intervals)
        starts_sizes_heap.push({interval[0], interval[1] + 1 - interval[0]});

    vector<pair<int, int>> queries_indices; // Format: {query num, query idx}.
    for (int query_idx = 0; query_idx < queries.size(); query_idx++)
        queries_indices.push_back({queries[query_idx], query_idx});

    sort( // Sort by ascending query nums.
        queries_indices.begin(), queries_indices.end(),
        [](const pair<int, int> &a, const pair<int, int> &b)
        { return a.first < b.first; });

    vector<int> answers(queries.size(), -1); // Default to -1.
    for (auto [query_num, query_idx] : queries_indices)
    {
        while (!starts_sizes_heap.empty() && starts_sizes_heap.top()[0] <= query_num)
        {
            int start = starts_sizes_heap.top()[0], size = starts_sizes_heap.top()[1];
            sizes_ends_heap.push({size, start + size - 1}); // Format: {size, interval end}.
            starts_sizes_heap.pop();
        }

        while (!sizes_ends_heap.empty() && sizes_ends_heap.top()[1] < query_num)
        {
            sizes_ends_heap.pop();
        }

        if (!sizes_ends_heap.empty())
            answers[query_idx] = sizes_ends_heap.top()[0];
    }

    return answers;
}
