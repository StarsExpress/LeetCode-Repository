#include <list>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class MaxRisingPath
{ // LeetCode Q.329.
public:
    int find_longest_rising_path(vector<vector<int>> &matrix)
    {
        stored_matrix = matrix;
        total_rows = matrix.size();
        total_cols = matrix[0].size();

        for (int row_idx = 0; row_idx < total_rows; row_idx++)
        {
            for (int col_idx = 0; col_idx < total_cols; col_idx++)
            {
                dfs_max_rising_path(row_idx, col_idx);
            }
        }
        return max_rising_len;
    }

private:
    int max_rising_len = 1; // Base case.
    unordered_map<string, int> max_rising_lens;
    int total_rows;
    int total_cols;
    vector<vector<int>> stored_matrix;

    int dfs_max_rising_path(int row_idx, int col_idx)
    {
        string hash_id = to_string(row_idx) + "-" + to_string(col_idx);

        if (max_rising_lens.find(hash_id) == max_rising_lens.end())
        {
            list<vector<int>> neighbors;
            if (col_idx < total_cols - 1)
            { // Can go East.
                neighbors.push_back({row_idx, col_idx + 1});
            }

            if (0 < col_idx)
            { // Can go West.
                neighbors.push_back({row_idx, col_idx - 1});
            }

            if (row_idx < total_rows - 1)
            { // Can go South.
                neighbors.push_back({row_idx + 1, col_idx});
            }

            if (0 < row_idx)
            { // Can go North.
                neighbors.push_back({row_idx - 1, col_idx});
            }

            int max_neighbor_len = 0;
            for (auto neighbor : neighbors)
            {
                int neighbor_val = stored_matrix[neighbor[0]][neighbor[1]];
                if (neighbor_val > stored_matrix[row_idx][col_idx])
                {
                    int neighbor_len = dfs_max_rising_path(
                        neighbor[0], neighbor[1]);
                    if (neighbor_len > max_neighbor_len)
                    {
                        max_neighbor_len = neighbor_len;
                    }
                }
            }

            max_rising_lens[hash_id] = 1 + max_neighbor_len;
            if (max_rising_lens[hash_id] > max_rising_len)
            {
                max_rising_len = max_rising_lens[hash_id];
            }
        }

        return max_rising_lens[hash_id];
    }
};