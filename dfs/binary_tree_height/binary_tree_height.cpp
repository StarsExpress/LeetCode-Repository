#include <unordered_map>
#include <deque>
#include <vector>
#include <algorithm>
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
    // Min tree height for each node if node and its ancestors exist.
    unordered_map<int, int> nodes2MinHeights;

    // Original tree's height, and total leaves at tree's max level.
    int fullTreeHeight = 0, totalMaxLevelLeaves = 0;

    unordered_map<int, int> nodes2Levels; // Each node's level.

    // Each level's top 2 min heights of nodes in this level.
    unordered_map<int, deque<int>> levels2MinHeights;

    unordered_map<int, int> remainingHeight; // Tree height if each node is removed.

    int dfsTreeHeight(TreeNode *node, int height)
    {
        nodes2Levels[node->val] = height; // Level = height.
        if (height > fullTreeHeight)
        {
            fullTreeHeight = height; // Reset init tree height.
            totalMaxLevelLeaves = 0; // Reset total max level leaves.

            levels2MinHeights[height] = {}; // A new level.
        }

        if (height == fullTreeHeight)
            totalMaxLevelLeaves += 1;

        nodes2MinHeights[node->val] = height;
        if (node->left != nullptr)
        {
            int left_height = dfsTreeHeight(node->left, height + 1);
            if (left_height > nodes2MinHeights[node->val])
                nodes2MinHeights[node->val] = left_height;
        }

        if (node->right != nullptr)
        {
            int right_height = dfsTreeHeight(node->right, height + 1);
            if (right_height > nodes2MinHeights[node->val])
                nodes2MinHeights[node->val] = right_height;
        }

        levels2MinHeights[height].push_back(nodes2MinHeights[node->val]);
        sort(levels2MinHeights[height].begin(), levels2MinHeights[height].end());

        if (levels2MinHeights[height].size() > 2)
            levels2MinHeights[height].pop_front();

        return nodes2MinHeights[node->val];
    }

    int dfsMaxLevelLeaves(TreeNode *node, int height)
    {
        remainingHeight[node->val] = fullTreeHeight;

        // Total max level leaves of the subtree rooted at current node.
        int maxLevelLeaves = 0;
        if (height == fullTreeHeight)
            maxLevelLeaves += 1;

        height += 1; // Increment for next generation.
        if (node->left != nullptr)
            maxLevelLeaves += dfsMaxLevelLeaves(node->left, height);

        if (node->right != nullptr)
            maxLevelLeaves += dfsMaxLevelLeaves(node->right, height);

        if (maxLevelLeaves == totalMaxLevelLeaves)
        {
            int level = nodes2Levels[node->val];
            if (levels2MinHeights[level].size() == 2)
            {
                int second_height = levels2MinHeights[level][0];
                remainingHeight[node->val] = second_height;
            }
            else
            {
                remainingHeight[node->val] = level - 1;
            }
        }

        return maxLevelLeaves;
    }

public:
    vector<int> queryHeight(TreeNode *root, vector<int> &queries)
    {
        levels2MinHeights[0] = {};
        dfsTreeHeight(root, 0);
        dfsMaxLevelLeaves(root, 0);

        vector<int> answers;
        for (auto query : queries)
            answers.push_back(remainingHeight[query]);
        return answers;
    }
};