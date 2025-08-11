#include <vector>
using namespace std;

class MaxNodesSum
{ // LeetCode Q.3068.
private:
    vector<vector<int>> graph;
    vector<int> values;
    vector<bool> visited;

    long long value_sum = 0;
    int increments_count = 0;
    int min_increment = numeric_limits<int>::max();
    int max_decrement = -numeric_limits<int>::max();

    void dfs_increments(int node, int k)
    {
        visited[node] = true;

        value_sum += values[node];
        int increment = (values[node] ^ k) - values[node];
        if (increment > 0)
        {
            value_sum += increment;
            increments_count++;
            if (increment < min_increment)
                min_increment = increment;
        }
        else if (increment > max_decrement)
        {
            max_decrement = increment;
        }

        for (auto neighbor_node : graph[node])
        {
            if (visited[neighbor_node] == false)
                dfs_increments(neighbor_node, k);
        }
    }

public:
    long long maximize_value_sum(vector<int> &nums, int k, vector<vector<int>> &edges)
    {
        graph.resize(nums.size());
        for (auto edge : edges)
        {
            int node_1 = edge[0], node_2 = edge[1];
            graph[node_1].push_back(node_2);
            graph[node_2].push_back(node_1);
        }

        values = nums;
        visited.resize(nums.size(), false);
        dfs_increments(0, k);

        if (increments_count % 2 == 1)
            value_sum += max(-min_increment, max_decrement);
        return value_sum;
    }
};