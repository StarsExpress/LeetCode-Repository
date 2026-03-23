#include <vector>
using namespace std;

int findMaxSortableChunks(vector<int> &nums)
{ // LeetCode Q.768 & 769.
    vector<int> prefixMaxs;
    for (auto num : nums)
    {
        if (prefixMaxs.empty())
        {
            prefixMaxs.push_back(num);
            continue;
        }
        prefixMaxs.push_back(max(prefixMaxs.back(), num));
    }

    int maxChunks = 1, suffixMin = nums.back(); // Base case.
    for (int idx = nums.size() - 1; idx >= 1; idx--)
    {
        if (nums[idx] < suffixMin)
        {
            suffixMin = nums[idx];
        }
        if (suffixMin >= prefixMaxs[idx - 1])
        {
            maxChunks += 1;
        }
    }

    return maxChunks;
}
