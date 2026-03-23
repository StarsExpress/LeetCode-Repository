#include <vector>
using namespace std;

class LongestCycle
{ // LeetCode Q.2360.
private:
    vector<int> graph;
    vector<int> visitOrders;
    vector<int> status; // 1: not searched yet; 2: now under DFS; 3: finished DFS.

    int dfsCycleLen(int node, int visitOrder)
    {
        visitOrders[node] = visitOrder, status[node] = 2;

        int cycleLen = -1; // Default to no cycle.
        if (graph[node] != -1)

        { // Current node has an outgoing node.
            if (status[graph[node]] == 1)
            {
                cycleLen = dfsCycleLen(graph[node], visitOrder + 1);
            }

            if (status[graph[node]] == 2)
            { // Cycle forms.
                cycleLen = visitOrder + 1 - visitOrders[graph[node]];
            }
        }

        status[node] = 3; // Current node finishes DFS.
        return cycleLen;
    }

public:
    int computeLongestCycleLen(vector<int> &edges)
    {
        graph = edges;
        visitOrders.resize(edges.size(), -1); // Default order = -1 (not searched).
        status.resize(edges.size(), 1);       // All nodes aren't searched at the beginning.

        int maxCycleLen = -1;
        for (int outNode = 0; outNode < edges.size(); outNode++)
        {
            int inNode = edges[outNode];
            if (inNode != -1)

            { // Each node has at most 1 outgoing edge.
                int cycleLen = dfsCycleLen(outNode, 1);
                if (cycleLen > maxCycleLen)
                {
                    maxCycleLen = cycleLen;
                }
            }
        }

        return maxCycleLen;
    }
};