#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <algorithm>
using namespace std;

class RedundantDirectedEdge
{ // LeetCode Q.685.
private:
    unordered_map<int, unordered_set<int>> graph;
    unordered_set<int> visitedNodes;

    void removeEdge(int outNode, int inNode)
    {
        if (graph.find(outNode) != graph.end())
        {
            if (graph[outNode].find(inNode) != graph[outNode].end())
                graph[outNode].erase(inNode);
        }
    }

    void restoreEdge(int outNode, int inNode)
    {
        graph[outNode].insert(inNode);
    }

    bool testConnection(int startNode, int endNode)
    {
        visitedNodes.clear();
        return dfsConnection(startNode, endNode);
    }

    bool dfsConnection(int startNode, int endNode)
    {
        visitedNodes.insert(startNode);
        if (graph.find(startNode) != graph.end())
        {
            for (auto neighborNode : graph[startNode])
            {
                if (neighborNode == endNode)
                    return true;

                if (visitedNodes.find(neighborNode) == visitedNodes.end())
                {
                    if (dfsConnection(neighborNode, endNode))
                        return true;
                }
            }
        }

        return false;
    }

public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>> &edges)
    {
        unordered_map<int, int> inDegrees;
        for (auto edge : edges)
        { // Edge format: {out node, in node}.
            int out_node = edge[0];
            int in_node = edge[1];

            if (graph.find(out_node) == graph.end())
                graph[out_node] = {};

            graph[out_node].insert(in_node);

            for (auto node : edge)
            {
                if (inDegrees.find(node) == inDegrees.end())
                    inDegrees[node] = 0;
            }
            inDegrees[in_node] += 1;
        }

        int root = -1;
        for (const auto &pair : inDegrees)
        {
            if (pair.second == 0)
            {
                root = pair.first;
                break;
            }
        }

        reverse(edges.begin(), edges.end());

        for (auto edge : edges)
        { // Edge format: {out node, in node}.
            if (root != -1)
            { // Root is detected.
                if (inDegrees[edge[1]] == 2)
                {
                    removeEdge(edge[0], edge[1]);
                    if (testConnection(root, edge[1]))
                        return edge; // Edge removal: root still visits in node.

                    restoreEdge(edge[0], edge[1]);
                }
                continue;
            }

            // Root not detected yet.
            removeEdge(edge[0], edge[1]);
            if (testConnection(edge[1], edge[0]))
                return edge; // Edge removal: in node still visits out node.

            restoreEdge(edge[0], edge[1]);
        }

        return {};
    }
};
