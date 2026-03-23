#include <list>
#include <string>
#include <vector>
using namespace std;

class MaxRisingPath
{ // LeetCode Q.329.
private:
    int maxRisingLen = 1; // Base case.
    vector<vector<int>> longestRisingLens;

    int totalRows;
    int totalCols;
    vector<vector<int>> storedMatrix;

    void dfsMaxRisingPath(int rowIdx, int colIdx)
    {
        list<vector<int>> neighbors;

        if (colIdx < totalCols - 1)
        { // Can go East.
            neighbors.push_back({rowIdx, colIdx + 1});
        }

        if (0 < colIdx)
        { // Can go West.
            neighbors.push_back({rowIdx, colIdx - 1});
        }

        if (rowIdx < totalRows - 1)
        { // Can go South.
            neighbors.push_back({rowIdx + 1, colIdx});
        }

        if (0 < rowIdx)
        { // Can go North.
            neighbors.push_back({rowIdx - 1, colIdx});
        }

        int maxNeighborLen = 0;
        for (auto neighbor : neighbors)
        {
            int nextRowIdx = neighbor[0];
            int nextColIdx = neighbor[1];
            int neighborVal = storedMatrix[nextRowIdx][nextColIdx];

            if (neighborVal > storedMatrix[rowIdx][colIdx])
            {
                if (longestRisingLens[nextRowIdx][nextColIdx] == 0)
                {
                    dfsMaxRisingPath(nextRowIdx, nextColIdx);
                }

                int neighborLen = longestRisingLens[nextRowIdx][nextColIdx];

                if (neighborLen > maxNeighborLen)
                {
                    maxNeighborLen = neighborLen;
                }
            }
        }

        longestRisingLens[rowIdx][colIdx] = 1 + maxNeighborLen;
        if (longestRisingLens[rowIdx][colIdx] > maxRisingLen)
        {
            maxRisingLen = longestRisingLens[rowIdx][colIdx];
        }
    }

public:
    int findLongestRisingPath(vector<vector<int>> &matrix)
    {
        storedMatrix = matrix;
        totalRows = matrix.size();
        totalCols = matrix[0].size();

        // Initialize matrix to 0, denoting all unsearched cells.
        longestRisingLens = vector<vector<int>>(
            totalRows, vector<int>(totalCols, 0));

        for (int rowIdx = 0; rowIdx < totalRows; rowIdx++)
        {
            for (int colIdx = 0; colIdx < totalCols; colIdx++)
            {
                if (longestRisingLens[rowIdx][colIdx] == 0)
                {
                    dfsMaxRisingPath(rowIdx, colIdx);
                }
            }
        }
        return maxRisingLen;
    }
};