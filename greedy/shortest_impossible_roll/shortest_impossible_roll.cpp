#include <vector>
#include <unordered_map>
using namespace std;

int findShortestImpossibleSequence(vector<int> &rolls, int diceValues)
{ // LeetCode Q.2350.
    int shortestImpossibleLen = 1;
    unordered_map<int, bool> nums2Counts;

    for (auto num : rolls)
    {
        nums2Counts[num] = true;
        if (nums2Counts.size() == diceValues) // Current seq len is possible.
        {
            nums2Counts.clear();     // Reset.
            shortestImpossibleLen++; // Go to next seq len.
        }
    }

    return shortestImpossibleLen;
}
