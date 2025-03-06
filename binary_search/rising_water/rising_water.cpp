#include <unordered_set>
#include <vector>
#include <list>
#include <string>
using namespace std;

class RisingWater
{ // LeetCode Q.778.
private:
    vector<vector<int>> water;
    int total_rows;
    int total_cols;

    unordered_set<string> visited_cells;

    void dfs_path(int row_idx, int col_idx, int elevation)
    {
        visited_cells.insert(to_string(row_idx) + ":" + to_string(col_idx));

        list<vector<int>> neighbors = {
            {row_idx, col_idx + 1},
            {row_idx, col_idx - 1},
            {row_idx + 1, col_idx},
            {row_idx - 1, col_idx}};

        for (auto neighbor : neighbors)
        {
            if (neighbor[0] < 0 || total_rows <= neighbor[0])
            {
                continue;
            }
            if (neighbor[1] < 0 || total_cols <= neighbor[1])
            {
                continue;
            }

            if (water[neighbor[0]][neighbor[1]] <= elevation)
            {
                string neighbor_id = to_string(neighbor[0]) + ":" + to_string(neighbor[1]);
                if (visited_cells.find(neighbor_id) == visited_cells.end())
                {
                    dfs_path(neighbor[0], neighbor[1], elevation);
                }
            }
        }
    }

public:
    int swim(vector<vector<int>> &grid)
    {
        water = grid;
        total_rows = grid.size();
        total_cols = grid[0].size();
        string bottom_right_cell_id = to_string(total_rows - 1) + ":" + to_string(total_cols - 1);

        int min_elevation = grid[0][0]; // Base case: elevation of top left cell.
        int max_elevation = -numeric_limits<int>::max();
        for (int row_idx = 0; row_idx < total_rows; row_idx++)
        {
            for (int col_idx = 0; col_idx < total_cols; col_idx++)
            {
                if (water[row_idx][col_idx] > max_elevation)
                {
                    max_elevation = water[row_idx][col_idx];
                }
            }
        }

        while (min_elevation <= max_elevation)
        {
            int mid_elevation = (min_elevation + max_elevation) / 2;

            visited_cells.clear(); // Reset before DFS.
            dfs_path(0, 0, mid_elevation);
            if (visited_cells.find(bottom_right_cell_id) != visited_cells.end())
            {
                max_elevation = mid_elevation - 1;
                continue;
            }
            min_elevation = mid_elevation + 1;
        }

        return min_elevation;
    }
};