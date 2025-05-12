#include <vector>
#include <unordered_set>
using namespace std;

vector<int> query_cycle_lengths(vector<vector<int>> &queries)
{ // LeetCode Q.2509.
    vector<int> answers;
    unordered_set<int> ancestors; // Track nodes' common ancestors.

    for (auto query : queries)
    {
        int node_1 = query[0], node_2 = query[1];
        int min_node = min(node_1, node_2), max_node = max(node_1, node_2);
        int min_node_level = 0, max_node_level = 0;

        ancestors.insert(min_node); // Min node might be max node's ancestor.
        while (min_node > 1)
        { // Trace min node's ancestors.
            min_node >>= 1;
            min_node_level++;
            ancestors.insert(min_node);
        }

        int first_common_ancestor = 1; // Default to the root 1.
        bool first_common_ancestor_found = false;
        int first_common_ancestor_level = 0;

        while (max_node > 1)
        { // Trace max node's ancestors.
            max_node >>= 1;
            max_node_level++;

            if (first_common_ancestor_found)
            {
                first_common_ancestor_level++;
            }
            else
            {
                // Both nodes' first common ancestor.
                if (ancestors.find(max_node) != ancestors.end())
                {
                    first_common_ancestor = max_node;
                    first_common_ancestor_found = true;
                }
                ancestors.insert(max_node);
            }
        }

        answers.push_back(min_node_level + max_node_level + 1);
        answers.back() -= 2 * first_common_ancestor_level;
        ancestors.clear(); // Reset for the next query.
    }

    return answers;
}
