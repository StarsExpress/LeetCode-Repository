#include <list>
#include <string>
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

        // Initialize matrix to 0 as 0 denotes an unsearched cell.
        longest_rising_lens = vector<vector<int>>(
            total_rows, vector<int>(total_cols, 0));

        for (int row_idx = 0; row_idx < total_rows; row_idx++)
        {
            for (int col_idx = 0; col_idx < total_cols; col_idx++)
            {
                if (longest_rising_lens[row_idx][col_idx] == 0)
                {
                    dfs_max_rising_path(row_idx, col_idx);
                }
            }
        }
        return max_rising_len;
    }

private:
    int max_rising_len = 1; // Base case.
    vector<vector<int>> longest_rising_lens;
    int total_rows;
    int total_cols;
    vector<vector<int>> stored_matrix;

    void dfs_max_rising_path(int row_idx, int col_idx)
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
            int next_row_idx = neighbor[0];
            int next_col_idx = neighbor[1];
            int neighbor_val = stored_matrix[next_row_idx][next_col_idx];

            if (neighbor_val > stored_matrix[row_idx][col_idx])
            {
                if (longest_rising_lens[next_row_idx][next_col_idx] == 0)
                {
                    dfs_max_rising_path(next_row_idx, next_col_idx);
                }
                int neighbor_len = longest_rising_lens[next_row_idx][next_col_idx];
                if (neighbor_len > max_neighbor_len)
                {
                    max_neighbor_len = neighbor_len;
                }
            }
        }

        longest_rising_lens[row_idx][col_idx] = 1 + max_neighbor_len;
        if (longest_rising_lens[row_idx][col_idx] > max_rising_len)
        {
            max_rising_len = longest_rising_lens[row_idx][col_idx];
        }
    }
};