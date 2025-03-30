#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class RedundantDirectedEdge
{ // LeetCode Q.685.
private:
    unordered_map<int, unordered_set<int>> graph;
    unordered_set<int> visited_nodes;

    void remove_edge(int out_node, int in_node)
    {
        if (graph.find(out_node) != graph.end())
        {
            if (graph[out_node].find(in_node) != graph[out_node].end())
            {
                graph[out_node].erase(in_node);
            }
        }
    }

    void restore_edge(int out_node, int in_node)
    {
        graph[out_node].insert(in_node);
    }

    bool test_connection(int start_node, int end_node)
    {
        visited_nodes.clear();
        return dfs_connection(start_node, end_node);
    }

    bool dfs_connection(int start_node, int end_node)
    {
        visited_nodes.insert(start_node);
        if (graph.find(start_node) != graph.end())
        {
            for (auto neighbor_node : graph[start_node])
            {
                if (neighbor_node == end_node)
                {
                    return true;
                }

                if (visited_nodes.find(neighbor_node) == visited_nodes.end())
                {
                    if (dfs_connection(neighbor_node, end_node))
                    {
                        return true;
                    }
                }
            }
        }

        return false;
    }

public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>> &edges)
    {
        unordered_map<int, int> in_degrees;
        for (auto edge : edges)
        { // Edge format: {out node, in node}.
            int out_node = edge[0];
            int in_node = edge[1];
            if (graph.find(out_node) == graph.end())
            {
                graph[out_node] = {};
            }
            graph[out_node].insert(in_node);

            for (auto node : edge)
            {
                if (in_degrees.find(node) == in_degrees.end())
                {
                    in_degrees[node] = 0;
                }
            }
            in_degrees[in_node] += 1;
        }

        int root = -1;
        for (const auto &pair : in_degrees)
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
                if (in_degrees[edge[1]] == 2)
                {
                    remove_edge(edge[0], edge[1]);
                    if (test_connection(root, edge[1]))
                    {
                        return edge; // Edge removal: root still visits in node.
                    }
                    restore_edge(edge[0], edge[1]);
                }
                continue;
            }

            // Root not detected yet.
            remove_edge(edge[0], edge[1]);
            if (test_connection(edge[1], edge[0]))
            {
                return edge; // Edge removal: in node still visits out node.
            }
            restore_edge(edge[0], edge[1]);
        }

        return {};
    }
};
