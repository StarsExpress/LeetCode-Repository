#include <string>
using namespace std;

string findLargestSubstring(string s) // LeetCode Q.1163.
{
    int startIdx = 0; // Start idx of the substring with max lexi order.

    // Current idx's char compares to (start idx + relative order) idx's char.
    int relativeOrder = 0;

    for (int idx = 1; idx < s.length(); idx++)
    {
        if (s[idx] == s[startIdx + relativeOrder])
        {
            relativeOrder++; // Tie: increment order to keep comparison.
            continue;
        }

        if (s[idx] > s[startIdx]) // Directly beats char at start idx.
            startIdx = idx;

        else if (s[idx] > s[startIdx + relativeOrder])
        {
            startIdx = idx - 1;
            while (s[startIdx - 1] >= s[startIdx])
                startIdx--; // Extend w.r.t. monotonicity.
        }

        relativeOrder = 0; // Reset.
    }

    return s.substr(startIdx);
}
