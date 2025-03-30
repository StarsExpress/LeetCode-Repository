#include <vector>
#include <unordered_map>
using namespace std;

int find_max_modified_subsequence(vector<int> &nums)
{ // LeetCode Q.3041.
    sort(nums.begin(), nums.end());

    int max_len = 1; // Base case.
    // Keys: put or add. Values: {tail, len}.
    unordered_map<string, vector<int>> lengths = {
        {"put", {nums[0], 1}}, {"add", {nums[0] + 1, 1}}}; // Base case.

    nums.erase(nums.begin());
    for (auto num : nums)
    {
        int put_len = 1; // Initialize these values by 1.
        int add_len = 1;

        if (num == lengths["add"][0] + 1)
        { // Num stays put.
            put_len += lengths["add"][1];
        }
        if (num == lengths["put"][0] + 1)
        { // Num stays put.
            put_len += lengths["put"][1];
        }

        if (num == lengths["add"][0])
        { // Num increments by 1.
            add_len += lengths["add"][1];
        }
        if (num == lengths["put"][0])
        { // Num increments by 1.
            add_len += lengths["put"][1];
        }

        if (num > lengths["put"][0] + 1)
        {
            // Future nums staying put can't extend put len.
            lengths["put"] = {num, 1}; // Reset.
        }
        if (put_len > lengths["put"][1])
        { // Update put len.
            lengths["put"] = {num, put_len};
        }

        if (num + 1 > lengths["add"][0] + 1)
        {
            // Future nums adding 1 can't extend add len.
            lengths["add"] = {num + 1, 1}; // Reset.
        }
        if (add_len > lengths["add"][1])
        { // Update add len.
            lengths["add"] = {num + 1, add_len};
        }

        if (max(lengths["put"][1], lengths["add"][1]) > max_len)
        {
            max_len = max(lengths["put"][1], lengths["add"][1]);
        }
    }

    return max_len;
}
