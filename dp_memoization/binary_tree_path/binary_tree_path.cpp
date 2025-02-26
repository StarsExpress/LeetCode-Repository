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

class BinaryTreeMaxPathSum // LeetCode Q.124.
{
private:
    int global_max_path_sum = -1000; // Min node value stated by question.

    int dfs_path_sum(TreeNode *node)
    {
        int left_child_path_sum = 0;
        int right_child_path_sum = 0;

        if (node->left != nullptr)
        {
            left_child_path_sum += max(dfs_path_sum(node->left), 0);
        }
        if (node->right != nullptr)
        {
            right_child_path_sum += max(dfs_path_sum(node->right), 0);
        }

        int left_end_path_sum = left_child_path_sum + node->val;
        int middle_path_sum = left_end_path_sum + right_child_path_sum;
        int right_end_path_sum = node->val + right_child_path_sum;

        int max_path_sum = max(
            max(left_end_path_sum, middle_path_sum), right_end_path_sum);

        if (max_path_sum > global_max_path_sum)
        {
            global_max_path_sum = max_path_sum;
        }

        return max(max(left_end_path_sum, right_end_path_sum), 0);
    }

public:
    int find_max_path_sum(TreeNode *root)
    {
        dfs_path_sum(root);
        return global_max_path_sum;
    }
};