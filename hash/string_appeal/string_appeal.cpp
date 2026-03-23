#include <string>
#include <unordered_map>
using namespace std;

long long sumTotalAppeal(string s)
{ // LeetCode 2262.
    long long totalAppeal = 0, lastAppeal = 0;
    unordered_map<char, int> charsIndices; // Each char's last occurred idx.

    for (int idx = 0; idx < s.length(); idx++)
    {
        if (charsIndices.find(s[idx]) != charsIndices.end())
            lastAppeal -= 1 + charsIndices[s[idx]];

        charsIndices[s[idx]] = idx;

        lastAppeal += 1 + idx;
        totalAppeal += lastAppeal;
    }
    return totalAppeal;
}
