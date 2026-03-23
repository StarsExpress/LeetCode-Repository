#include <vector>
using namespace std;

long long countMinOperations(vector<int> &nums)
{ // LeetCode Q.2366.
    long long minOperations = 0;

    int idx = nums.size() - 2;
    while (idx >= 0)
    {
        if (nums[idx] > nums[idx + 1])
        { // Maximize the division by minimizing pieces to break into.
            int pieces = nums[idx] / nums[idx + 1];

            if (nums[idx] % nums[idx + 1] > 0) // Have to add another piece.
                pieces += 1;

            nums[idx] /= pieces;
            minOperations += pieces - 1; // Conduct (pieces - 1) operations.
        }

        idx--;
    }
    return minOperations;
}
