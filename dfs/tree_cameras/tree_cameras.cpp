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
    int totalCameras = 0;

    int dfsCameras(TreeNode *node, bool haveParent)
    {
        // Status: 0 is uncovered; 1 is covered with self camara.
        // 2 is covered with child(ren) camera(s).
        // Default child status is 2: child is covered but can't cover its parent.

        int leftChildStatus = 2;
        if (node->left != nullptr)
        {
            leftChildStatus = dfsCameras(node->left, true);
        }
        int rightChildStatus = 2;
        if (node->right != nullptr)
        {
            rightChildStatus = dfsCameras(node->right, true);
        }

        if (min(leftChildStatus, rightChildStatus) == 0)
        {
            totalCameras += 1; // Current node must cover for its child(ren).
            return 1;
        }

        if (min(leftChildStatus, rightChildStatus) == 1)
        {
            return 2; // Current node is covered by child(ren)'s camera(s).
        }

        // Current node has no coverage from its child(ren).
        if (haveParent == true)
        { // Ask parent for coverage.
            return 0;
        }
        totalCameras += 1; // No parent: must cover itself.
        return 1;
    }

public:
    int countMinCameras(TreeNode *root) // LeetCode Q.968.
    {
        totalCameras -= totalCameras; // Reset before DFS.
        dfsCameras(root, false);
        return totalCameras;
    }
};