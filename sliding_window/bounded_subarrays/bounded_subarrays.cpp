#include <vector>
using namespace std;

long long count_bounded_subarrays(vector<int> &nums, int minimum, int maximum)
{ // LeetCode Q.2444.
    long long bounded_subarrays = 0;
    int left_bound = 0;                       // Min start idx of fixed subarrays ending at current idx.
    int min_prev_idx = -1, max_prev_idx = -1; // Latest indices of min k and max k.

    for (int idx = 0; idx < nums.size(); idx++)
    {
        if (nums[idx] < minimum || maximum < nums[idx])
        {                                         // Current num is out of bounds.
            min_prev_idx = -1, max_prev_idx = -1; // Reset indices.
            left_bound = idx + 1;                 // Reset left bound.
            continue;
        }

        if (nums[idx] == minimum)
            min_prev_idx = idx;
        if (nums[idx] == maximum)
            max_prev_idx = idx;

        // Current num is the end of bounded subarrays.
        if (min(min_prev_idx, max_prev_idx) != -1)
            // Max start idx = the smaller of min prev idx and max prev idx.
            bounded_subarrays += min(min_prev_idx, max_prev_idx) + 1 - left_bound;
    }

    return bounded_subarrays;
}
