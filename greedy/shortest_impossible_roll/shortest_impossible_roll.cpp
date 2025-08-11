#include <vector>
#include <unordered_map>
using namespace std;

int find_shortest_impossible_sequence(vector<int> &rolls, int dice_values)
{ // LeetCode Q.2350.
    int shortest_impossible_len = 1;
    unordered_map<int, bool> nums2occurrences;
    for (auto num : rolls)
    {
        nums2occurrences[num] = true;
        if (nums2occurrences.size() == dice_values)
        {                              // Current seq len is possible.
            nums2occurrences.clear();  // Reset.
            shortest_impossible_len++; // Go to next seq len.
        }
    }
    return shortest_impossible_len;
}
