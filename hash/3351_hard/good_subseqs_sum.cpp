#include <vector>
#include <unordered_map>
using namespace std;

int sumGoodSubsequences(vector<int> &nums) // LeetCode Q.3351.
{
    long long modulo = pow(10, 9) + 7; // Long long prevents overflow.

    unordered_map<int, long long> subseqCounts;
    unordered_map<int, long long> subseqSums;

    for (long long num : nums)
    {
        for (auto validTail : {num - 1, num + 1})
        {
            subseqCounts[num] += subseqCounts[validTail];

            subseqSums[num] += num * subseqCounts[validTail];

            subseqSums[num] += subseqSums[validTail];
        }

        // Counts & sums are O(2^n) so must do modulo for future operations.
        subseqCounts[num] += 1;
        subseqCounts[num] %= modulo;
        subseqSums[num] += num;
        subseqSums[num] %= modulo;
    }

    long long goodSubseqSum = 0;
    for (auto &pair : subseqSums)
        goodSubseqSum += pair.second;

    return goodSubseqSum % modulo; // Control long long size.
}