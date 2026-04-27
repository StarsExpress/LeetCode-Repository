#include <vector>
#include <deque>
#include <ranges>
#include <algorithm>
using namespace std;

vector<int> query_max_sum(vector<int> &nums_1, vector<int> &nums_2, vector<vector<int>> &queries)
{                                        // LeetCode Q.2736.
    vector<vector<int>> queries_indices; // Format: {x, y, idx}.
    for (int idx = 0; idx < queries.size(); idx++)
        queries_indices.push_back({queries[idx][0], queries[idx][1], idx});

    sort(
        queries_indices.begin(), queries_indices.end(),
        [](const vector<int> &a, const vector<int> &b)
        { return a[0] > b[0]; }); // Sort by descending x.

    vector<pair<int, int>> nums; // Format: {num 1, num 2}.
    for (auto const &[x, y] : views::zip(nums_1, nums_2))
        nums.push_back({x, y});

    sort(nums.begin(), nums.end()); // Sort by ascending x and ascending y.

    deque<vector<int>> stack; // Ascending y and descending x + y. Format: {y, x + y}.

    vector<int> answers(queries.size(), -1); // Default to -1.

    for (auto query_idx : queries_indices)
    {
        int query_x = query_idx[0];

        while (!nums.empty() && nums.back().first >= query_x)
        {
            int y = nums.back().second, pair_sum = y + nums.back().first;
            nums.pop_back();

            // Current y and pair sum overpower stack top.
            while (!stack.empty() && stack.back()[1] <= pair_sum)
                stack.pop_back();

            // Stack top overpowers current y and pair sum.
            if (!stack.empty() && stack.back()[0] >= y)
                continue;
            stack.push_back({y, pair_sum});
        }

        int query_y = query_idx[1], idx = query_idx[2];

        auto iterator = lower_bound(
            stack.begin(), stack.end(), query_y,
            [](const vector<int> &element, int value)
            { return element[0] < value; });
        if (iterator < stack.end())
            answers[idx] = (*iterator)[1];
    }

    return answers;
}
