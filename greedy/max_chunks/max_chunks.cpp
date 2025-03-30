#include <vector>
using namespace std;

int find_max_sortable_chunks(vector<int> &nums)
{ // LeetCode Q.768 & 769.
    vector<int> prefix_maxs;
    for (auto num : nums)
    {
        if (prefix_maxs.empty())
        {
            prefix_maxs.push_back(num);
            continue;
        }
        prefix_maxs.push_back(max(prefix_maxs.back(), num));
    }

    int max_chunks = 1, suffix_min = nums.back(); // Base case.
    for (int idx = nums.size() - 1; idx >= 1; idx--)
    {
        if (nums[idx] < suffix_min)
        {
            suffix_min = nums[idx];
        }
        if (suffix_min >= prefix_maxs[idx - 1])
        {
            max_chunks += 1;
        }
    }

    return max_chunks;
}
