#include <vector>
#include <list>
#include <map>
#include <unordered_map>
#include <queue>
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

vector<vector<int>> verticalTraversal(TreeNode *root) // LeetCode Q.987.
{
    map<int, vector<int>> cols2nums;

    queue<pair<TreeNode *, int>> queue; // Format: {node, col}.
    queue.push({root, 0});

    unordered_map<int, vector<int>> current_row_values; // Keys: cols.
    list<pair<TreeNode *, int>> next_row_nodes;         // Format: {node, col}.

    while (!queue.empty())
    {
        TreeNode *node = queue.front().first;
        int col = queue.front().second;

        queue.pop();
        if (node->left != nullptr)
        {
            next_row_nodes.push_back({node->left, col - 1});
        }
        if (node->right != nullptr)
        {
            next_row_nodes.push_back({node->right, col + 1});
        }

        if (cols2nums.find(col) == cols2nums.end())
        {
            cols2nums[col] = {};
        }
        if (current_row_values.find(col) == current_row_values.end())
        {
            current_row_values[col] = {};
        }
        current_row_values[col].push_back(node->val);
        sort(current_row_values[col].begin(), current_row_values[col].end());

        if (queue.empty())
        {
            while (!next_row_nodes.empty())
            {
                pair<TreeNode *, int> next_row_node = next_row_nodes.front();
                queue.push(next_row_node);
                next_row_nodes.pop_front();
            }
            for (const auto &pair : current_row_values)
            {
                for (auto value : pair.second)
                {
                    cols2nums[pair.first].push_back(value);
                }
            }
            current_row_values.clear(); // Clear for the next row.
        }
    }

    vector<vector<int>> vectical_traversal;
    for (const auto &pair : cols2nums)
    {
        vectical_traversal.push_back(pair.second);
    }
    return vectical_traversal;
}
