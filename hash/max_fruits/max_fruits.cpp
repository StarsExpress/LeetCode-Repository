#include <vector>
using namespace std;

int harvest_max_fruits(vector<vector<int>> &fruits, int start_position, int steps)
{ // LeetCode Q.2106.
    vector<int> positions, fruits_prefix_sums;
    for (auto fruit : fruits) // Format: {position, fruits}.
    {
        positions.push_back(fruit[0]);

        if (fruits_prefix_sums.empty())
        {
            fruits_prefix_sums.push_back(fruit[1]);
        }
        else
        {
            fruits_prefix_sums.push_back(fruits_prefix_sums.back() + fruit[1]);
        }
    }

    int max_harvested_fruits = 0;
    // Idx of the last position <= start position.
    int start_idx = upper_bound(positions.begin(), positions.end(), start_position) - positions.begin() - 1;

    for (int step_1 = 0; step_1 <= steps / 2; step_1++)
    {
        int step_2 = steps - step_1 * 2;

        vector<pair<int, int>> ends_pairs = {
            {start_position - step_1, start_position + step_2},
            {start_position - step_2, start_position + step_1}};

        for (auto ends_pair : ends_pairs)
        {
            auto [left_end, right_end] = ends_pair;
            // Idx of the last position <= left end - 1.
            int left_idx = upper_bound(positions.begin(), positions.end(), left_end - 1) - positions.begin() - 1;
            // Idx of the last position <= right end.
            int right_idx = upper_bound(positions.begin(), positions.end(), right_end) - positions.begin() - 1;

            int harvested_fruits = 0;
            if (right_idx > start_idx)
            { // Can harvest fruits at start position's right side.
                harvested_fruits += fruits_prefix_sums[right_idx];
                if (start_idx >= 0)
                {
                    harvested_fruits -= fruits_prefix_sums[start_idx];
                }
            }

            if (start_idx > left_idx)
            { // Can harvest fruits at start position's left side.
                harvested_fruits += fruits_prefix_sums[start_idx];
                if (left_idx >= 0)
                {
                    harvested_fruits -= fruits_prefix_sums[left_idx];
                }
            }

            if (harvested_fruits > max_harvested_fruits)
            {
                max_harvested_fruits = harvested_fruits;
            }
        }
    }

    return max_harvested_fruits;
}
