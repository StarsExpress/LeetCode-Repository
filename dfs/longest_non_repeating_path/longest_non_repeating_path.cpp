#include <unordered_map>
#include <list>
#include <numeric>
#include <string>
using namespace std;

class LongestNonRepeatingPath
{ // LeetCode Q.2246.
private:
    string chars;
    unordered_map<int, list<int>> tree;
    int max_non_repeating_len;

    int dfs_max_non_repeating_len(int idx)
    {
        if (tree.find(idx) == tree.end())
        { // Base case: leave nodes.
            return 1;
        }

        list<int> top_2_children_lens;
        for (auto child_idx : tree[idx])
        {
            top_2_children_lens.push_back(0); // Default to 0.
            int children_len = dfs_max_non_repeating_len(child_idx);
            if (chars[child_idx] != chars[idx])
            {
                top_2_children_lens.back() += children_len;
            }

            if (top_2_children_lens.size() > 2)
            { // Always keep top 2.
                top_2_children_lens.sort();
                top_2_children_lens.pop_front();
            }
        }

        top_2_children_lens.sort();
        int straight_len = 1 + top_2_children_lens.back();
        // Curve path is centered at current node.
        int curve_len = accumulate(top_2_children_lens.begin(), top_2_children_lens.end(), 1);

        if (max(straight_len, curve_len) > max_non_repeating_len)
        {
            max_non_repeating_len = max(straight_len, curve_len);
        }
        return straight_len; // Only straight len can be reported to parent.
    }

public:
    int find_longest_non_repeating_len(vector<int> &parent, string characters)
    {
        chars = characters;
        tree.clear();
        for (int child_idx = 0; child_idx < parent.size(); child_idx++)
        {
            int parent_idx = parent[child_idx];
            if (parent_idx != -1)
            { // Non root nodes.
                if (tree.find(parent_idx) == tree.end())
                {
                    tree[parent_idx] = {};
                }
                tree[parent_idx].push_back(child_idx);
            }
        }

        max_non_repeating_len = 1;    // Base case.
        dfs_max_non_repeating_len(0); // Start from root.
        return max_non_repeating_len;
    }
};