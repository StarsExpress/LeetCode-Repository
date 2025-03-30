#include <vector>
using namespace std;

int calculate_min_formation(vector<int> &target)
{ // LeetCode Q.1526.
    int coverage = 0, operations = 0;
    for (auto num : target)
    {
        if (coverage < num)
        { // Need operations for additional coverage.
            operations += num - coverage;
        }
        coverage = num;
    }

    return operations;
}
