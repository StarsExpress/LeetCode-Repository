#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class CoinsCollector
{ // LeetCode Q.2603.
private:
    vector<unordered_set<int>> graph;

    vector<bool> leaves, leavesParents; // If a node is a coin leave or parent of coin leave.
    vector<bool> requiredVisits;        // If a node must be visited to collect all coins.
    vector<bool> visited;               // For DFS visited marks.

    void dfsRequiredVisitNodes(int node)
    {
        visited[node] = true;
        for (auto neighbor : graph[node])
        {
            if (leavesParents[neighbor] == true && visited[neighbor] == false)
            {
                requiredVisits[node] = true;
                dfsRequiredVisitNodes(neighbor);
            }
        }
    }

    int mustVisitEdges = 0;

    bool dfsMustVisitEdges(int parent, int node)
    {
        visited[node] = true;
        for (auto neighbor : graph[node])
        {
            if (visited[neighbor] == false)
            {
                if (dfsMustVisitEdges(node, neighbor))
                {
                    requiredVisits[node] = true;
                }
            }
        }

        if (requiredVisits[node] && parent != -1)
        {
            mustVisitEdges++;
        }
        return requiredVisits[node];
    }

    unordered_set<int> emptyParents;
    int maxEmptyParentsDist = 1;

    int dfsMaxEmptyParentsDist(int node)
    {
        visited[node] = true;
        vector<int> childrenDists;

        for (auto neighbor : graph[node])
        {
            if (emptyParents.find(neighbor) != emptyParents.end())
            {
                if (visited[neighbor] == false)
                {
                    childrenDists.push_back(dfsMaxEmptyParentsDist(neighbor));
                }
            }
        }

        int localMaxDist = 1;
        if (childrenDists.empty())
        {
            return localMaxDist;
        }

        sort(childrenDists.begin(), childrenDists.end());
        localMaxDist = childrenDists.back();

        if (childrenDists.size() >= 2)
        {
            localMaxDist += childrenDists[childrenDists.size() - 2];
        }
        if (localMaxDist > maxEmptyParentsDist)
        {
            maxEmptyParentsDist = localMaxDist;
        }

        return childrenDists.back() + 1;
    }

public:
    int collectCoins(vector<int> &coins, vector<vector<int>> &edges)
    {
        graph.resize(coins.size());
        for (auto edge : edges)
        { // Undirected edges.
            graph[edge[0]].insert(edge[1]);
            graph[edge[1]].insert(edge[0]);
        }

        // Graph reduction: keep removing leaves w/o coins.
        for (int node = 0; node < coins.size(); node++)
        {
            while (coins[node] == 0 && graph[node].size() == 1)
            {
                int neighbor = *graph[node].begin();
                graph[neighbor].erase(node);
                graph[node].clear();
                node = neighbor;
            }
        }

        leaves.resize(coins.size(), false);
        leavesParents.resize(coins.size(), false);

        for (int node = 0; node < coins.size(); node++)
        {
            if (coins[node] == 1 && graph[node].size() == 1)
            {
                leaves[node] = true;

                int neighbor = *graph[node].begin();
                if (coins[neighbor] == 0 || graph[neighbor].size() > 1)
                {
                    leavesParents[neighbor] = true;
                }
            }
        }

        bool parentsAllEmpty = true;
        requiredVisits.resize(coins.size(), false);

        for (int node = 0; node < coins.size(); node++)
        {
            if (leavesParents[node])
            {
                bool isEmptyParent = true;

                for (auto neighbor : graph[node])
                {
                    if (leavesParents[neighbor] == false && leaves[neighbor] == false)
                    {
                        requiredVisits[neighbor] = true;
                        isEmptyParent = false, parentsAllEmpty = false;
                    }
                }

                if (isEmptyParent)
                {
                    emptyParents.insert(node);
                }
            }
        }

        if (parentsAllEmpty)
        {
            if (emptyParents.empty())
            {
                return 0;
            }
            visited.resize(coins.size(), false);
            dfsMaxEmptyParentsDist(*emptyParents.begin());
            return max(0, (maxEmptyParentsDist - 2) * 2);
        }

        visited.clear(); // Must clear before resize to reset all values to false.
        visited.resize(coins.size(), false);

        int mustVisitNode = -1;

        for (int node = 0; node < coins.size(); node++)
        {
            if (requiredVisits[node] && visited[node] == false)
            {
                mustVisitNode = node;
                dfsRequiredVisitNodes(node);
            }
        }

        if (mustVisitNode != -1)
        {
            visited.clear(); // Must clear before resize to reset all values to false.
            visited.resize(coins.size(), false);
            dfsMustVisitEdges(-1, mustVisitNode);
        }
        return mustVisitEdges * 2;
    }
};