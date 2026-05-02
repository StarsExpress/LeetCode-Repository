#include <vector>
using namespace std;

class DirectedGraphVisitedNodes // LeetCode Q.2876.
{
private:
    vector<int> graph, visitedOrders, visitedCounts;
    int currentOrder = 1;

    int dfsVisitedNodes(int node)
    {
        visitedOrders[node] = currentOrder;
        currentOrder++;
        int tgtNode = graph[node];

        // A cycle just forms. Current node and its target node are members.
        if ((visitedOrders[tgtNode] != -1) && (visitedCounts[tgtNode] == 0))
        {
            int cycleSize = visitedOrders[node] + 1 - visitedOrders[tgtNode];
            visitedCounts[node] = cycleSize;
            return visitedOrders[tgtNode]; // Where cycle starts.
        }

        int cycleStartOrder = -1;
        if (visitedOrders[tgtNode] == -1)
            cycleStartOrder = dfsVisitedNodes(tgtNode);

        // Reset: current node is no part of any cycle. Nor are its ascendants.
        if (visitedOrders[node] < cycleStartOrder)
            cycleStartOrder = -1;

        visitedCounts[node] = visitedCounts[tgtNode];
        if (cycleStartOrder == -1)
            visitedCounts[node]++;

        return cycleStartOrder;
    }

public:
    vector<int> countVisitedNodes(vector<int> &edges)
    {
        graph = edges;
        visitedOrders.assign(edges.size(), -1); // -1 means unvisited yet.

        visitedCounts.assign(edges.size(), 0);

        for (int node = 0; node < graph.size(); node++)
        {
            if (visitedOrders[node] == -1)
                dfsVisitedNodes(node);
        }

        return visitedCounts;
    }
};