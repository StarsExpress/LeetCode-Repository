#include <numeric>
#include <vector>
using namespace std;

int maximize_scores_difference(vector<int> &stones) // LeetCode Q.1872.
{
    auto stones_sum = reduce(stones.begin(), stones.end());
    int max_diff = stones_sum;

    // For stones count >= 3, DP starts from the 3rd rightmost stone.
    int idx = stones.size() - 3;
    while (idx > -1)
    {
        // Current round's stones sum = stones[0] + ... + stones[idx + 1].
        stones_sum -= stones[idx + 2];
        if (stones_sum - max_diff > max_diff)
        {
            max_diff = stones_sum - max_diff;
        }
        idx--;
    }
    return max_diff;
}
