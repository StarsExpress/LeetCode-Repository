#include <iostream>
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

class BinaryTreeHouseRobber // LeetCode Q.337.
{
private:
    pair<int, int> dfs_rob(TreeNode *node)
    { // Pair format: {robbed money w.r.t. node, robbed money w.r.t. children}.
        int children_money = 0;
        int node_money = node->val;

        if (node->left != nullptr)
        {
            pair<int, int> robbed_money_pair = dfs_rob(node->left);
            node_money += robbed_money_pair.second;
            children_money += robbed_money_pair.first;
        }
        if (node->right != nullptr)
        {
            pair<int, int> robbed_money_pair = dfs_rob(node->right);
            node_money += robbed_money_pair.second;
            children_money += robbed_money_pair.first;
        }

        return {max(node_money, children_money), children_money};
    }

public:
    int rob(TreeNode *root)
    {
        return dfs_rob(root).first;
    }
};