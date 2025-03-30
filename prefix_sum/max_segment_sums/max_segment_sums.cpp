#include <vector>
#include <queue>
using namespace std;

vector<long long> collect_max_segment_sums(vector<int> &nums, vector<int> &queries)
{ // LeetCode Q.2382.

    vector<long long> prefix_sums; // Store sums in long long.
    for (auto num : nums)
    {
        if (prefix_sums.empty())
        {
            prefix_sums.push_back(num);
        }
        else
        {
            prefix_sums.push_back(prefix_sums.back() + num);
        }
    }

    // Max heap. Format: {segment sum, segment start idx, segment end idx}.
    priority_queue<vector<long long>, vector<vector<long long>>> sums_heap;
    int total_nums = nums.size();
    sums_heap.push({prefix_sums.back(), 0, total_nums - 1});

    vector<long long> max_segment_sums;
    vector<int> sorted_queries;

    for (auto query : queries)
    {
        if (max_segment_sums.size() == queries.size() - 1)
        {
            max_segment_sums.push_back(0); // Last query's answer is always 0.
            break;
        }

        int query_idx = upper_bound(sorted_queries.begin(), sorted_queries.end(), query) - sorted_queries.begin();
        sorted_queries.insert(sorted_queries.begin() + query_idx, query);

        while (!sums_heap.empty())
        {
            long long segment_sum = sums_heap.top()[0]; // Store sums in long long.
            int start = sums_heap.top()[1];
            int end = sums_heap.top()[2];

            // Idx of the 1st query >= start.
            int start_idx = upper_bound(sorted_queries.begin(), sorted_queries.end(), start - 1) - sorted_queries.begin();

            // Idx of the 1st query >= end.
            int end_idx = upper_bound(sorted_queries.begin(), sorted_queries.end(), end - 1) - sorted_queries.begin();

            if (start_idx == end_idx)
            {
                if (end_idx == sorted_queries.size())
                { // Edge case.
                    max_segment_sums.push_back(segment_sum);
                    break;
                }
                if (sorted_queries[end_idx] != end)
                {
                    max_segment_sums.push_back(segment_sum);
                    break;
                }
            }

            sums_heap.pop(); // Max segment sum is split by a removed idx.
            int removed_idx = sorted_queries[start_idx];

            int new_end = removed_idx - 1;
            if (start <= new_end)
            {
                segment_sum = prefix_sums[new_end];
                if (start > 0)
                {
                    segment_sum -= prefix_sums[start - 1];
                }
                sums_heap.push({segment_sum, start, new_end});
            }

            int new_start = removed_idx + 1;
            if (new_start <= end)
            {
                segment_sum = prefix_sums[end];
                if (new_start > 0)
                {
                    segment_sum -= prefix_sums[new_start - 1];
                }
                sums_heap.push({segment_sum, new_start, end});
            }
        }
    }

    return max_segment_sums;
}
