#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <deque>
using namespace std;

int find_min_reorder(vector<vector<int>> &connections) // LeetCode Q.1466.
{
    unordered_map<int, vector<int>> graph, reversed_graph;

    for (auto connection : connections)
    {
        int start = connection[0], end = connection[1];
        if (graph.find(start) == graph.end())
            graph[start] = {};
        graph[start].push_back(end);

        if (reversed_graph.find(end) == reversed_graph.end())
            reversed_graph[end] = {};
        reversed_graph[end].push_back(start);
    }

    int min_changes = 0;
    deque<int> queue = {0}; // Always start from capital.
    unordered_set<int> visited_nodes;

    while (!queue.empty())
    {
        int node = queue.front();
        queue.pop_front();
        visited_nodes.insert(node);

        // Go to next level BFS to check potential flips.
        if (graph.find(node) != graph.end())
        {
            for (auto outgoing_node : graph[node])
            {
                if (visited_nodes.find(outgoing_node) == visited_nodes.end())
                {
                    queue.push_back(outgoing_node);
                    min_changes++; // Flip to let this outgoing node visit current node.
                }
            }
        }

        if (reversed_graph.find(node) != reversed_graph.end())
        {
            for (auto incoming_node : reversed_graph[node])
            {
                if (visited_nodes.find(incoming_node) == visited_nodes.end())
                    queue.push_back(incoming_node);
            }
        }
    }

    return min_changes;
}
