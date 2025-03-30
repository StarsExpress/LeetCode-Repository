#include <vector>
using namespace std;

vector<int> countSmaller(vector<int> &nums)
{ // LeetCode Q.315.
    vector<int> smaller_rights, sorted_nums;
    for (int idx = nums.size() - 1; idx >= 0; idx--)
    {
        // Idx of the 1st right sorted num > current num - 1.
        int insertion_idx = upper_bound(sorted_nums.begin(), sorted_nums.end(), nums[idx] - 1) - sorted_nums.begin();

        sorted_nums.insert(sorted_nums.begin() + insertion_idx, nums[idx]);
        smaller_rights.push_back(insertion_idx);
    }
    reverse(smaller_rights.begin(), smaller_rights.end());
    return smaller_rights;
}
