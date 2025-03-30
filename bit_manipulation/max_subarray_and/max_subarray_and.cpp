#include <vector>
using namespace std;

int find_longest_subarray(vector<int> &nums) // LeetCode Q.2419.
{
    int longest_subarray_len = 1; // Base case.
    int max_num = *max_element(nums.begin(), nums.end());
    int max_num_streak = 0;

    for (auto num : nums)
    {
        if (num == max_num)
        { // Max AND: only need to consider max num streak.
            max_num_streak += 1;
            if (max_num_streak > longest_subarray_len)
            {
                longest_subarray_len = max_num_streak;
            }
            continue;
        }
        max_num_streak -= max_num_streak;
    }
    return longest_subarray_len;
}
