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

    TreeNode *dfs_recover_tree(int level)
    {
        int node_value;
        if (level == hyphens)
        {
            hyphens -= hyphens; // Reset.

            string node_value_str = "";
            while (!characters.empty() && characters.front() != '-')
            {
                node_value_str += characters.front();
                characters.pop();
            }
            node_value = stoi(node_value_str);
        }
        TreeNode *tree = new TreeNode(node_value);

        level += 1; // Increment level to do DFS on left and right children.
        while (!characters.empty() && characters.front() == '-')
        {
            characters.pop();
            hyphens += 1;
        }
        if (level == hyphens)
        {
            tree->left = dfs_recover_tree(level);
        }

        while (!characters.empty() && characters.front() == '-')
        {
            characters.pop();
            hyphens += 1;
        }
        if (level == hyphens)
        {
            tree->right = dfs_recover_tree(level);
        }
        return tree;
    }

public:
    TreeNode *recover(string traversal)
    {
        for (auto character : traversal)
        {
            characters.push(character);
        }
        return dfs_recover_tree(0);
    }
};