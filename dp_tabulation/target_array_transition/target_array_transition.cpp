#include <vector>
using namespace std;

long long calculate_min_transition(vector<int> &nums, vector<int> &targets)
{ // LeetCode Q.3229.
    for (int idx = 0; idx < nums.size(); idx++)
    {
        nums[idx] = targets[idx] - nums[idx];
    }

    long long operations = 0;
    int positive_coverage = 0, negative_coverage = 0;

    for (auto num : nums)
    {
        if (0 <= num)
        {
            negative_coverage = 0;

            if (positive_coverage < num)
            { // Need operations for extra coverage.
                operations += num - positive_coverage;
            }
            positive_coverage = num;
        }
        else
        {
            positive_coverage = 0;

            if (num < negative_coverage)
            { // Need operations for extra coverage.
                operations += negative_coverage - num;
            }
            negative_coverage = num;
        }
    }

    return operations;
}
