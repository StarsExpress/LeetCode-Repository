#include <vector>
#include <unordered_set>
using namespace std;

class CoinsCollector
{ // LeetCode Q.2603.
private:
    vector<unordered_set<int>> graph;

    vector<bool> leaves, leaves_parents; // If a node is a coin leave or parent of coin leave.
    vector<bool> required_visits;        // If a node must be visited to collect all coins.
    vector<bool> visited;                // For DFS visited marks.

    void dfs_required_visit_nodes(int node)
    {
        visited[node] = true;
        for (auto neighbor : graph[node])
        {
            if (leaves_parents[neighbor] == true && visited[neighbor] == false)
            {
                required_visits[node] = true;
                dfs_required_visit_nodes(neighbor);
            }
        }
    }

    int must_visit_edges = 0;
    bool dfs_must_visit_edges(int parent, int node)
    {
        visited[node] = true;
        for (auto neighbor : graph[node])
        {
            if (visited[neighbor] == false)
            {
                if (dfs_must_visit_edges(node, neighbor))
                {
                    required_visits[node] = true;
                }
            }
        }

        if (required_visits[node] && parent != -1)
        {
            must_visit_edges++;
        }
        return required_visits[node];
    }

    unordered_set<int> empty_parents;
    int max_empty_parents_dist = 1;
    int dfs_max_empty_parents_dist(int node)
    {
        visited[node] = true;
        vector<int> children_dists;
        for (auto neighbor : graph[node])
        {
            if (empty_parents.find(neighbor) != empty_parents.end())
            {
                if (visited[neighbor] == false)
                {
                    children_dists.push_back(dfs_max_empty_parents_dist(neighbor));
                }
            }
        }

        int local_max_dist = 1;
        if (children_dists.empty())
        {
            return local_max_dist;
        }

        sort(children_dists.begin(), children_dists.end());
        local_max_dist = children_dists.back();

        if (children_dists.size() >= 2)
        {
            local_max_dist += children_dists[children_dists.size() - 2];
        }
        if (local_max_dist > max_empty_parents_dist)
        {
            max_empty_parents_dist = local_max_dist;
        }

        return children_dists.back() + 1;
    }

public:
    int collectTheCoins(vector<int> &coins, vector<vector<int>> &edges)
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
        leaves_parents.resize(coins.size(), false);
        for (int node = 0; node < coins.size(); node++)
        {
            if (coins[node] == 1 && graph[node].size() == 1)
            {
                leaves[node] = true;

                int neighbor = *graph[node].begin();
                if (coins[neighbor] == 0 || graph[neighbor].size() > 1)
                {
                    leaves_parents[neighbor] = true;
                }
            }
        }

        bool parents_all_empty = true;
        required_visits.resize(coins.size(), false);
        for (int node = 0; node < coins.size(); node++)
        {
            if (leaves_parents[node])
            {
                bool is_empty_parent = true;

                for (auto neighbor : graph[node])
                {
                    if (leaves_parents[neighbor] == false && leaves[neighbor] == false)
                    {
                        required_visits[neighbor] = true;
                        is_empty_parent = false, parents_all_empty = false;
                    }
                }

                if (is_empty_parent)
                {
                    empty_parents.insert(node);
                }
            }
        }

        if (parents_all_empty)
        {
            if (empty_parents.empty())
            {
                return 0;
            }
            visited.resize(coins.size(), false);
            dfs_max_empty_parents_dist(*empty_parents.begin());
            return max(0, (max_empty_parents_dist - 2) * 2);
        }

        visited.clear(); // Must clear before resize to reset all values to false.
        visited.resize(coins.size(), false);
        int must_visit_node = -1;
        for (int node = 0; node < coins.size(); node++)
        {
            if (required_visits[node] && visited[node] == false)
            {
                must_visit_node = node;
                dfs_required_visit_nodes(node);
            }
        }

        if (must_visit_node != -1)
        {
            visited.clear(); // Must clear before resize to reset all values to false.
            visited.resize(coins.size(), false);
            dfs_must_visit_edges(-1, must_visit_node);
        }
        return must_visit_edges * 2;
    }
};