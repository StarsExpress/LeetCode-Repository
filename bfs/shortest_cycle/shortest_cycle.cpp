#include <vector>
#include <list>
#include <queue>
using namespace std;

int find_shortest_cycle(int n, vector<vector<int>> &edges)
{ // LeetCode Q.2608.
    vector<list<int>> graph(n);
    for (auto edge : edges)
    { // Undirected distinct edges.
        graph[edge[0]].push_back(edge[1]);
        graph[edge[1]].push_back(edge[0]);
    }

    int shortest_cycle = numeric_limits<int>::max();
    queue<pair<int, int>> queue; // Format: {node, parent}.
    for (int start_node = 0; start_node < n; start_node++)
    { // Find the shortest cycle starting from each node.
        // Each node's dist to its parent. -1 means unvisited.
        vector<int> parent_dists(n, -1);
        parent_dists[start_node] = 0;

        queue.push({start_node, start_node});
        while (!queue.empty())
        {
            auto [node, parent] = queue.front();
            queue.pop();

            for (int neighbor : graph[node])
            {
                if (neighbor != parent)
                { // Each edge must be visited just once.
                    if (parent_dists[neighbor] == -1)
                    { // Unvisited node.
                        parent_dists[neighbor] = parent_dists[node] + 1;
                        queue.push({neighbor, node});
                    }
                    else
                    { // Cycle forms.
                        int cycle_len = 1 + parent_dists[node] + parent_dists[neighbor];
                        if (cycle_len < shortest_cycle)
                        {
                            shortest_cycle = cycle_len;
                        }
                    }
                }
            }
        }
    }

    if (shortest_cycle == numeric_limits<int>::max())
    { // No cycle at all.
        return -1;
    }
    return shortest_cycle;
}
