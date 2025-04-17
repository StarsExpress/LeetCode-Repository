#include <unordered_map>
#include <deque>
#include <vector>
using namespace std;

struct TreeNode
{
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class BinaryTreeHeight
{ // LeetCode Q.2458.
private:
    // Min tree height for each node if node and uts ancestors exist.
    unordered_map<int, int> nodes2min_heights;
    // Original tree's height, and total leaves at tree's max level.
    int full_tree_height = 0, total_max_level_leaves = 0;

    unordered_map<int, int> nodes2levels; // Each node's level.

    // Each level's top 2 min heights of nodes in this level.
    unordered_map<int, deque<int>> levels2min_heights;

    unordered_map<int, int> remaining_height; // Tree height if each node is removed.

    int dfs_tree_height(TreeNode *node, int height)
    {
        nodes2levels[node->val] = height; // Level = height.
        if (height > full_tree_height)
        {
            full_tree_height = height;  // Reset init tree height.
            total_max_level_leaves = 0; // Reset total max level leaves.

            levels2min_heights[height] = {}; // A new level.
        }

        if (height == full_tree_height)
            total_max_level_leaves += 1;

        nodes2min_heights[node->val] = height;
        if (node->left != nullptr)
        {
            int left_height = dfs_tree_height(node->left, height + 1);
            if (left_height > nodes2min_heights[node->val])
                nodes2min_heights[node->val] = left_height;
        }

        if (node->right != nullptr)
        {
            int right_height = dfs_tree_height(node->right, height + 1);
            if (right_height > nodes2min_heights[node->val])
                nodes2min_heights[node->val] = right_height;
        }

        levels2min_heights[height].push_back(nodes2min_heights[node->val]);
        sort(levels2min_heights[height].begin(), levels2min_heights[height].end());

        if (levels2min_heights[height].size() > 2)
            levels2min_heights[height].pop_front();

        return nodes2min_heights[node->val];
    }

    int dfs_max_level_leaves(TreeNode *node, int height)
    {
        remaining_height[node->val] = full_tree_height;

        // Total max level leaves of the subtree rooted at current node.
        int max_level_leaves = 0;
        if (height == full_tree_height)
            max_level_leaves += 1;

        height += 1; // Increment for next generation.
        if (node->left != nullptr)
            max_level_leaves += dfs_max_level_leaves(node->left, height);

        if (node->right != nullptr)
            max_level_leaves += dfs_max_level_leaves(node->right, height);

        if (max_level_leaves == total_max_level_leaves)
        {
            int level = nodes2levels[node->val];
            if (levels2min_heights[level].size() == 2)
            {
                int second_height = levels2min_heights[level][0];
                remaining_height[node->val] = second_height;
            }
            else
            {
                remaining_height[node->val] = level - 1;
            }
        }

        return max_level_leaves;
    }

public:
    vector<int> query_height(TreeNode *root, vector<int> &queries)
    {
        levels2min_heights[0] = {};
        dfs_tree_height(root, 0);
        dfs_max_level_leaves(root, 0);

        vector<int> answers;
        for (auto query : queries)
            answers.push_back(remaining_height[query]);
        return answers;
    }
};