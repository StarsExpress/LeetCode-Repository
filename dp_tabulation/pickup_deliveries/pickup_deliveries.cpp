#include <cmath>
using namespace std;

int count_valid_options(int total_orders) // LeetCode Q.1359.
{
    long long valid_pickups = 1, sequence_len = 2; // Base case at n = 1: (P1, D1).

    long long modulo = pow(10, 9) + 7;
    for (int order = 2; order <= total_orders; order++)
    {
        long long combos = (1 + sequence_len + 1) * (sequence_len + 1) / 2;
        combos %= modulo;
        valid_pickups *= combos;
        valid_pickups %= modulo;
        sequence_len += 2; // Update sequence len for next order amount.
    }

    return valid_pickups;
}
