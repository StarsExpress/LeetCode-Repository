#include <vector>
#include <ranges>
using namespace std;

long long calculateMinTransition(vector<int> &nums, vector<int> &targets)
{ // LeetCode Q.3229.
    long long operations = 0;
    int positive_coverage = 0, negative_coverage = 0;

    for (auto [target, num] : views::zip(targets, nums))
    {
        target -= num;

        if (0 <= target)
        { // Need increments to reach target.
            negative_coverage = 0;

            // Operations for extra coverage.
            operations += max(target - positive_coverage, 0);
            positive_coverage = target;
        }
        else
        { // Need decrements to reach target.
            positive_coverage = 0;

            // Operations for extra coverage.
            operations += max(negative_coverage - target, 0);
            negative_coverage = target;
        }
    }

    return operations;
}
