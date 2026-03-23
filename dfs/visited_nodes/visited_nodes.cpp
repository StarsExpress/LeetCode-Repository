#include <vector>
#include <algorithm>
using namespace std;

class DirectedGraphVisitedNodes
{ // LeetCode Q.2876.
private:
    vector<int> graph; // -1 means a node has no outgoing edge.

    vector<int> visitOrders;     // -1 means a node isn't in current DFS.
    vector<int> descCycleStarts; // -1 means a node hasn't been searched yet.
    vector<int> distinctVisits;  // 0 means a node hasn't been searched yet.

    pair<int, int> dfsCycles(int node, int visitOrder)
    {
        // Return format: (descendant cycle start node, distinct visits).

        if (visitOrders[graph[node]] != -1)
        {
            // Goes to a node that belongs to current DFS: cycle forms.
            descCycleStarts[node] = graph[node];
            distinctVisits[node] += visitOrder + 1 - visitOrders[graph[node]];

            return {descCycleStarts[node], distinctVisits[node]};
        }

        if (distinctVisits[graph[node]] != 0)
        {
            // Goes to a node that already knows its distinct visits.
            descCycleStarts[node] = descCycleStarts[graph[node]];
            distinctVisits[node] += distinctVisits[graph[node]] + 1;

            return {descCycleStarts[node], distinctVisits[node]};
        }

        visitOrders[node] = visitOrder;
        auto [cycle_start, visits] = dfsCycles(graph[node], visitOrder + 1);
        descCycleStarts[node] = cycle_start;

        if (visitOrders[cycle_start] == -1) // Cycle start has left current DFS.
            visits += 1;

        distinctVisits[node] += visits;

        visitOrders[node] = -1; // Node is visited and leaves current DFS.
        return {descCycleStarts[node], distinctVisits[node]};
    }

public:
    vector<int> countVisitedNodes(vector<int> &edges)
    {
        graph.resize(edges.size());
        fill(graph.begin(), graph.end(), -1);

        for (int outNode = 0; outNode < edges.size(); outNode++)
            graph[outNode] = edges[outNode]; // Directed edges.

        visitOrders.resize(edges.size());
        fill(visitOrders.begin(), visitOrders.end(), -1);

        descCycleStarts.resize(edges.size());
        fill(descCycleStarts.begin(), descCycleStarts.end(), -1);

        distinctVisits.resize(edges.size());
        fill(distinctVisits.begin(), distinctVisits.end(), 0);

        for (int node = 0; node < edges.size(); node++)
        {
            if (distinctVisits[node] == 0) // Not searched yet.
                dfsCycles(node, 1);
        }

        return distinctVisits;
    }
};