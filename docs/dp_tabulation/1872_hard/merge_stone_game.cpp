#include <vector>
#include <numeric>
using namespace std;

int maximizeScoresDifference(vector<int> &stones) // LeetCode Q.1872.
{
    int prefixSum = 0;
    for (auto stone : stones)
        prefixSum += stone;

    // Base case: Alice merges everything as the only attempt.
    int maxScoreDiff = prefixSum;

    prefixSum -= stones.back();

    for (int idx = stones.size() - 2; idx >= 1; idx--)
    {
        if (prefixSum - maxScoreDiff > maxScoreDiff)
            maxScoreDiff = prefixSum - maxScoreDiff;

        prefixSum -= stones[idx];
    }

    return maxScoreDiff;
}
