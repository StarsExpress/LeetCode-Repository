#include <vector>
#include <unordered_map>
using namespace std;

int sumGoodSubsequences(vector<int> &nums) // LeetCode Q.3351.
{
    int modulo = pow(10, 9) + 7;

    int64_t goodSubseqsSum = 0; // 64-bit int: avoid overflow.

    // Keys: subseqs ending at num; values: such subseqs' count and elements sum.
    unordered_map<int, vector<int64_t>> subseqsTable = {};

    for (auto num : nums)
    {
        if (subseqsTable.find(num) == subseqsTable.end())
            subseqsTable[num] = {0, 0}; // Format: {count, elements sum}.

        subseqsTable[num][0] += 1;
        subseqsTable[num][1] += num;
        goodSubseqsSum += num;

        // Current num extends subseqs at such two ends.
        for (auto subseqEnd : {num - 1, num + 1})
        {
            if (subseqsTable.find(subseqEnd) != subseqsTable.end())
            {
                subseqsTable[num][0] += subseqsTable[subseqEnd][0];

                int64_t newSum = subseqsTable[subseqEnd][1];
                newSum += num * subseqsTable[subseqEnd][0];

                subseqsTable[num][1] += newSum;
                goodSubseqsSum += newSum;
            }
        }

        subseqsTable[num][0] %= modulo; // Avoid overflow.
        subseqsTable[num][1] %= modulo;
        goodSubseqsSum %= modulo;
    }

    return goodSubseqsSum;
}