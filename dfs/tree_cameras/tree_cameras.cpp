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

class TreeCameras
{
private:
    int total_cameras = 0;

    int dfs_cameras(TreeNode *node, bool have_parent)
    {
        // Status: 0 is uncovered; 1 is covered with self camara.
        // 2 is covered with child(ren) camera(s).
        // Default child status is 2: child is covered but can't cover its parent.

        int left_child_status = 2;
        if (node->left != nullptr)
        {
            left_child_status = dfs_cameras(node->left, true);
        }
        int right_child_status = 2;
        if (node->right != nullptr)
        {
            right_child_status = dfs_cameras(node->right, true);
        }

        if (min(left_child_status, right_child_status) == 0)
        {
            total_cameras += 1; // Current node must cover for its child(ren).
            return 1;
        }

        if (min(left_child_status, right_child_status) == 1)
        {
            return 2; // Current node is covered by child(ren)'s camera(s).
        }

        // Current node has no coverage from its child(ren).
        if (have_parent == true)
        { // Ask parent for coverage.
            return 0;
        }
        total_cameras += 1; // No parent: must cover itself.
        return 1;
    }

public:
    int count_min_cameras(TreeNode *root) // LeetCode Q.968.
    {
        total_cameras -= total_cameras; // Reset before DFS.
        dfs_cameras(root, false);
        return total_cameras;
    }
};