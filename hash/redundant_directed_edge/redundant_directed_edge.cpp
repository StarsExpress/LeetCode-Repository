#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

class RedundantDirectedEdge
{ // LeetCode Q.685.
private:
    unordered_map<int, unordered_set<int>> graph;
    unordered_set<int> visited_nodes;

    bool test_connection(int start_node, int end_node)
    {
        visited_nodes.clear();
        if (graph.find(start_node) != graph.end())
        {
            if (graph[start_node].find(end_node) != graph[start_node].end())
            {
                graph[start_node].erase(end_node);
                bool connection = dfs_connection(start_node, end_node);
                graph[start_node].insert(end_node); // Restore the edge.
                return connection;
            }
        }

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
    vector<int> find_redundant_connection(vector<vector<int>> &edges)
    {
        unordered_map<int, int> in_degrees;

        unordered_set<string> visited_edges;
        vector<vector<int>> opposite_edges;

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

            string opposite_edge_id = to_string(in_node) + ":" + to_string(out_node);
            if (visited_edges.find(opposite_edge_id) != visited_edges.end())
            {
                opposite_edges.push_back({in_node, out_node});
                opposite_edges.push_back({out_node, in_node});
            }

            string edge_id = to_string(out_node) + ":" + to_string(in_node);
            visited_edges.insert(edge_id);
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

        if (!opposite_edges.empty())
        {
            int in_node = opposite_edges[1][1];

            if (root != -1)
            { // Root is detected.
                if (in_degrees[in_node] == 1)
                {                             // Remove current edge: gets another root.
                    return opposite_edges[0]; // Must remove the other edge.
                }
                return opposite_edges[1];
            }

            // An edge goes into root, preventing detection.
            if (in_degrees[in_node] == 1)
            { // Remove current edge: root shows up.
                return opposite_edges[1];
            }
            return opposite_edges[0];
        }

        reverse(edges.begin(), edges.end());
        for (auto edge : edges)
        { // Edge format: {out node, in node}.
            if (root != -1)
            { // Root is detected.
                if (in_degrees[edge[1]] == 2)
                {
                    if (root != edge[0] || test_connection(root, edge[1]))
                    {
                        return edge;
                    }
                }
                continue;
            }

            // Root not detected yet.
            if (in_degrees[edge[1]] == 1 && test_connection(edge[1], edge[0]))
            {
                return edge;
            }
        }

        return {};
    }
};
