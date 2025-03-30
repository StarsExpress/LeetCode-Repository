#include <vector>
#include <queue>
using namespace std;

class ShortestPathsCalculator
{ // LeetCode Q.2642.
private:
    vector<vector<int>> shortest_paths;
    int total_nodes;
    int infinity = numeric_limits<int>::max();

public:
    ShortestPathsCalculator(int n, vector<vector<int>> &edges)
    {
        shortest_paths.assign(n, vector<int>(n, infinity));
        for (auto edge : edges)
        { // Edge format: {out node, in node, cost}.
            shortest_paths[edge[0]][edge[1]] = edge[2];
        }
        for (int node = 0; node < n; node++)
        {
            shortest_paths[node][node] = 0; // Each node's cost to itself is 0.
        }
        total_nodes = n;
    }

    void add_edge(vector<int> edge)
    { // Edge format: {out node, in node, cost}.
        shortest_paths[edge[0]][edge[1]] = edge[2];
    }

    int calculate_shortest_path(int start, int end)
    {
        // Min heap. Format: {cost, node}.
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> cost_heap;

        for (int node = 0; node < total_nodes; node++)
        {
            if (start != node && shortest_paths[start][node] != infinity)
            {
                cost_heap.push({shortest_paths[start][node], node});
            }
        }

        while (!cost_heap.empty() && cost_heap.top().first != infinity)
        {
            auto [min_cost, min_cost_node] = cost_heap.top();
            cost_heap.pop();

            for (int neighbor = 0; neighbor < total_nodes; neighbor++)
            {
                int cost = shortest_paths[min_cost_node][neighbor];
                if (cost != infinity)
                {
                    if (min_cost + cost < shortest_paths[start][neighbor])
                    {
                        shortest_paths[start][neighbor] = min_cost + cost;
                        cost_heap.push({shortest_paths[start][neighbor], neighbor});
                    }
                }
            }
        }

        if (shortest_paths[start][end] == infinity)
        {
            return -1;
        }
        return shortest_paths[start][end];
    }
};