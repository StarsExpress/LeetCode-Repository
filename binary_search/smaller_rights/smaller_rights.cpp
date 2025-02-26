#include <vector>
using namespace std;

vector<int> countSmaller(vector<int> &nums)
{ // LeetCode Q.315.
    vector<int> smaller_rights;
    vector<int> sorted_nums;
    for (int idx = nums.size() - 1; idx >= 0; idx--)
    {
        int left_idx = 0;
        int right_idx = sorted_nums.size() - 1;
        while (left_idx <= right_idx)
        {
            int mid_idx = (left_idx + right_idx) / 2;
            if (sorted_nums[mid_idx] < nums[idx])
            {
                left_idx = mid_idx + 1;
            }
            else
            {
                right_idx = mid_idx - 1;
            }
        }
        sorted_nums.insert(sorted_nums.begin() + left_idx, nums[idx]);
        smaller_rights.push_back(left_idx);
    }
    reverse(smaller_rights.begin(), smaller_rights.end());
    return smaller_rights;
}
