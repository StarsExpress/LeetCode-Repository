#include <vector>
using namespace std;

class LongestCycle // LeetCode Q.2360.
{
private:
    vector<int> graph, visitedOrders;
    int currentOrder = 1, maxCycle = -1;

    bool dfsCycle(int node)
    {
        visitedOrders[node] = currentOrder;
        currentOrder++; // Increment for the next node.

        int targetNode = graph[node];
        if (targetNode == -1)
        {
            visitedOrders[node] = -2;
            return false;
        }

        if (visitedOrders[targetNode] <= -2)
        {
            visitedOrders[node] = -2;
            return false;
        }

        if (visitedOrders[targetNode] == -1)
        {
            if (dfsCycle(targetNode) == false)
            {
                visitedOrders[node] = -2;
                return false;
            }

            visitedOrders[node] = -3; // Belongs to a cycle.
            return true;
        }

        int cycleLen = visitedOrders[node] + 1 - visitedOrders[targetNode];
        if (cycleLen > maxCycle)
            maxCycle = cycleLen;

        visitedOrders[node] = -3; // Belongs to a cycle.
        return true;
    }

public:
    int computeLongestCycle(vector<int> &edges)
    {
        graph = edges;

        // Special marks: -1 = unvisited.
        // -2 = can't help find a cycle. -3 = belongs to a cycle.
        visitedOrders.assign(edges.size(), -1);

        for (int node = 0; node < edges.size(); node++)
        {
            if (visitedOrders[node] == -1) // Unvisited yet.
                dfsCycle(node);
        }

        return maxCycle;
    }
};