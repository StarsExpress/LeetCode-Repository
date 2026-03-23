#include <vector>
#include <algorithm>
using namespace std;

int harvestMaxFruits(vector<vector<int>> &fruits, int startPosition, int steps)
{ // LeetCode Q.2106.
    vector<int> positions, fruitsPrefixSums;
    for (auto fruit : fruits) // Format: {position, fruits}.
    {
        positions.push_back(fruit[0]);

        if (fruitsPrefixSums.empty())
            fruitsPrefixSums.push_back(fruit[1]);

        else
            fruitsPrefixSums.push_back(fruitsPrefixSums.back() + fruit[1]);
    }

    int maxHarvestedFruits = 0;

    // Idx of the last position <= start position.
    int startIdx = upper_bound(positions.begin(), positions.end(), startPosition) - positions.begin() - 1;

    for (int step_1 = 0; step_1 <= steps / 2; step_1++)
    {
        int step_2 = steps - step_1 * 2;

        vector<pair<int, int>> ends_pairs = {
            {startPosition - step_1, startPosition + step_2},
            {startPosition - step_2, startPosition + step_1}};

        for (auto ends_pair : ends_pairs)
        {
            auto [left_end, right_end] = ends_pair;

            // Idx of the last position <= left end - 1.
            int leftIdx = upper_bound(positions.begin(), positions.end(), left_end - 1) - positions.begin() - 1;

            // Idx of the last position <= right end.
            int rightIdx = upper_bound(positions.begin(), positions.end(), right_end) - positions.begin() - 1;

            int harvestedFruits = 0;

            if (rightIdx > startIdx)
            { // Can harvest fruits at start position's right side.
                harvestedFruits += fruitsPrefixSums[rightIdx];
                if (startIdx >= 0)
                    harvestedFruits -= fruitsPrefixSums[startIdx];
            }

            if (startIdx > leftIdx)
            { // Can harvest fruits at start position's left side.
                harvestedFruits += fruitsPrefixSums[startIdx];
                if (leftIdx >= 0)
                    harvestedFruits -= fruitsPrefixSums[leftIdx];
            }

            if (harvestedFruits > maxHarvestedFruits)
                maxHarvestedFruits = harvestedFruits;
        }
    }

    return maxHarvestedFruits;
}
