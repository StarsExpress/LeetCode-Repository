#include <unordered_map>
#include <vector>
#include <string>
using namespace std;

vector<int> partitionLabels(string s) // LeetCode Q.763.
{
    unordered_map<char, int> charsOrders;
    vector<pair<int, int>> indicesPairs; // Same char's 1st and last indices pair.

    for (int idx = 0; idx < s.size(); idx++)
    {
        char character = s[idx];
        if (charsOrders.find(character) == charsOrders.end())
        {
            charsOrders[character] = charsOrders.size() + 1;
            indicesPairs.push_back({idx, idx});
        }

        int order = charsOrders[character];
        indicesPairs[order - 1].second = idx;
    }

    vector<int> partitionSizes;

    int currentSize = 0;
    int currentRightIdx = -1;

    for (auto [firstIdx, lastIdx] : indicesPairs)
    {
        if (currentRightIdx < firstIdx) // Start a new partition.
        {
            if (currentSize > 0) // Store the latest partition.
                partitionSizes.push_back(currentSize);

            currentSize = lastIdx + 1 - firstIdx;
            currentRightIdx = lastIdx;
            continue;
        }

        if (lastIdx > currentRightIdx) // Current partition extends.
        {
            currentSize += lastIdx - currentRightIdx;
            currentRightIdx = lastIdx;
        }
    }

    if (currentSize > 0) // Last remaining partition.
        partitionSizes.push_back(currentSize);

    return partitionSizes;
}
