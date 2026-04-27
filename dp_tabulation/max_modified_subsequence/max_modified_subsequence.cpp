#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

int findMaxModifiedSubsequence(vector<int> &nums)
{ // LeetCode Q.3041.
    sort(nums.begin(), nums.end());

    int maxLen = 1; // Base case.

    // Keys: put or add. Values: {tail, len}.
    unordered_map<string, vector<int>> lengths = {
        {"put", {nums[0], 1}}, {"add", {nums[0] + 1, 1}}}; // Base case.

    nums.erase(nums.begin());
    for (auto num : nums)
    {
        int putLen = 1; // Initialize these values by 1.
        int addLen = 1;

        if (num == lengths["add"][0] + 1) // Num stays put.
            putLen += lengths["add"][1];

        if (num == lengths["put"][0] + 1) // Num stays put.
            putLen += lengths["put"][1];

        if (num == lengths["add"][0]) // Num increments by 1.
            addLen += lengths["add"][1];

        if (num == lengths["put"][0]) // Num increments by 1.
            addLen += lengths["put"][1];

        if (num > lengths["put"][0] + 1) // Future nums staying put can't extend put len.
            lengths["put"] = {num, 1};   // Reset.

        if (putLen > lengths["put"][1]) // Update put len.
            lengths["put"] = {num, putLen};

        if (num + 1 > lengths["add"][0] + 1) // Future nums adding 1 can't extend add len.
            lengths["add"] = {num + 1, 1};   // Reset.

        if (addLen > lengths["add"][1]) // Update add len.
            lengths["add"] = {num + 1, addLen};

        if (max(lengths["put"][1], lengths["add"][1]) > maxLen)
            maxLen = max(lengths["put"][1], lengths["add"][1]);
    }

    return maxLen;
}
