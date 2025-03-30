#include <string>
#include <unordered_map>
using namespace std;

long long sum_total_appeal(string s)
{ // LeetCode 2262.
    long long total_appeal = 0, last_appeal = 0;
    unordered_map<char, int> chars2indices; // Each char's last occurred idx.

    for (int idx = 0; idx < s.length(); idx++)
    {
        if (chars2indices.find(s[idx]) != chars2indices.end())
        {
            last_appeal -= 1 + chars2indices[s[idx]];
        }
        chars2indices[s[idx]] = idx;

        last_appeal += 1 + idx;
        total_appeal += last_appeal;
    }
    return total_appeal;
}
