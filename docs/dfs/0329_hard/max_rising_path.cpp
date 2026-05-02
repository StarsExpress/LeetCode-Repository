#include <algorithm>
#include <vector>
using namespace std;

class MaxRisingPath // LeetCode Q.329.
{
private:
    // An entry's max rising path value is -1 if this entry is unsearched.
    // Otherwise, max rising path value is the finalized value w.r.t. entry.
    vector<vector<int>> entries, maxRisingPath;

    int maxRisingLen = 1; // Base case.

    void dfsRisingPath(int rowIdx, int colIdx)
    {
        maxRisingPath[rowIdx][colIdx] = 1; // Base case: a path of only current entry.

        vector<pair<int, int>> neighbors = {
            {rowIdx + 1, colIdx}, // South.
            {rowIdx - 1, colIdx}, // North.
            {rowIdx, colIdx + 1}, // East.
            {rowIdx, colIdx - 1}  // West.
        };

        for (auto [neighborRowIdx, neighborColIdx] : neighbors)
        {
            // Inbound checks on row & col indices.
            if (0 > neighborRowIdx || neighborRowIdx >= entries.size())
                continue;

            if (0 > neighborColIdx || neighborColIdx >= entries[0].size())
                continue;

            // Skip neighbors that aren't bigger than current entry.
            if (entries[rowIdx][colIdx] >= entries[neighborRowIdx][neighborColIdx])
                continue;

            if (maxRisingPath[neighborRowIdx][neighborColIdx] == -1) // Unsearched neighbor.
                dfsRisingPath(neighborRowIdx, neighborColIdx);

            int risingLen = 1 + maxRisingPath[neighborRowIdx][neighborColIdx];

            if (risingLen > maxRisingPath[rowIdx][colIdx])
                maxRisingPath[rowIdx][colIdx] = risingLen;

            if (risingLen > maxRisingLen)
                maxRisingLen = risingLen;
        }
    }

public:
    int findLongestRisingPath(vector<vector<int>> &matrix)
    {
        entries = matrix;

        maxRisingPath.assign(matrix.begin(), matrix.end()); // Base case.
        for (auto &row : maxRisingPath)
            fill(row.begin(), row.end(), -1);

        for (int rowIdx = 0; rowIdx < matrix.size(); rowIdx++)
        {
            for (int colIdx = 0; colIdx < matrix[0].size(); colIdx++)
            {
                if (maxRisingPath[rowIdx][colIdx] == -1)
                    dfsRisingPath(rowIdx, colIdx);
            }
        }

        return maxRisingLen;
    }
};