#include <queue>
#include <string>
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

class TreeRecovery
{ // LeetCode Q.1028.
private:
    queue<char> characters;
    int hyphens = 0;

    TreeNode *dfsRecoverTree(int level)
    {
        int nodeValue = 0;
        if (level == hyphens)
        {
            hyphens -= hyphens; // Reset.

            string nodeValueStr = "";
            while (!characters.empty() && characters.front() != '-')
            {
                nodeValueStr += characters.front();
                characters.pop();
            }
            nodeValue = stoi(nodeValueStr);
        }

        TreeNode *tree = new TreeNode(nodeValue);

        level += 1; // Increment level to do DFS on left and right children.
        while (!characters.empty() && characters.front() == '-')
        {
            characters.pop();
            hyphens += 1;
        }

        if (level == hyphens)
            tree->left = dfsRecoverTree(level);

        while (!characters.empty() && characters.front() == '-')
        {
            characters.pop();
            hyphens += 1;
        }

        if (level == hyphens)
            tree->right = dfsRecoverTree(level);

        return tree;
    }

public:
    TreeNode *recover(string traversal)
    {
        for (auto character : traversal)
            characters.push(character);

        return dfsRecoverTree(0);
    }
};