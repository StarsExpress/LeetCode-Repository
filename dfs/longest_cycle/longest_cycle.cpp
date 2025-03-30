#include <vector>
using namespace std;

class LongestCycle
{ // LeetCode Q.2360.
private:
    vector<int> graph;
    vector<int> visit_orders;
    vector<int> status; // 1: not searched yet; 2: now under DFS; 3: finished DFS.

    int dfs_cycle_len(int node, int visit_order)
    {
        visit_orders[node] = visit_order, status[node] = 2;

        int cycle_len = -1; // Default to no cycle.
        if (graph[node] != -1)
        { // Current node has an outgoing node.
            if (status[graph[node]] == 1)
            {
                cycle_len = dfs_cycle_len(graph[node], visit_order + 1);
            }

            if (status[graph[node]] == 2)
            { // Cycle forms.
                cycle_len = visit_order + 1 - visit_orders[graph[node]];
            }
        }

        status[node] = 3; // Current node finishes DFS.
        return cycle_len;
    }

public:
    int compute_longest_cycle_len(vector<int> &edges)
    {
        graph = edges;
        visit_orders.resize(edges.size(), -1); // Default order = -1 (not searched).
        status.resize(edges.size(), 1);        // All nodes aren't searched at the beginning.

        int max_cycle_len = -1;
        for (int out_node = 0; out_node < edges.size(); out_node++)
        {
            int in_node = edges[out_node];
            if (in_node != -1)
            { // Each node has at most 1 outgoing edge.
                int cycle_len = dfs_cycle_len(out_node, 1);
                if (cycle_len > max_cycle_len)
                {
                    max_cycle_len = cycle_len;
                }
            }
        }

        return max_cycle_len;
    }
};