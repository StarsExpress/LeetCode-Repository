#include <vector>
#include <unordered_map>
using namespace std;

bool determine_winner(vector<int> &nums) // LeetCode Q.810.
{
    vector<int> distinct_nums;
    unordered_map<int, int> nums2counts;

    int xor_value = 0;
    for (auto num : nums)
    {
        xor_value ^= num;

        if (nums2counts.find(num) == nums2counts.end())
        {
            nums2counts[num] = 0;
            distinct_nums.push_back(num);
        }
        nums2counts[num] += 1;
    }

    int current_round = 1;
    int pop_idx = 0;
    while (xor_value != 0)
    {
        if (distinct_nums[pop_idx] == xor_value && distinct_nums.size() > 1)
        {
            pop_idx += 1; // Must and can switch to another removal choice.
        }

        int erased_num = distinct_nums[pop_idx];
        xor_value ^= erased_num;
        nums2counts[erased_num] -= 1;

        if (nums2counts[erased_num] == 0)
        {
            nums2counts.erase(erased_num);
            distinct_nums.erase(distinct_nums.begin() + pop_idx);
        }

        current_round += 1;
        pop_idx -= pop_idx; // Reset to the default 0.
    }

    if (current_round % 2 == 0)
    {
        return false;
    }
    return true;
}
