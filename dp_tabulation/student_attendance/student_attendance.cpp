#include <vector>
using namespace std;

int count_possibilities(int record_len) // LeetCode Q.552.
{
    long long modulo = pow(10, 9) + 7; // Use long long to prevent overflow.

    record_len -= 1; // Base case: record length of 1 where A, L and P are all possible.

    // Count on each idx = possibilities with idx count of late suffixes.
    vector<long long> no_absence = {1, 1, 0};
    vector<long long> one_absence = {1, 0, 0};

    vector<long long> no_absence_changes = {}; // Count changes: x to x + 1 length.
    vector<long long> one_absence_changes = {};

    while (record_len > 0)
    {
        // AL0 count change at current length.
        one_absence_changes.push_back(
            no_absence[0] + no_absence[1] + no_absence[2]);
        one_absence_changes[0] += one_absence[1] + one_absence[2];

        // AL1 count change at current length.
        one_absence_changes.push_back(one_absence[0] - one_absence[1]);

        // AL2 count change at current length.
        one_absence_changes.push_back(one_absence[1] - one_absence[2]);

        // L0 count change at current length.
        no_absence_changes.push_back(no_absence[1] + no_absence[2]);

        // L1 count change at current length.
        no_absence_changes.push_back(no_absence[0] - no_absence[1]);

        // L2 count change at current length.
        no_absence_changes.push_back(no_absence[1] - no_absence[2]);

        for (int idx = 0; idx < 3; idx++)
        { // Required to control size.
            no_absence[idx] += no_absence_changes[idx] % modulo;
            no_absence[idx] %= modulo;
            one_absence[idx] += one_absence_changes[idx] % modulo;
            one_absence[idx] %= modulo;
        }

        record_len -= 1; // Reset for the next length.
        no_absence_changes.clear();
        one_absence_changes.clear();
    }

    long long possibilities = no_absence[0] + no_absence[1] + no_absence[2];
    possibilities += one_absence[0] + one_absence[1] + one_absence[2];
    return possibilities % modulo; // Required to control size.
}
