#include <vector>
#include <unordered_map>
using namespace std;

int count_special_subsequences(vector<int> &nums)
{ // LeetCode Q.1955.
    long long modulo = pow(10, 9) + 7;
    unordered_map<int, long long> subarrays_ends_counts;

    for (auto num : nums)
    {
        subarrays_ends_counts[num] *= 2;
        subarrays_ends_counts[num] += subarrays_ends_counts[num - 1];
        subarrays_ends_counts[num] %= modulo;

        if (num == 0)
            subarrays_ends_counts[num]++;
    }

    return subarrays_ends_counts[2];
}
