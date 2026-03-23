#include <vector>
#include <unordered_set>
using namespace std;

class Provinces // LeetCode Q.547.
{
private:
    vector<vector<int>> graph;
    unordered_set<int> visitedCities;
    int totalCapitals = 0;

    void dfsProvinces(int city)
    {
        visitedCities.insert(city);
        for (int nextCity = 0; nextCity < graph[city].size(); nextCity++)
        {
            if (graph[city][nextCity] == 1)
            {
                if (visitedCities.find(nextCity) == visitedCities.end())
                    dfsProvinces(nextCity);
            }
        }
    }

public:
    int countProvinces(vector<vector<int>> &connections)
    {
        graph = connections;
        for (int city_1 = 0; city_1 < graph.size(); city_1++)
        {
            if (visitedCities.find(city_1) == visitedCities.end())
            {
                totalCapitals++;
                dfsProvinces(city_1);
            }
        }

        return totalCapitals;
    }
};