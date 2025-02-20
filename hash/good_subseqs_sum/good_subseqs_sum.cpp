#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

int sum_good_subsequences(vector<int> &nums) // LeetCode Q.3351.
{
    int modulo = pow(10, 9) + 7;
    int64_t good_subseqs_sum = 0; // 64-bit int: avoid overflow.
    // Keys: subseqs ending at num; values: such subseqs' count and elements sum.
    unordered_map<int, vector<int64_t>> subseqs_table = {};

    for (auto num : nums)
    {
        if (subseqs_table.find(num) == subseqs_table.end())
        {
            subseqs_table[num] = {0, 0}; // Format: {count, elements sum}.
        }
        subseqs_table[num][0] += 1;
        subseqs_table[num][1] += num;
        good_subseqs_sum += num;

        // Current num extends subseqs at such two ends.
        for (auto subseq_end : {num - 1, num + 1})
        {
            if (subseqs_table.find(subseq_end) != subseqs_table.end())
            {
                subseqs_table[num][0] += subseqs_table[subseq_end][0];

                int64_t new_sum = subseqs_table[subseq_end][1];
                new_sum += num * subseqs_table[subseq_end][0];

                subseqs_table[num][1] += new_sum;
                good_subseqs_sum += new_sum;
            }
        }

        subseqs_table[num][0] %= modulo; // Avoid overflow.
        subseqs_table[num][1] %= modulo; // Avoid overflow.
        good_subseqs_sum %= modulo;      // Avoid overflow.
    }
    return good_subseqs_sum;
}