#include <vector>
using namespace std;

int sum_heroes_power(vector<int> &nums)
{ // LeetCode Q.2681.
    sort(nums.begin(), nums.end());

    long long heroes_power_sum = 0, prefix_sum = 0;
    long long modulo = pow(10, 9) + 7; // Must use long long to prevent overflow.
    for (auto num : nums)
    {
        // Power function overflows. Must use num * num and modulo as cushion.
        long long increment = (prefix_sum + num) * num % modulo;
        heroes_power_sum += increment * num;
        heroes_power_sum %= modulo;

        prefix_sum += prefix_sum + num;
        prefix_sum %= modulo;
    }

    return heroes_power_sum;
}
