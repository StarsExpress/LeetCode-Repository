#include <string>
using namespace std;

string find_largest_substring(string s) // LeetCode Q.1163.
{
    int start_idx = 0; // Start idx of the substring with max lexi order.
    // Current idx's char compares to (start idx + relative order) idx's char.
    int relative_order = 0;

    for (int idx = 1; idx < s.length(); idx++)
    {
        if (s[idx] == s[start_idx + relative_order])
        {
            relative_order++; // Tie: increment order to keep comparison.
            continue;
        }

        if (s[idx] > s[start_idx])
        { // Directly beats char at start idx.
            start_idx = idx;
        }
        else if (s[idx] > s[start_idx + relative_order])
        {
            start_idx = idx - 1;
            while (s[start_idx - 1] >= s[start_idx])
            {
                start_idx--; // Extend w.r.t. monotonicity.
            }
        }

        relative_order = 0; // Reset.
    }

    return s.substr(start_idx);
}
