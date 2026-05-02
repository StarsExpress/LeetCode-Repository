#include <string>
#include <unordered_map>
using namespace std;

string findMinWindowSubstring(string sourceString, string targetString) // LeetCode Q.76.
{
    unordered_map<char, int> tgtCharsCounts;

    for (auto character : targetString)
        tgtCharsCounts[character]++;

    int uniqueTgtCharsCount = tgtCharsCounts.size();

    // Must not exceed unique target chars count during sliding window.
    int coverage = 0;

    int minWindowLeftIdx = -1;
    int minLen = sourceString.size() + 1; // Source length + 1: symbol of not found yet.

    int leftIdx = 0;
    for (int rightIdx = 0; rightIdx < sourceString.size(); rightIdx++)
    {
        char character = sourceString[rightIdx];
        if (tgtCharsCounts.find(character) != tgtCharsCounts.end())
        {
            tgtCharsCounts[character]--;

            if (tgtCharsCounts[character] == 0) // Becomes covered.
                coverage++;
        }

        while (coverage == uniqueTgtCharsCount) // Can try to shrink window.
        {
            int windowLen = rightIdx + 1 - leftIdx;

            if (windowLen < minLen)
                minLen = windowLen, minWindowLeftIdx = leftIdx;

            char removedChar = sourceString[leftIdx];
            if (tgtCharsCounts.find(removedChar) != tgtCharsCounts.end())
            {
                tgtCharsCounts[removedChar]++;

                if (tgtCharsCounts[removedChar] > 0) // Becomes uncovered.
                    coverage--;
            }

            leftIdx += 1;
        }
    }

    if (minLen == sourceString.size() + 1)
        return "";

    return sourceString.substr(minWindowLeftIdx, minLen);
}
