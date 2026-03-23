#include <random>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class UnBlockedPick
{ // LeetCode Q.710.
private:
    int totalCandidates;
    unordered_map<int, int> numsReplacements;

public:
    UnBlockedPick(int n, vector<int> &blocklist)
    {
        unordered_set<int> blockedNums(blocklist.begin(), blocklist.end());

        totalCandidates = n - blocklist.size();
        int replacement = totalCandidates;
        for (auto blockedNum : blocklist)
        {
            if (blockedNum < totalCandidates)
            { // Need replacements for blocked nums in [0, total candidates - 1].
                while (blockedNums.find(replacement) != blockedNums.end())
                    replacement++;

                numsReplacements[blockedNum] = replacement;
                replacement++;
            }
        }
    }

    int pick()
    {
        static random_device rd;
        static mt19937 gen(rd());

        uniform_int_distribution<> distribution(0, totalCandidates - 1);
        int pickedNum = distribution(gen);

        if (numsReplacements.find(pickedNum) != numsReplacements.end())
            pickedNum = numsReplacements[pickedNum];
        return pickedNum;
    }
};