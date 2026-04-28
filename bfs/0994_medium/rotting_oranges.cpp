#include <vector>
#include <unordered_set>
#include <string>
using namespace std;

int rot_oranges(vector<vector<int>> &grid) // LeetCode Q.994.
{
    int spent_mins = 0;

    vector<pair<int, int>> current_rot, next_rot; // Format: {row idx, col idx}.
    unordered_set<string> fresh_fruits;           // Format: str(row idx) + "-" + str(col idx).

    for (int row_idx = 0; row_idx < grid.size(); row_idx++)
    {
        for (int col_idx = 0; col_idx < grid[0].size(); col_idx++)
        {
            if (grid[row_idx][col_idx] == 2)
            {
                current_rot.push_back({row_idx, col_idx});
            }
            else if (grid[row_idx][col_idx] == 1)
            {
                fresh_fruits.insert(to_string(row_idx) + "-" + to_string(col_idx));
            }
        }
    }

    while (!current_rot.empty())
    {
        auto [row_idx, col_idx] = current_rot.back();
        current_rot.pop_back();

        vector<pair<int, int>> neighbors = {
            {row_idx - 1, col_idx}, {row_idx, col_idx + 1}, {row_idx + 1, col_idx}, {row_idx, col_idx - 1}};

        for (auto [neighbor_row_idx, neighbor_col_idx] : neighbors)
        {
            if (0 <= neighbor_row_idx && neighbor_row_idx < grid.size())
            {
                if (0 <= neighbor_col_idx && neighbor_col_idx < grid[0].size())
                {
                    if (grid[neighbor_row_idx][neighbor_col_idx] == 1)
                    {
                        fresh_fruits.erase(
                            to_string(neighbor_row_idx) + "-" + to_string(neighbor_col_idx));
                        grid[neighbor_row_idx][neighbor_col_idx]++;
                        next_rot.push_back({neighbor_row_idx, neighbor_col_idx});
                    }
                }
            }
        }

        if (current_rot.empty() && !next_rot.empty())
        {
            spent_mins++;
            current_rot = next_rot;
            next_rot.clear();
        }
    }

    if (!fresh_fruits.empty())
        return -1;
    return spent_mins;
}
