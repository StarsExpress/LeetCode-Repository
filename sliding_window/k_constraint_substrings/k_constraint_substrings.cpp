#include <vector>
#include <string>
using namespace std;

vector<long long> count_substrings(string bin_string, int k, vector<vector<int>> &queries)
{ // LeetCode Q.3261.
    // Min left idx for substrings w/ right idx at ith idx.
    vector<int> left_boundaries;

    int zeros_counts = 0, ones_counts = 0;
    vector<long long> prefix_substrings_counts;

    int left_idx = 0;
    for (int right_idx = 0; right_idx < bin_string.length(); right_idx++)
    {
        if (bin_string[right_idx] == '1')
        {
            ones_counts++;
        }
        else
        {
            zeros_counts++;
        }

        while (min(zeros_counts, ones_counts) > k)
        {
            if (bin_string[left_idx] == '1')
            {
                ones_counts--;
            }
            else
            {
                zeros_counts--;
            }

            left_idx++;
        }

        left_boundaries.push_back(left_idx);

        if (prefix_substrings_counts.empty())
        {
            prefix_substrings_counts.push_back(0);
        }
        else
        {
            prefix_substrings_counts.push_back(prefix_substrings_counts.back());
        }
        prefix_substrings_counts.back() += right_idx + 1 - left_idx;
    }

    // Max right idx for subarrays w/ left idx <= ith idx.
    vector<int> right_boundaries;

    left_idx = 0;
    for (int right_idx = 0; right_idx < bin_string.length(); right_idx++)
    {
        while (left_idx < bin_string.length() && left_boundaries[left_idx] <= right_idx)
        {
            left_idx++;
        }
        right_boundaries.push_back(left_idx - 1);
    }

    vector<long long> answers;
    for (auto query : queries)
    {
        int start_idx = query[0], end_idx = query[1];

        answers.push_back(prefix_substrings_counts[end_idx]);
        if (start_idx > 0)
        { // Query's start idx > 0: need adjustments.
            int last_affected_idx = min(right_boundaries[start_idx], end_idx);
            answers.back() -= prefix_substrings_counts[last_affected_idx];

            long long total_affected_indices = (last_affected_idx + 1 - start_idx);
            answers.back() += (1 + total_affected_indices) * total_affected_indices / 2;
        }
    }

    return answers;
}
