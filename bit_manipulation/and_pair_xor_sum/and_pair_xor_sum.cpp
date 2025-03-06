#include <vector>
using namespace std;

int count_and_pair_xor_sum(vector<int> &nums_1, vector<int> &nums_2)
{ // LeetCode Q.1835.
    // Key: (a & b) ^ (a & c) = a & (b ^ c).
    int xor_value_1 = 0;
    for (auto num : nums_1)
    {
        xor_value_1 ^= num;
    }
    int xor_value_2 = 0;
    for (auto num : nums_2)
    {
        xor_value_2 ^= num;
    }
    return xor_value_1 & xor_value_2;
}
