#include <random>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class UnBlockedPick
{ // LeetCode Q.710.
private:
    int total_candidates;
    unordered_map<int, int> nums2replacements;

public:
    UnBlockedPick(int n, vector<int> &blacklist)
    {
        unordered_set<int> blocked_nums(blacklist.begin(), blacklist.end());

        total_candidates = n - blacklist.size();
        int replacement = total_candidates;
        for (auto blocked_num : blacklist)
        {
            if (blocked_num < total_candidates)
            { // Need replacements for blocked nums in [0, total candidates - 1].
                while (blocked_nums.find(replacement) != blocked_nums.end())
                    replacement++;

                nums2replacements[blocked_num] = replacement;
                replacement++;
            }
        }
    }

    int pick()
    {
        static random_device rd;
        static mt19937 gen(rd());
        uniform_int_distribution<> distribution(0, total_candidates - 1);
        int picked_num = distribution(gen);

        if (nums2replacements.find(picked_num) != nums2replacements.end())
            picked_num = nums2replacements[picked_num];
        return picked_num;
    }
};