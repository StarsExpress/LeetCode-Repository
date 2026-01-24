#include <vector>
using namespace std;

vector<long long> count_stable_subarrays(vector<int> &nums, vector<vector<int>> &queries)
{ // LeetCode Q.3748.
    vector<long long> prefix_sum_counts;
    vector<int> start_indices;

    int streak_start_idx = 0;

    for (int idx = 0; idx < nums.size(); idx++)
    {
        int num = nums[idx];

        if (idx > 0 && num < nums[idx - 1])
            streak_start_idx = idx;
        start_indices.push_back(streak_start_idx);

        if (prefix_sum_counts.empty())
            prefix_sum_counts.push_back(0);
        else
            prefix_sum_counts.push_back(prefix_sum_counts.back());

        prefix_sum_counts.back() += idx + 1 - streak_start_idx;
    }

    vector<long long> answers;
    for (auto query : queries)
    {
        answers.push_back(0);

        int left_idx = query[0], right_idx = query[1];

        int split_idx = lower_bound(
                            start_indices.begin() + left_idx, start_indices.begin() + right_idx + 1, left_idx) -
                        start_indices.begin();

        if (split_idx > left_idx)
        {
            long long cutoff_count = split_idx - left_idx;
            answers.back() += (cutoff_count * (1 + cutoff_count)) / 2;
        }

        if (split_idx <= right_idx)
        {
            answers.back() += prefix_sum_counts[right_idx];
            if (split_idx > 0)
                answers.back() -= prefix_sum_counts[split_idx - 1];
        }
    }

    return answers;
}
