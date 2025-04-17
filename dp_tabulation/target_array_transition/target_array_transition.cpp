#include <vector>
using namespace std;

long long calculate_min_transition(vector<int> &nums, vector<int> &targets)
{ // LeetCode Q.3229.
    long long operations = 0;
    int positive_coverage = 0, negative_coverage = 0;

    for (int idx = 0; idx < targets.size(); idx++)
    {
        targets[idx] -= nums[idx];
        if (0 <= targets[idx])
        { // Need increments to reach target.
            negative_coverage = 0;

            // Operations for extra coverage.
            operations += max(targets[idx] - positive_coverage, 0);
            positive_coverage = targets[idx];
        }
        else
        { // Need decrements to reach target.
            positive_coverage = 0;

            // Operations for extra coverage.
            operations += max(negative_coverage - targets[idx], 0);
            negative_coverage = targets[idx];
        }
    }

    return operations;
}
