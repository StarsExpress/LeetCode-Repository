#include <vector>
using namespace std;

class DirectedGraphVisitedNodes
{ // LeetCode Q.2876.
private:
    vector<int> graph; // -1 means a node has no outgoing edge.

    vector<int> visit_orders;      // -1 means a node isn't in current DFS.
    vector<int> desc_cycle_starts; // -1 means a node hasn't been searched yet.
    vector<int> distinct_visits;   // 0 means a node hasn't been searched yet.

    pair<int, int> dfs_cycles(int node, int visit_order)
    {
        // Return format: (descendant cycle start node, distinct visits).

        if (visit_orders[graph[node]] != -1)
        {
            // Goes to a node that belongs to current DFS: cycle forms.
            desc_cycle_starts[node] = graph[node];
            distinct_visits[node] += visit_order + 1 - visit_orders[graph[node]];
            return {desc_cycle_starts[node], distinct_visits[node]};
        }

        if (distinct_visits[graph[node]] != 0)
        {
            // Goes to a node that already knows its distinct visits.
            desc_cycle_starts[node] = desc_cycle_starts[graph[node]];
            distinct_visits[node] += distinct_visits[graph[node]] + 1;
            return {desc_cycle_starts[node], distinct_visits[node]};
        }

        visit_orders[node] = visit_order;
        auto [cycle_start, visits] = dfs_cycles(graph[node], visit_order + 1);
        desc_cycle_starts[node] = cycle_start;

        if (visit_orders[cycle_start] == -1)
        { // Cycle start has left current DFS.
            visits += 1;
        }
        distinct_visits[node] += visits;

        visit_orders[node] = -1; // Node is visited and leaves current DFS.
        return {desc_cycle_starts[node], distinct_visits[node]};
    }

public:
    vector<int> count_visited_nodes(vector<int> &edges)
    {
        graph.resize(edges.size());
        fill(graph.begin(), graph.end(), -1);

        for (int out_node = 0; out_node < edges.size(); out_node++)
        {
            graph[out_node] = edges[out_node]; // Directed edges.
        }

        visit_orders.resize(edges.size());
        fill(visit_orders.begin(), visit_orders.end(), -1);

        desc_cycle_starts.resize(edges.size());
        fill(desc_cycle_starts.begin(), desc_cycle_starts.end(), -1);

        distinct_visits.resize(edges.size());
        fill(distinct_visits.begin(), distinct_visits.end(), 0);

        for (int node = 0; node < edges.size(); node++)
        {
            if (distinct_visits[node] == 0)
            { // Not searched yet.
                dfs_cycles(node, 1);
            }
        }

        return distinct_visits;
    }
};