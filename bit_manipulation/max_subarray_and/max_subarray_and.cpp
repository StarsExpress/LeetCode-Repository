#include <vector>
using namespace std;

int find_longest_subarray(vector<int> &nums) // LeetCode Q.2419.
{
    int longest_len = 1; // Base case.
    int max_num = 0, max_streak = 0;

    for (auto num : nums)
    { // Max AND: only need to consider max num streak.
        if (num != max_num)
        {
            max_streak -= max_streak; // Reset.

            if (num > max_num)
                max_num = num, longest_len = 1; // Reset.
        }

        if (num == max_num)
        {
            max_streak++;
            if (max_streak > longest_len)
                longest_len = max_streak;
        }
    }

    return longest_len;
}
