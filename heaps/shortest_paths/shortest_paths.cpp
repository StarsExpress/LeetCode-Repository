#include <vector>
#include <queue>
using namespace std;

class ShortestPathsCalculator
{ // LeetCode Q.2642.
private:
    vector<vector<int>> shortestPaths;
    int totalNodes;
    int infinity = numeric_limits<int>::max();

public:
    ShortestPathsCalculator(int n, vector<vector<int>> &edges)
    {
        shortestPaths.assign(n, vector<int>(n, infinity));
        for (auto edge : edges)
        { // Edge format: {out node, in node, cost}.
            shortestPaths[edge[0]][edge[1]] = edge[2];
        }
        for (int node = 0; node < n; node++)
        {
            shortestPaths[node][node] = 0; // Each node's cost to itself is 0.
        }
        totalNodes = n;
    }

    void add_edge(vector<int> edge)
    { // Edge format: {out node, in node, cost}.
        shortestPaths[edge[0]][edge[1]] = edge[2];
    }

    int calculate_shortest_path(int start, int end)
    {
        // Min heap. Format: {cost, node}.
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> costHeap;

        for (int node = 0; node < totalNodes; node++)
        {
            if (start != node && shortestPaths[start][node] != infinity)
                costHeap.push({shortestPaths[start][node], node});
        }

        while (!costHeap.empty() && costHeap.top().first != infinity)
        {
            auto [minCost, minCostNode] = costHeap.top();
            costHeap.pop();

            for (int neighbor = 0; neighbor < totalNodes; neighbor++)
            {
                int cost = shortestPaths[minCostNode][neighbor];
                if (cost != infinity)
                {
                    if (minCost + cost < shortestPaths[start][neighbor])
                    {
                        shortestPaths[start][neighbor] = minCost + cost;
                        costHeap.push({shortestPaths[start][neighbor], neighbor});
                    }
                }
            }
        }

        if (shortestPaths[start][end] == infinity)
            return -1;
        return shortestPaths[start][end];
    }
};