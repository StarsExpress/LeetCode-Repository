#include <vector>
#include <unordered_set>
using namespace std;

class Provinces // LeetCode Q.547.
{
private:
    vector<vector<int>> graph;
    unordered_set<int> visited_cities;
    int total_capitals = 0;

    void dfs_provinces(int city)
    {
        visited_cities.insert(city);
        for (int next_city = 0; next_city < graph[city].size(); next_city++)
        {
            if (graph[city][next_city] == 1)
            {
                if (visited_cities.find(next_city) == visited_cities.end())
                    dfs_provinces(next_city);
            }
        }
    }

public:
    int count_provinces(vector<vector<int>> &connections)
    {
        graph = connections;
        for (int city_1 = 0; city_1 < graph.size(); city_1++)
        {
            if (visited_cities.find(city_1) == visited_cities.end())
            {
                total_capitals++;
                dfs_provinces(city_1);
            }
        }

        return total_capitals;
    }
};